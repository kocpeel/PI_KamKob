import tkinter as tk

# PIP INSTALL TKINTER IF YOU DON'T HAVE ONE

from adfgvx import ADFGVX

class UserInterface:
   def __init__(self):
       self.root = tk.Tk()
       self.root.title("ADFGVX Cipher")
       self.input_label = tk.Label(self.root, text="Input:")
       self.input_entry = tk.Entry(self.root)
       self.encrypt_button = tk.Button(self.root, text="Encrypt", command=self.encrypt)
       self.decrypt_button = tk.Button(self.root, text="Decrypt", command=self.decrypt)
       self.output_label = tk.Label(self.root, text="Output:")
       self.output_text = tk.Text(self.root)

       self.input_label.pack()
       self.input_entry.pack()
       self.encrypt_button.pack()
       self.decrypt_button.pack()
       self.output_label.pack()
       self.output_text.pack()

   def encrypt(self):
       message = self.input_entry.get().upper()
       key = 'KEY'
       cipher = ADFGVX('QWERTYUIOPASDFGHJKLZXCVBNM', key) # POLIBEUS SQUARE MARK (+)
       result = cipher.encrypt(message)
       self.output_text.delete(1.0, tk.END)
       self.output_text.insert(tk.END, result)

   def decrypt(self):
       message = self.input_entry.get().upper()
       key = 'KEY'
       cipher = ADFGVX('QWERTYUIOPASDFGHJKLZXCVBNM', key) # POLIBEUS SQUARE MARK (+)
       result = cipher.decrypt(message)
       self.output_text.delete(1.0, tk.END)
       self.output_text.insert(tk.END, result)