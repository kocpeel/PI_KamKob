from ui import UserInterface
from adfgvx import ADFGVX

def main():
   interface = UserInterface()
   cipher = ADFGVX('POLYBIUS SQUARE', 'KEY')

   while True:
       action = interface.get_action()
       if action == 'encrypt':
           message = interface.get_message()
           key = interface.get_key()
           result = cipher.encrypt(message, key)
           interface.show_result(result)
       elif action == 'decrypt':
           ciphertext = interface.get_ciphertext()
           key = interface.get_key()
           result = cipher.decrypt(ciphertext, key)
           interface.show_result(result)
       else:
           break

if __name__ == "__main__":
   main()