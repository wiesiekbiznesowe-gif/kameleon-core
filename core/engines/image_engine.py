import os
import uuid
from datetime import datetime

from core.base_engine import BaseEngine


class ImageEngine(BaseEngine):
    """
    Pierwszy produkcyjny silnik Kameleona.
    Wersja LOCAL – generuje plik obrazu (dummy) bez zewnętrznych API.
    """

    def __init__(self):
        super().__init__("image")

    def execute(self, payload: dict) -> dict:
        prompt = payload.get("prompt")

        if not prompt:
            return {
                "status": "error",
                "message": "No prompt provided"
            }

        # Tworzymy katalog output jeśli nie istnieje
        output_dir = "output/images"
        os.makedirs(output_dir, exist_ok=True)

        # Unikalna nazwa pliku
        file_id = str(uuid.uuid4())[:8]
        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        filename = f"image_{timestamp}_{file_id}.txt"

        file_path = os.path.join(output_dir, filename)

        # Na start zapisujemy prompt do pliku (dummy generacja)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("KAMELEON IMAGE ENGINE\n")
            f.write(f"Generated at: {timestamp} UTC\n")
            f.write(f"Prompt: {prompt}\n")

        return {
            "status": "success",
            "engine": "image",
            "file_path": file_path,
            "prompt": prompt
        }
