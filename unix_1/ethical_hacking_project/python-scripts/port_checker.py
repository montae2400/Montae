# port_checker.py
"""Simple TCP port check script (lab-only)."""
import socket
from typing import List

def check_tcp_port(target_ip: str, port_number: int, timeout_seconds: float = 1.0) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout_seconds)
        try:
            sock.connect((target_ip, port_number))
            return True
        except (socket.timeout, ConnectionRefusedError, OSError):
            return False

def parse_ports(port_list_string: str) -> List[int]:
    port_strings = [p.strip() for p in port_list_string.split(',') if p.strip()]
    return [int(p) for p in port_strings]

def main():
    target_ip = input("Enter target IP (lab only): ").strip()
    ports_input = input("Enter ports to check (comma-separated, e.g. 22,80): ").strip()
    ports_to_check = parse_ports(ports_input)
    for port in ports_to_check:
        is_open = check_tcp_port(target_ip, port)
        status = 'OPEN' if is_open else 'CLOSED'
        print(f"PORT {port}: {status} on {target_ip}")

if __name__ == '__main__':
    main()
