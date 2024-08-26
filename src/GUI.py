import os

import customtkinter as ctk
from tkinter import filedialog
from Organizer import Organizer

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):

  def __init__(self):
    super().__init__()

    self.organizer = None

    self.title("Download Organizer")
    self.geometry("500x300")

    self.columnconfigure(0, weight=1)
    self.columnconfigure(1, weight=1)
    self.columnconfigure(2, weight=1)
    self.rowconfigure(0, weight=1)

    self.entry_path = ctk.CTkEntry(self, width=300)
    self.entry_path.grid(row=0, column=0)

    self.button_browse = ctk.CTkButton(self, text="Browse Directory",
                                       command=self.select_download_folder)
    self.button_browse.grid(row=0, column=1)

    self.button_action = ctk.CTkButton(self, text="Submit",
                                       command=self.on_button_click)
    self.button_action.grid(row=0, column=2)

  def select_download_folder(self):
    folder_selected = filedialog.askdirectory(
      initialdir=os.path.expanduser("~/Downloads"))
    if folder_selected:
      self.entry_path.delete(0, ctk.END)
      self.entry_path.insert(0, folder_selected)
    self.organizer = Organizer(folder_selected)

  def on_button_click(self):
    if self.organizer is None:
      print("Please select a directory first.")
      return
    self.organizer.organize()

if __name__ == "__main__":
  app = App()
  app.mainloop()
