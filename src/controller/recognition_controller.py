import traceback
from fastapi import APIRouter, UploadFile, File, HTTPException, status
from src.service.recognition_service import RecognitionService

router = APIRouter(
    prefix="/api/v1/recognition", 
    tags=["Face Recognition"]
)

@router.post("/")
async def recognize_faces_in_video(file: UploadFile = File(...)):
    if not file.content_type.startswith('video/'):
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail="Unsupported file type. Please upload a video."
        )
    
    try:
        recognition_service = RecognitionService()
        video_bytes = await file.read()
        results = recognition_service.process_video(video_bytes)
        return {"filename": file.filename, "results": results}
    except Exception as e:
        traceback.print_exc()

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {str(e)}"
        )