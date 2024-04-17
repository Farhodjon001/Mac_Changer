#!/usr/bin/env python3

import subprocess
import optparse
import re
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its Mac adress")
    parser.add_option("-m", "--mac", dest="new_mac", help="New Mac adress")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Iltimos interfaceni kirirting ma'lumot uchun --help kiriting")
    elif not options.new_mac:
        parser.error("[-] Iltimos new mac ni kirirting ma'lumot uchun --help kiriting")
    return options

def change_mac(interface, new_mac):
    print("[+] Changing Mac address for " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_adress_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_adress_search_result:
        return mac_adress_search_result.group(0)
    else:
        print("[-] Could not read Mac address.")


options = get_arguments()

current_mac = get_current_mac(options.interface)
print("Current Mac = " + str(current_mac))

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] Mac adress was successfully changed to " + current_mac)
else:
    print("[-] Mac address did not get changed")

# interface = "eth0"
# new_mac = "00:00:11:33:44:66"

# interface = raw_input("interface >")  #faqat python2 versiyasida ishlaydi
# new_mac = raw_input("new Mac >")

# interface = input("interface >")  # bular esa python va python3 versiyasida ishlaydi
# new_mac = input("new Mac >")

# interface = options.interface
# new_mac = options.new_mac


# subprocess.call("ifconfig eth0 down", shell=True)
# subprocess.call("ifconfig eth0 hw ether 00:11:22:22:33:44", shell=True)
# subprocess.call("ifconfig eth0 up", shell=True)

# subprocess.call("ifconfig " + interface + " down", shell=True)
# subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
# subprocess.call("ifconfig " + interface + " up", shell=True)

git config --global user.email "shermuhammadfarhod@gmail.com"
git
config - -
global user.name
"Your Name"
git
config - -
global user.name
"Your Name"
