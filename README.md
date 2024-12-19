# MAC Address Changer

A Python script to change the MAC address of a specified network interface. This can be used for privacy, testing, or bypassing network restrictions.

## Features
- Retrieves the current MAC address of the specified interface.
- Changes the MAC address to a user-defined value.
- Verifies the MAC address change.

## Requirements
- Python 3.x
- Administrative privileges (root access).
- `ifconfig` command available on the system.

## Installation
1. Clone the repository:
   git clone https://github.com/SainiJapneet/mac-address-changer.git
   cd mac-address-changer

2. Ensure Python is installed:
   python3 --version

## Usage
1. Run the script with the required options:
   sudo python3 mac_changer.py -i <interface> -m <new_mac>
   Replace `<interface>` with the network interface (e.g., `eth0`, `wlan0`) and `<new_mac>` with the desired MAC address (e.g., `00:11:22:33:44:55`).

2. Example:
   sudo python3 mac_changer.py -i wlan0 -m 00:11:22:33:44:55

## Options
- `-i` or `--interface`: Specify the network interface.
- `-m` or `--mac`: Specify the new MAC address.

## Example Output
## Example Output
Current MAC of wlan0 interface is 12:34:56:78:9a:bc
[+] Changing MAC address for wlan0 to 00:11:22:33:44:55 ...
[+] MAC has been changed successfully from 12:34:56:78:9a:bc to 00:11:22:33:44:55

## Notes
- Run the script with `sudo` or as a root user to modify network configurations.
- Ensure the `ifconfig` command is installed on your system. Install it using:
   sudo apt-get install net-tools

## License
This project is licensed under the MIT License.

## Disclaimer
Use this tool responsibly and ensure you comply with local laws and regulations.

