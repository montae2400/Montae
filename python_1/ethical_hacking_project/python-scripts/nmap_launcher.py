# nmap_launcher.py
"""Run a simple nmap ping scan and save output (lab-only)."""
import subprocess, datetime

def run_nmap_ping_scan(network_range: str, output_filename: str) -> int:
    cmd = ["nmap", "-sn", network_range]
    with open(output_filename, "w") as outfile:
        result = subprocess.run(cmd, stdout=outfile, stderr=subprocess.STDOUT, text=True)
    return result.returncode

def main():
    network_range = input("Enter network range (e.g. 192.168.56.0/24): ").strip()
    ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    output_file = f"nmap_ping_{ts}.txt"
    print(f"Running nmap -sn {network_range} ... output -> {output_file}")
    rc = run_nmap_ping_scan(network_range, output_file)
    print("Done. Return code:", rc)

if __name__ == '__main__':
    main()
