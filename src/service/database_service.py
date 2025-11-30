import psycopg2
from psycopg2.extras import RealDictCursor
from pydantic_settings import BaseSettings
from typing import List, Dict, Any

class Settings(BaseSettings):
    db_host: str
    db_port: int
    db_name: str
    db_user: str
    db_password: str

class DatabaseService:
    def __init__(self):
        self.settings = Settings()
        self.dsn = (
            f"host={self.settings.db_host} "
            f"port={self.settings.db_port} "
            f"dbname={self.settings.db_name} "
            f"user={self.settings.db_user} "
            f"password={self.settings.db_password}"
        )
        self.connection = None

    def _connect(self):
        try:
            if not self.connection or self.connection.closed:
                self.connection = psycopg2.connect(self.dsn)
        except psycopg2.DatabaseError as e:
            raise ConnectionError(f"Database connection failed: {e}")

    def _disconnect(self):
        if self.connection and not self.connection.closed:
            self.connection.close()

    def get_known_faces(self) -> List[Dict[str, Any]]:
        self._connect()
        try:
            with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(
                    "SELECT id, name, surname, title, face_encoding_base64 FROM face"
                )
                results = cursor.fetchall()
                return results
        except psycopg2.Error as e:
            raise RuntimeError(f"Failed to fetch data from database: {e}")
        finally:
            self._disconnect()