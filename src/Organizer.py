import os
import shutil
from pathlib import Path


class Organizer:

  def __init__(self, given_path):
    self.path_to_sort = given_path
    self.directories = {
      "HTML": [".html5", ".html", ".htm", ".xhtml"],
      "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg",
                 ".svg", ".heif", ".psd"],
      "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob",
                 ".mng", ".qt", ".mpg", ".mpeg", ".3gp"],
      "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                    ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                    ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                    ".pptx"],
      "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                   ".dmg", ".rar", ".xar", ".zip"],
      "AUDIO": [".aac", ".aa", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
                ".msv", ".ogg", ".oga", ".raw", ".vox", ".wav", ".wma"],
      "PLAINTEXT": [".txt", ".in", ".out"],
      "PDF": [".pdf"],
      "PYTHON": [".py"],
      "XML": [".xml"],
      "EXE": [".exe"],
      "SHELL": [".sh"],
      "C": [".c"],
      "ASSEMBLY": [".asm"],
      "RISC_V": [".s"],
      "MISC": []
    }

  def __get_unique_filename(self, file_path):
    """Generate a unique filename by adding a numerical suffix if needed."""
    counter = 1
    new_file_path = file_path
    while new_file_path.exists():
      new_file_path = file_path.with_name(f"{file_path.stem}_{counter}{file_path.suffix}")
      counter += 1
    return new_file_path

  def __create_folders(self):
    """Create necessary directories for sorting files."""
    for directory in self.directories:
      folder_path = Path(self.path_to_sort) / directory
      folder_path.mkdir(parents=True, exist_ok=True)

  def __sort(self):
    """Sort files into respective folders based on their extensions."""
    for entry in os.scandir(self.path_to_sort):
      if entry.is_dir():
        continue
      file_path = Path(entry)
      file_type = file_path.suffix.lower()

      # Skip macOS metadata files
      if file_path.name == ".DS_Store":
        continue

      matched = False
      for file_folder, file_extensions in self.directories.items():
        if file_type in file_extensions:
          destination_folder = Path(self.path_to_sort) / file_folder
          destination_file = destination_folder / file_path.name

          if destination_file.exists():
            destination_file = self.__get_unique_filename(destination_file)

          shutil.move(file_path, destination_file)
          matched = True
          break  # Stop searching once a match is found

      if not matched:
        destination_folder = Path(self.path_to_sort) / "MISC"
        destination_file = destination_folder / file_path.name

        if destination_file.exists():
          destination_file = self.__get_unique_filename(destination_file)

        shutil.move(file_path, destination_file)

  def organize(self):
    """Public method to trigger file organization."""
    self.__create_folders()
    self.__sort()
