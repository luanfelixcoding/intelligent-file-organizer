import logging
from pathlib import Path

log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)
log_path = log_dir / "organizer.log"

logging.basicConfig(
    filename=log_path,
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logger = logging.getLogger("organizer")
