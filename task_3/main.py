import sys
from pathlib import Path
from colorama import Fore

def dir_struct_visual(dir_path, indent=""):

    if not Path(dir_path).is_dir():
        print("Error: Directory not found.")
        sys.exit(1)
    
    dir = Path(dir_path)
    print(indent + Fore.BLUE + f"{dir.name}/")

    for item in Path(dir_path).iterdir():
        color = Fore.BLUE if item.is_dir() else Fore.GREEN
        if item.is_dir():
            dir_struct_visual(item, indent + "  ")
        else:
            print(indent + "  " + color + str(item.name))

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Error: Path to directory not found.")
        sys.exit(1)

    dir_path = sys.argv[1]
    dir_struct_visual(dir_path)