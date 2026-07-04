from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    BASE_URL = os.getenv("BASE_URL")
    BROWSER = os.getenv("BROWSER")
    HEADLESS = os.getenv("HEADLESS", "False").lower() == "true"

    IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", "10"))
    EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "20"))

    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")


settings = Settings()