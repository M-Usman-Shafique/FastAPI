from dotenv import load_dotenv
import os

load_dotenv()

API_URL = os.getenv("API_URL")
DATABASE_URL: str = os.getenv("DATABASE_URL") or "sqlite:///sqlite.db"

