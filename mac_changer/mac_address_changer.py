#!/usr/bin/env
import subprocess
import optparse


# optparse is used to take cmd line arguments from user and parse them.

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface whose MAC is to be changed")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address for the specified interface")
    if not options.interface:
        parser.error("[-] Please specify an interface. Use --help for more information.")
    elif not options.new_mac:
        parser.error("[-] Please specify a MAC address. Use --help for more information.")
    return options


def execute_shell_cmd(cmd):
    subprocess.call(cmd, shell=False)


def read_cmd_output(cmd):
    return subprocess.check_output(cmd)


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac + " ...")

    # To avoid command injection, sanitize user inout we can make use of list which takes each word as an element of list
    # user will not be able to enter new commands
    execute_shell_cmd(["ifconfig", interface, "down"])
    execute_shell_cmd(["ifconfig", interface, "hw", "ether", new_mac])
    execute_shell_cmd(["ifconfig", interface, "up"])


options = get_arguments()
change_mac(interface=options.interface, new_mac=options.new_mac)
