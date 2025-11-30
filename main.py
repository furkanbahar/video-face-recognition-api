from fastapi import FastAPI
from src.controller import recognition_controller

app = FastAPI(
    title="PersonaVision API",
    version="1.0.0"
)

app.include_router(recognition_controller.router)