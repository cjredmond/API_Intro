import requests
import sys
from functions import search_name, ask_info, ask_value, search, info

def main():
    choice = input("(S)earch, (N)ame, (I)nfo, or Q(uit)\n").lower()
    if choice == "i":
        info(ask_info())
        main()
    elif choice == "s":
        stuff = ask_value(ask_info())
        search(stuff[0], stuff[1])
        main()
    elif choice == "n":
        search_name()
        main()
    elif choice == "q":
        sys.exit()
    else:
        main()

main()
