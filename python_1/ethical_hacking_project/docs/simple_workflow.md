# Simple Workflow (what to run & when)

1. Host discovery:
   nmap -sn 192.168.56.0/24 -oN nmap_ping_YYYYMMDD.txt
2. Pick a live host and run service scan:
   sudo nmap -sS -sV -p1-1000 192.168.56.101 -oN nmap_target_service_YYYYMMDD.txt
3. Targeted UDP (if needed):
   sudo nmap -sU -p 53,123 192.168.56.101 -oN nmap_udp_quick.txt
4. NSE checks for web services:
   nmap -p 80 --script http-title,http-headers 192.168.56.101 -oN nmap_http_info.txt
5. Use Wireshark to capture a short trace during one scan for packet evidence.
