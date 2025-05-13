import colorama
from colorama import Fore, Style

def greet():
    print(Fore.GREEN + "Hello from halo-tea!" + Style.RESET_ALL)

if __name__ == "__main__":
    greet()
