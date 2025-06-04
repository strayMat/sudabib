import os
from pathlib import Path

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

DIR2ROOT = Path(__file__).parent.parent.absolute()

DIR2DATA = DIR2ROOT / "data"

DEFAULT_MODEL = "gemini-2.5-flash-preview-05-20"
DEFAULT_LOCAL_MODEL = "llama3.2:1b"

DEFAULT_OPEN_ALEX_MAIL = "matt.dout@gmail.com"
