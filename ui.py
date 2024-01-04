import tkinter as tk
from tkinter import messagebox

class UserInterface:
   def __init__(self):
       self.root = tk.Tk()
       self.root.title("ADFGVX Cipher")

   def get_action(self):
       return messagebox.askyesno("Action", "Encrypt or Decrypt?")

   def get_message(self):
    while True:
        message = messagebox.askstring("Message", "Enter the message")
        if message:
             return message
   def get_key(self):
        while True:
           key = messagebox.askstring("Key", "Enter the key")
           if key:
             return key

   def show_result(self, result):
       messagebox.showinfo("Result", result)

   def run(self):
       self.root.mainloop()