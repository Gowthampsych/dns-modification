from scapy.all import *
import threading
import time

# Explicitly provide source IP addresses for the attack
source_ips = ["158.234.249.53", "197.89.210.72"]  # Modify with your desired source IPs

# Function to send DNS response packets using the list of IPs repeatedly
def send_dns_requests():
    while True:
        for src_ip in source_ips:
            target_ip = "127.0.0.1"  # Use the fixed target IP address
            print("Target ip", target_ip)
            print(f"Generated IP that is attacking: {src_ip}")  # Print generated IP
            dns_request = IP(src=src_ip, dst=target_ip) / UDP() / DNS(rd=1, qd=DNSQR(qname="example.com"))
            send(dns_request, verbose=False)  # Send the packet
            time.sleep(1)  # Adjust the frequency of requests as needed

# Start sending DNS request packets in a separate thread
dns_thread = threading.Thread(target=send_dns_requests)
dns_thread.start()

# Keep the program running
while True:
    time.sleep(1)


