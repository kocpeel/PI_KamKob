from ui import UserInterface
from adfgvx import ADFGVX

if __name__ == "__main__":
   interface = UserInterface()
   cipher = ADFGVX('POLYBIUS SQUARE', 'KEY')
   interface.root.mainloop()