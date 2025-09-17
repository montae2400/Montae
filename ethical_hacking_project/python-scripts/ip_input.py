# ip_input.py
"""Prompt for an IP and validate basic IPv4 format."""
import re

def is_basic_ipv4_format(ip_address: str) -> bool:
    pattern = r'^\d{1,3}(\.\d{1,3}){3}$'
    return bool(re.match(pattern, ip_address))

def main():
    user_input_ip = input("Enter a target IP (lab only): ").strip()
    if is_basic_ipv4_format(user_input_ip):
        print(f"You entered IP: {user_input_ip}")
    else:
        print("That doesn't look like a valid IPv4 address.")

if __name__ == '__main__':
    main()
