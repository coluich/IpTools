# /==================================================================================\
# ||                                                                                ||
# ||   ___________     _____  ___  _     _____ _   _ _      ___ _____ ___________   ||
# ||  |_   _| ___ \   /  __ \/ _ \| |   /  __ | | | | |    / _ |_   _|  _  | ___ \  ||
# ||    | | | |_/ /   | /  \/ /_\ | |   | /  \| | | | |   / /_\ \| | | | | | |_/ /  ||
# ||    | | |  __/    | |   |  _  | |   | |   | | | | |   |  _  || | | | |      /   ||
# ||   _| |_| |       | \__/| | | | |___| \__/| |_| | |___| | | || | \ \_/ | |\ \   ||
# ||   \___/\_|        \____\_| |_\_____/\____/\___/\_____\_| |_/\_/  \___/\_| \_|  ||
# ||                                                                                ||
# \==================================================================================/

import IPCalculator
import prettytable
from dns_resolver import resolve
import time
import os
import sys

# version 1.0.0
version = "1.0.0"


############ FUNCTIONS ############

# pulisce la console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
clear_console()

# stampa con effetto macchina da scrivere
def printa(text, delay=0.0005):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
banner = """
/==================================================================================\\
||                                                                                ||
||   ___________     _____  ___  _     _____ _   _ _      ___ _____ ___________   ||
||  |_   _| ___ \\   /  __ \\/ _ \\| |   /  __ | | | | |    / _ |_   _|  _  | ___ \\  ||
||    | | | |_/ /   | /  \\/ /_\\ | |   | /  \\| | | | |   / /_\\ \\| | | | | | |_/ /  ||
||    | | |  __/    | |   |  _  | |   | |   | | | | |   |  _  || | | | |      /   ||
||   _| |_| |       | \\__/| | | | |___| \\__/| |_| | |___| | | || | \\ \\_/ | |\\ \\   ||
||   \\___/\\_|        \\____\\_| |_\\_____/\\____/\\___/\\_____\\_| |_/\\_/  \\___/\\_| \\_|  ||
||                                                                                ||
\\==================================================================================/
"""
printa(banner)
printa("Welcome to the IP Calculator", 0.01)
printa("o(*￣▽￣*)ブ", 0.01)
print()


def ip_ask(asd=None):
    if asd==True or asd==None:
        printa("Enter the IP address and CIDR (<IP>/<CIDR>)", 0.01)
        printa("Example: 192.168.178.0/24", 0.01)
        printa("For help, type 'help'", 0.01)
    return input("(IP) -> ")

def main(bho=None):
    try:
        input_ip = ip_ask(bho)

        ############ COMMANDS ############
        if input_ip == "exit":
            printa("Goodbye! (´▽`ʃ♡ƪ)", 0.01)
            time.sleep(2)
            exit()
        if input_ip == "help":
            printa("Enter the IP address and CIDR (<IP>/<CIDR>)", 0.0005)
            printa("Or enter the following commands:", 0.0005)
            table = prettytable.PrettyTable()
            table.field_names = ["Command", "Description"]
            table.align["Description"] = "l"
            table.add_row(["about", "About this program"])
            table.add_row(["clear", "Clear the console"])
            table.add_row(["exit", "Exit the program"])
            table.add_row(["help", "Show this help message"])
            table.add_row(["version", "Show the version"])
            table.add_row(["logo", "Show the logo"])
            table.add_row(["ping <hostname>", "Ping a hostname"])
            table.add_row(["nslookup <hostname>", "Resolve a hostname"])
            table.add_row(["tracert <hostname>", "Trace the route to a hostname"])

            print(table)
            main(False)
            return
        if input_ip == "about":
            print("This is a simple IP Calculator made by @coluich")
            main(False)
            return
        if input_ip == "clear" or input_ip == "cls":
            clear_console()
            main(False)
            return
        if input_ip == "version":
            print("Version " + version)
            main(False)
            return
        if input_ip == "logo" or input_ip == "banner" or input_ip == "ascii":
            clear_console()
            printa(banner, 0.0001)
            main(False)
            return
        try:
            if input_ip.split(" ")[0] == "ping":
                hostname = input_ip.split(" ")[1]
                param = '-n' if os.sys.platform.lower()=='win32' else '-c'
                response = os.system(f"ping {param} 1 {hostname} >nul 2>&1")
                if response == 0:
                    print(hostname, 'is up!')
                else:
                    print(hostname, 'is down!')
                main(False)
                return
            if input_ip.split(" ")[0] == "nslookup":
                hostname = input_ip.split(" ")[1]
                # response = os.popen(f"nslookup {hostname}").read()
                response = resolve(hostname)
                try:
                    print("ipV4: " + response[0]) 
                except Exception as e:
                    print("impossible to resolve the ipV4")
                try:
                    print("ipV6: " + response[1])
                except:
                    print("impossible to resolve the ipV6")
                main(False)
                return
            if input_ip.split(" ")[0] == "tracert":
                hostname = input_ip.split(" ")[1]
                response = os.system(f"tracert {hostname}")
                print(response)
                main(False)
                return
        except: pass
        
        ############ ERRORS ############
        if input_ip == "":
            main(False)
            return
        if input_ip == " ":
            print("(IP) -> ")
            main(False)
            return
        if "/" not in input_ip or input_ip.count("/") > 1:
            print("Please enter a valid IP address ( ˘︹˘ )")
            main(False)
            return

        ############ PROGRAMM ############     
        ip = input_ip.split("/")[0]
        cidr = int(input_ip.split("/")[1])
        if cidr > 32 or cidr < 0:
            print("Please enter a valid CIDR value （︶^︶）")
            main(False)
            return
        if len(ip.split(".")) != 4:
            print("Please enter a valid IP address ( ˘︹˘ )")
            main(False)
            return
        for i in ip.split("."):
            if not (int(i) >= 0 and int(i) <=255):
                print("Please enter a valid IP address ￣へ￣")
                exit() 
    except Exception as e:
        print("Please enter a valid IP address (* ￣︿￣)")
        # print(e)
        exit()

    ip_calculator = IPCalculator.IPCalculator(ip, cidr)

    print()
    table = prettytable.PrettyTable()
    table.field_names = ["Property", "Value"]
    table.align["Value"] = "l"
    table.add_row(["IP Address", f"{ip_calculator.ip}/{ip_calculator.cidr}"])
    table.add_row(["Network Address", ip_calculator.network_address])
    table.add_row(["Net-ID  bit", ip_calculator.cidr])
    table.add_row(["Host-IP bit", 32 - ip_calculator.cidr])
    table.add_row(["Total Hosts", 2**(32 - ip_calculator.cidr) - 2])
    table.add_row(["Class", ip_calculator.get_ip_type()+"/"+ip_calculator.classe()])
    table.add_row(["Broadcast Address", ip_calculator.broadcast_address])
    table.add_row(["NetMask", ip_calculator.subnet_mask])
    table.add_row(["Wildcard Mask", ip_calculator.wildcard_mask])
    table.add_row(["Host Range", ip_calculator.host_range[0] + " - " + ip_calculator.host_range[1]])
    print(table)

    main(False)
if __name__ == "__main__":
    main()