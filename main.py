from ui import UserInterface
from adfgvx import ADFGVX

if __name__ == "__main__":
   interface = UserInterface()
   cipher = ADFGVX('QWERTYUIOPASDFGHJKLZXCVBNM', 'KEY') # POLIBEUS SQUARE MARK (X)
   interface.root.mainloop()