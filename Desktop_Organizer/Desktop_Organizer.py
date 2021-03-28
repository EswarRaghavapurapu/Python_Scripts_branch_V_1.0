import os
from pathlib import Path

# Initiate list of Directories and File formats as dictionary
DIRECTORIES = {
    "HTML": [".html5", ".html", ".htm", ".xhtml"],
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
               ".heif", ".psd"],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp"],
    "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  "pptx"],
    "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"],
    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
    "PLAINTEXT": [".txt", ".in", ".out"],
    "PDF": [".pdf"],
    "PYTHON": [".py"],
    "XML": [".xml"],
    "EXE": [".exe"],
    "SHELL": [".sh"]
  
}

# Map the file formats with directory  
FILE_FORMATS = {file_format: directory
                for directory, file_formats in DIRECTORIES.items()
                for file_format in file_formats}
    
def organize_junk(input_path):
    for entry in os.scandir(input_path):
        if entry.is_dir():
            continue
        file_path = Path(entry)
        file_format = file_path.suffix.lower()
        if file_format in FILE_FORMATS:
            directory_name = FILE_FORMATS[file_format]
            directory_path = os.path.join(os.getcwd(),directory_name)
            if not os.path.exists(directory_path):
                os.mkdir(directory_path)
            file_path.rename(os.path.join(os.getcwd(),directory_name,os.path.basename(file_path)))
        for dir in os.scandir():
            print(dir)
            try:
                os.rmdir(dir)
            except:
                pass
  
if __name__ == "__main__":
    input_path = r'.......\Desktop'
    organize_junk(input_path)

