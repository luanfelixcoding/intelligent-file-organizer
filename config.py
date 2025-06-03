from pathlib import Path

# Folder to be watched
WATCHED_FOLDER = Path.home() / "Downloads"

# Folder Rules Organization by type of files
FOLDER_RULES = {
    "Documentos": [".pdf", ".docx", ".txt"],
    "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
    "Planilhas": [".xls", ".xlsx", ".csv"],
    "Executáveis": [".exe", ".msi"],
    "Compactados": [".zip", ".rar", ".7z"],
    "Outros": []
}

DESTINATION_FOLDER = Path.home() / "Desktop" / "Organized_Files"
