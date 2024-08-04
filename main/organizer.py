# navigate into the download directory
# and organize the files into folders according to their types
# and move them to their respective folders

import os
import shutil
from pathlib import Path


class Organizer:

  def __init__(self):
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
      if not os.path.exists(directory):
        os.mkdir(directory)

  def __sort(self):
    for entry in os.scandir():
      if entry.is_dir():
        continue
      file_path = Path(entry)
      file_type = file_path.suffix.lower()
      for file_folder, file_extension in self.directories.items():
        if file_type in file_extension:
          shutil.move(file_path, file_folder)

  def organize(self):
    self.__create_folders()
    self.__sort()

  #set the path to the download directory
  #TODO: the directory should be set automatically, depending on the OS and user
  #os.chdir('/Users/danielwendt/Downloads')
  #create_folders()
  #organize()
