# Minimal Evidence Checklist (Simplified)

- [ ] VirtualBox/UTM screenshot with attacker VM and target VM and network setting (host-only/internal).
- [ ] nmap_ping_*.txt (host discovery) + terminal screenshot.
- [ ] nmap_quick_tcp_*.txt (TCP SYN + -sV) + terminal screenshot.
- [ ] nmap_udp_*.txt (UDP targeted) + note about open|filtered.
- [ ] Service banner outputs (HTTP page screenshot, SSH banner text).
- [ ] Wireshark packet capture screenshot (showing SYN/ACK).
- [ ] Metasploit console banner screenshot and exploit session screenshot (lab-only).
- [ ] Snapshot restore screenshot showing cleanup.
- [ ] OWASP ZAP scan screenshot (if web app used) + one request/response evidence.
- [ ] Python scripts included and screenshots showing they ran.
