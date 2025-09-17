# Nmap Cheat Sheet (Beginner)

**Host discovery**
nmap -sn 192.168.56.0/24 -oN nmap_ping.txt

**Quick TCP (top ports)**
nmap -sS -sV 192.168.56.101 -oN nmap_quick_tcp.txt

**Port range (1-1000)**
sudo nmap -sS -p 1-1000 -sV 192.168.56.101 -oN nmap_1-1000.txt

**UDP targeted**
sudo nmap -sU -p 53,67,69,123 192.168.56.101 -oN nmap_udp.txt

**OS & service detection**
sudo nmap -O -sV 192.168.56.101 -oN nmap_os_service.txt

**Aggressive (lab-only)**
sudo nmap -A -T4 -p1-2000 192.168.56.101 -oN nmap_aggressive.txt

**NSE examples**
nmap -p 80 --script http-title,http-headers 192.168.56.101 -oN nmap_http_info.txt
nmap -p 22,21 --script banner 192.168.56.101 -oN nmap_banners.txt
nmap --script ssl-cert -p 443 192.168.56.101 -oN nmap_sslcert.txt

**Output formats**
-oN human.txt  (human readable)
-oX machine.xml (XML)
-oG grepable.txt (grepable)

**Short tips**
- Use sudo for better results.
- Start with -sn then -sS -sV.
- Save raw outputs and take screenshots for evidence.
