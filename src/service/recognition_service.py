import face_recognition
import numpy as np
import base64
import io
from PIL import Image
from typing import List, Dict, Any

from src.service.database_service import DatabaseService
from src.utils.video_processor import extract_frames

class RecognitionService:
    def __init__(self, tolerance: float = 0.5):
        self.db_service = DatabaseService()
        self.tolerance = tolerance
        self.known_face_encodings = []
        self.known_face_metadata = []

    def _load_known_faces(self):
        """Veritabanından bilinen yüzleri yükler ve kodlamaları hazırlar."""
        db_records = self.db_service.get_known_faces()
        for record in db_records:
            try:
                base64_string = record["face_encoding_base64"].strip()
                image_bytes = base64.b64decode(base64_string)
                image = Image.open(io.BytesIO(image_bytes))
                image_rgb = image.convert("RGB")
                image_np = np.array(image_rgb)
                
                encodings = face_recognition.face_encodings(image_np)
                if encodings:
                    self.known_face_encodings.append(encodings[0])
                    self.known_face_metadata.append({
                        "name": f"{record['name']} {record['surname']}",
                        "title": record['title']
                    })
            except Exception:
                continue

    def process_video(self, video_bytes: bytes) -> Dict[str, Any]:
        """Videodaki yüzleri işler ve bilinen yüzlerle karşılaştırır."""
        self._load_known_faces()
        if not self.known_face_encodings:
            return {"error": "Veritabanında geçerli bir yüz kaydı bulunamadı."}
        
        frame_generator = extract_frames(video_bytes)
        recognized_people = {}

        for frame_number, frame, fps in frame_generator:
            face_locations = face_recognition.face_locations(frame)
            face_encodings = face_recognition.face_encodings(frame, face_locations)

            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(
                    self.known_face_encodings, face_encoding, tolerance=self.tolerance
                )
                
                face_distances = face_recognition.face_distance(
                    self.known_face_encodings, face_encoding
                )
                
                best_match_index = np.argmin(face_distances)

                if matches[best_match_index]:
                    metadata = self.known_face_metadata[best_match_index]
                    name = metadata["name"]
                    confidence = 1 - face_distances[best_match_index]
                    if confidence >= 0.5:
                        timestamp_seconds = round(frame_number / fps, 2) if fps > 0 else 0
                        if name not in recognized_people or confidence > recognized_people[name]["confidence"]:
                            recognized_people[name] = {
                                "title": metadata["title"],
                                "confidence": round(confidence, 4),
                                "tespit_edildigi_saniye": timestamp_seconds
                            }
        
        return recognized_people