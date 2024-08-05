import unittest
import tempfile
import os
import shutil
from pathlib import Path
from src.Organizer import Organizer

class OrganizerTest(unittest.TestCase):

  def setUp(self):
    # Create a temporary directory
    self.test_dir = tempfile.TemporaryDirectory()
    self.download_path = self.test_dir.name

    # Create test files
    self.test_files = {
      "test.html": "HTML",
      "image.jpg": "IMAGES",
      "video.mp4": "VIDEOS",
      "document.docx": "DOCUMENTS",
      "archive.zip": "ARCHIVES",
      "audio.mp3": "AUDIO",
      "plaintext.txt": "PLAINTEXT",
      "file.pdf": "PDF",
      "script.py": "PYTHON",
      "data.xml": "XML",
      "program.exe": "EXE",
      "script.sh": "SHELL"
    }

    for file_name in self.test_files:
      file_path = Path(self.download_path) / file_name
      file_path.touch()  # Create an empty file

  def tearDown(self):
    # Cleanup the temporary directory
    self.test_dir.cleanup()

  def test_organize(self):
    organizer = Organizer(self.download_path)
    organizer.organize()

    for file_name, folder in self.test_files.items():
      expected_path = Path(self.download_path) / folder / file_name
      self.assertTrue(expected_path.exists(), f"{file_name} was not moved to {folder} folder")

    # Check that the directories are created
    for folder in organizer.directories.keys():
      folder_path = Path(self.download_path) / folder
      self.assertTrue(folder_path.exists(), f"Directory {folder} was not created")

if __name__ == "__main__":
  unittest.main()
