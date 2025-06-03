from config import DESTINATION_FOLDER, FOLDER_RULES
from utils import get_file_extension, create_folder_if_not_exist
from logger import logger
from pathlib import Path
import shutil


class FileOrganizer:
    def __init__(self) -> None:
        self.rules = FOLDER_RULES
        self.dest_folder = DESTINATION_FOLDER

    def organize(self, file_path: Path) -> None:
        ext = get_file_extension(file_path)
        for folder_name, extensions in self.rules.items():
            if ext in extensions:
                target_folder = self.dest_folder / folder_name
                break
        else:
            target_folder = self.dest_folder / "Outros"

        create_folder_if_not_exist(target_folder)

        try:
            new_path = target_folder / file_path.name
            shutil.move(str(file_path), str(new_path))
            logger.info(f"File moved: {file_path} → {new_path}")
        except Exception as unknown_error:
            logger.error(f"Error in moving {file_path}: {unknown_error}")
