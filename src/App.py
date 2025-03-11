import os

import customtkinter as ctk
from tkinter import filedialog, messagebox
from Organizer import Organizer
from pathlib import Path

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):

  def __init__(self):
    super().__init__()

    self.organizer = None

    self.title("Directory Organizer")
    self.geometry("500x300")

    self.columnconfigure(0, weight=1)
    self.columnconfigure(1, weight=1)
    self.columnconfigure(2, weight=1)
    self.rowconfigure(0, weight=1)

    self.entry_path = ctk.CTkEntry(self, width=300)
    self.entry_path.configure(state="disabled")
    self.entry_path.grid(row=0, column=0)

    self.button_browse = ctk.CTkButton(self, text="Browse Directory",
                                       command=self.__select_download_folder)
    self.button_browse.grid(row=0, column=1)

    self.button_action = ctk.CTkButton(self, text="Organize",
                                       command=self.__execute_organization)
    self.button_action.grid(row=0, column=2)

  def __select_download_folder(self):
    """Open a file dialog to select a directory for organization."""
    folder_selected = filedialog.askdirectory(
        initialdir=Path.home())
    if folder_selected:
      self.entry_path.configure(state="normal")
      self.entry_path.delete(0, ctk.END)
      self.entry_path.insert(0, folder_selected)
      self.entry_path.configure(state="disabled")
    self.organizer = Organizer(folder_selected)

  def __execute_organization(self):
    """Trigger the organization process."""
    if self.organizer is None:
      messagebox.showerror("Error", "Please select a directory first.")
      return

    execution = messagebox.askyesnocancel("Confirmation",
                                          "Are you sure you want "
                                          "to organize the directory?")
    if execution is None:
      return

    self.organizer.organize()
    messagebox.showinfo("Success", "Directory has been organized.")


if __name__ == "__main__":
  app = App()
  app.mainloop()
