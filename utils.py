from pathlib import Path


def get_file_extension(file_path: Path) -> str:
    return file_path.suffix.lower()


def create_folder_if_not_exist(folder_path: Path) -> None:
    folder_path.mkdir(parents=True, exist_ok=True)
