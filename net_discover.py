import re
import subprocess
import sys

import scapy.all as scapy

import language
import language_en
import language_pl


class NetDiscover:

    def __init__(self):
        self.default_language = language.Language.default_language
        self.language_set = None
        self.range = "24"
        self.id_system = 1

    def _set_default_language(self, default_language):
        """ Setting the selected language, overwriting the default one """
        if default_language == "pl":
            self.language_set = language_pl.LanguagePL()
        else:
            self.language_set = language_en.LanguageEN()

    @staticmethod
    def _installation():
        """Installing necessary software"""
        try:
            subprocess.run(["nmap", "-v"], capture_output=True)
        except FileNotFoundError:
            subprocess.run(["sudo", "apt-get", "install", "nmap"], capture_output=True)

    @staticmethod
    def _network(scope):
        """Range scan setting"""
        my_ip = scapy.ARP().psrc
        network = my_ip[:-1]  # slice of my network address
        network += "1/" + scope  # instruction for scanning the network from start
        return network

    def _network_clients(self):
        """scanning the entire network"""
        request = scapy.ARP(pdst=self._network(self.range))
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        request_and_broadcast = broadcast/request
        return scapy.srp(request_and_broadcast, timeout=1, verbose=False)[0]

    @staticmethod
    def _nmap_system(ip):
        """nmap system scan"""
        nmap_result = subprocess.run(["sudo", "nmap", ip, "-O", "-max-os-tries 1"], capture_output=True)
        ip_os = re.findall('(OS details:\s)(.*\d)', nmap_result.stdout.decode())
        return ip_os[0][1]

    def network_list(self, mode):
        """list of devices in the network """
        answer = self._network_clients()
        network_list = []

        if mode == 1:
            for element in answer:
                network = {"ip": element[1].psrc, "mac": element[1].hwsrc}
                network_list.append(network)
        else:
            for element in answer:
                try:
                    os_system = self._nmap_system(element[1].psrc)
                except IndexError:
                    os_system = "can't detect"
                network = {"ip": element[1].psrc, "mac": element[1].hwsrc, "os": os_system}
                network_list.append(network)
        return network_list

    @staticmethod
    def _standard_printing_network(network_list, mode):
        """Displaying network addresses depending on the selected option"""
        subprocess.run("clear")
        print("-" * 70)
        if mode == 1:
            print("IP\t\t\tMAC")
            for element in network_list:
                print(element["ip"] + "\t\t" + element["mac"])
        else:
            print("IP\t\t\tMAC\t\t\tSYSTEM")
            for element in network_list:
                print(element["ip"] + "\t\t" + element["mac"] + "\t" + element["os"])
        print("-" * 70)

    def _manual_network(self):
        """Manual option"""
        subprocess.run("clear")
        self.language_set.manual_network()

        while True:
            option = input("-> ")

            if option == str(1):
                self.language_set.manual_select_option1()
                break
            elif option == str(2):
                self.range = "16"
                break
            elif option == str(3):
                self.range = "8"
                break
            else:
                self.language_set.manual_select_option_else()

        self.language_set.manual_system_id()

        while True:
            id_option = input("-> ")

            if id_option == str(1):
                self.id_system = 2
                break
            elif id_option == str(2):
                self.language_set.manual_system_id_standard()
                break
            else:
                self.language_set.manual_select_option_else()

        self._standard_printing_network(self.network_list(self.id_system), self.id_system)

    def _mode_select(self):
        """Mod in manual option"""
        subprocess.run("clear")
        self.language_set.mode_select()

        while True:
            option = input("-> ")

            if option == str(1):
                self._standard_printing_network(self.network_list(self.id_system), self.id_system)
                break
            elif option == str(2):
                self._manual_network()
                break
            elif option == "e":
                sys.exit()
            else:
                self.language_set.manual_select_option_else()

    def run(self):
        self.default_language = language.Language.choose_language()
        self._set_default_language(self.default_language)
        self._installation()

        self._mode_select()
