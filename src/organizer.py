# navigate into the download directory
# and organize the files into folders according to their types
# and move them to their respective folders

import os
import shutil
from pathlib import Path


class Organizer:

  def __init__(self, download_path):
    self.download_path = download_path
    self.directories = {
      "HTML": [".html5", ".html", ".htm", ".xhtml"],
      "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg",
                 "svg",
                 ".heif", ".psd"],
      "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob",
                 ".mng",
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

  def __create_folders(self):
    for directory in self.directories:
      folder_path = Path(self.download_path) / directory
      if not folder_path.exists():
        folder_path.mkdir(directory)

  def organize(self):
    for entry in os.scandir(self.download_path):
      if entry.is_dir():
        continue
      file_path = Path(entry)
      file_type = file_path.suffix.lower()
      for file_folder, file_extensions in self.directories.items():
        if file_type in file_extensions:
          destination_folder = Path(self.download_path) / file_folder
          shutil.move(file_path, destination_folder)


  def organize(self):
    self.__create_folders()
    self.__sort()

if __name__ == "__main__":
  # Set the path to the download directory
  # TODO: Set the directory automatically depending on the OS and user
  download_dir = '/Users/danielwendt/Downloads'

  # Create an instance of Organizer and run the methods
  organizer = Organizer(download_dir)
  organizer.create_folders()
  organizer.organize()
