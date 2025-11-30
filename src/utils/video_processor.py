import cv2
import numpy as np
import tempfile
import os

def extract_frames(video_bytes: bytes, interval_seconds: int = 1):
    fp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    fp.write(video_bytes)
    fp.close()

    cap = cv2.VideoCapture(fp.name)

    if not cap.isOpened():
        os.unlink(fp.name)
        raise ValueError("Could not open video stream from bytes")
        
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_interval = int(fps * interval_seconds) if fps > 0 and fps < 200 else 30
    
    frame_count = 0
    success = True
    while success:
        success, frame = cap.read()
        if not success:
            break
        
        if frame_count % frame_interval == 0:
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            yield frame_count, rgb_frame, fps
        
        frame_count += 1
        
    cap.release()
    os.unlink(fp.name)