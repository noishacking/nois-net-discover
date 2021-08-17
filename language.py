import os
import re
import subprocess
import sys


class Language:

    @staticmethod
    def default_language():
        """Gets the system language and return."""
        if re.findall("pl_PL", os.getenv('LANG')):
            return "pl"
        else:
            return "en"

    @staticmethod
    def choose_language():
        """Menu with language selection. It is possible to choose the language, not only the system language."""
        subprocess.run("clear")

        while True:
            print("Wybierz swój język / Choose your language: \n")
            print("1) Polski")
            print("2) English")
            print("e) exit")

            language = input("\n:> ")

            if language == "1":
                return "pl"
            elif language == "2":
                return "en"
            elif language == "e":
                print("Koniec programu / End of program")
                sys.exit()
            else:
                print("\nWybrałeś złą opcję! / You selected wrong option\n")
