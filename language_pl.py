class LanguagePL:

    @staticmethod
    def mode_select():
        print("Wybierz w jaki sposób chcesz przeprowadzić skanowanie sieci:\n")
        print("1) Automatycznie przeskanuj całą sieć")
        print("2) Ustaw dostępne opcje przed rozpoczęciem skanowania")
        print("e) wyjdź\n")

    @staticmethod
    def manual_network():
        print("Wybierz zakres skanowania:\n ")
        print("1) 24 (standard)")
        print("2) 16")
        print("3) 8\n")

    @staticmethod
    def manual_select_option1():
        print("Mod standardowy. Nie zmieniam nic.")

    @staticmethod
    def manual_select_option_else():
        print("Nie istnieje taka opcja!")

    @staticmethod
    def manual_system_id():
        print("\nCzy chcesz aby program spróbował rozpoznać system danego urządzenia ?")
        print("UWAGA! Może to zająć dłuższą chwilę!\n")
        print("1) tak")
        print("2) nie\n")

    @staticmethod
    def manual_system_id_standard():
        print("\nUstawienie standardowe, nie wprowadzam żadnych zmian.")
