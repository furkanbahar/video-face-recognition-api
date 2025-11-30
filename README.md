# PersonaVision API - Video Face Recognition System

PersonaVision is a robust RESTful API designed for automated face recognition in video files. Built with FastAPI and Python, it processes uploaded videos to identify and recognize faces, leveraging powerful computer vision libraries.

## 🚀 Features

*   **Video Processing**: Efficiently handles video uploads and frame extraction.
*   **Face Recognition**: Utilizes `face_recognition` and `OpenCV` to detect and identify faces within video frames.
*   **RESTful API**: Provides a clean and documented API endpoint for easy integration.
*   **Dockerized**: Fully containerized application with Docker and Docker Compose for easy deployment.
*   **Database Integration**: Includes PostgreSQL integration for storing recognition data (implied by project structure).

## 🛠️ Tech Stack

*   **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
*   **Language**: Python 3.9+
*   **Computer Vision**: `face_recognition`, `opencv-python-headless`
*   **Database**: PostgreSQL (`psycopg2-binary`)
*   **Containerization**: Docker, Docker Compose

## 📂 Project Structure

```
.
├── src/
│   ├── controller/       # API route handlers
│   ├── service/          # Business logic (Recognition, Database)
│   └── utils/            # Utility functions
├── main.py               # Application entry point
├── Dockerfile            # Docker build instructions
├── docker-compose.yml    # Docker services configuration
├── init.sql              # Database initialization script
└── requirements.txt      # Python dependencies
```

## ⚡ Installation & Setup

### Option 1: Using Docker (Recommended)

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd videoarchive-facerecognation-main
    ```

2.  **Build and run the containers:**
    ```bash
    docker-compose up --build
    ```

3.  The API will be available at `http://localhost:8000`.

### Option 2: Local Installation

1.  **Prerequisites:**
    *   Python 3.8+
    *   CMake (required for `face_recognition` library)

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```bash
    uvicorn main:app --reload
    ```

## 📖 API Documentation

Once the application is running, you can access the interactive API documentation (Swagger UI) at:

*   **URL**: `http://localhost:8000/docs`

### Endpoints

*   `POST /api/v1/recognition/`: Upload a video file to perform face recognition.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

[MIT License](LICENSE)

