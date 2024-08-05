import unittest
import tempfile
from pathlib import Path
from src.Organizer import Organizer

class OrganizerTest(unittest.TestCase):

  def setUp(self):
    # Create a temporary directory
    self.test_dir = tempfile.TemporaryDirectory()
    self.download_path = self.test_dir.name
    self.organizer = Organizer(self.download_path)

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

  def test_create_folders(self):
    self.organizer._Organizer__create_folders()

    for folder in self.organizer.directories.keys():
      folder_path = Path(self.download_path) / folder
      self.assertTrue(folder_path.exists(), f"Directory {folder} was not created")

  def test_sort(self):
    self.organizer._Organizer__create_folders()
    self.organizer._Organizer__sort()

    for file_name, folder in self.test_files.items():
      expected_path = Path(self.download_path) / folder / file_name
      self.assertTrue(expected_path.exists(), f"{file_name} was not moved to {folder} folder")

  def test_organize(self):
    self.organizer.organize()

    for file_name, folder in self.test_files.items():
      expected_path = Path(self.download_path) / folder / file_name
      self.assertTrue(expected_path.exists(), f"{file_name} was not moved to {folder} folder")

    # Check that the directories are created
    for folder in self.organizer.directories.keys():
      folder_path = Path(self.download_path) / folder
      self.assertTrue(folder_path.exists(), f"Directory {folder} was not created")

if __name__ == "__main__":
  unittest.main()
