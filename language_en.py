class LanguageEN:

    @staticmethod
    def mode_select():
        print("Choose how do you want to scan the network: \n")
        print("1) Automatically scan the network")
        print("2) Set available options before starting the scan")
        print("e) exit\n")

    @staticmethod
    def manual_network():
        print("Select scan range: \n")
        print("1) 24 (standard)")
        print("2) 16")
        print("3) 8\n")

    @staticmethod
    def manual_select_option1():
        print("Standard mod. I don't change anything.")

    @staticmethod
    def manual_select_option_else():
        print("There is no such option!")

    @staticmethod
    def manual_system_id():
        print("\nDo you want to try recognize the system of a device?")
        print("ATTENTION! This may take a while!\n")
        print("1) yes")
        print("2) no\n")

    @staticmethod
    def manual_system_id_standard():
        print("\nStandard setting, I don't make any changes. ")
