import unittest
from unittest.mock import patch, MagicMock
import customtkinter as ctk
from src.GUI import App
from src.Organizer import Organizer


class TestAppGUI(unittest.TestCase):

  def setUp(self):
    self.app = App()

  def tearDown(self):
    self.app.destroy()

  def test_entry_creation(self):
    self.assertIsInstance(self.app.entry_path, ctk.CTkEntry)

  def test_button_browse_creation(self):
    self.assertIsInstance(self.app.button_browse, ctk.CTkButton)

  def test_button_action_creation(self):
    self.assertIsInstance(self.app.button_action, ctk.CTkButton)

  @patch("tkinter.filedialog.askdirectory", return_value="/mocked/path")
  @patch("Organizer")
  def test_select_download_folder(self, mock_organizer_class, mock_askdirectory):
    # Simuliere den Button-Klick für "Browse Directory"
    self.app.button_browse.invoke()

    # Überprüfe, ob der korrekte Pfad im Entry-Feld steht
    self.assertEqual(self.app.entry_path.get(), "/mocked/path")

    # Überprüfe, ob der Organizer mit dem richtigen Pfad instanziiert wurde
    mock_organizer_class.assert_called_with("/mocked/path")
    self.assertIsNotNone(self.app.organizer)

  @patch.object(Organizer, 'organize')
  @patch("tkinter.filedialog.askdirectory", return_value="/mocked/path")
  def test_on_button_click(self, mock_askdirectory, mock_organize):
    # Simuliere das Auswählen eines Ordners
    self.app.select_download_folder()

    # Simuliere den Button-Klick für "Submit"
    self.app.button_action.invoke()

    # Überprüfe, ob die Methode 'organize' auf dem Organizer aufgerufen wurde
    mock_organize.assert_called_once()

if __name__ == "__main__":
  unittest.main()
