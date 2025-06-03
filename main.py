from watcher import start_watching
from logger import logger

if __name__ == "__main__":
    logger.info("Initializing folder monitoring...")
    start_watching()
