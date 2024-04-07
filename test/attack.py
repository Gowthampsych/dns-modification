from scapy.all import *
import threading
import time
import random

# Function to send DNS response packets from a pool of source IP addresses
def send_dns_requests():
    source_ips = ["158.234.249.53", "197.89.210.72"]  # Modify with your desired source IPs

    while True:
        for src_ip in source_ips:
            target_ip = "192.168.29.1"  # Use the fixed target IP address
            print("Target IP:", target_ip)
            print("Source IP:", src_ip)
            dns_request = IP(src=src_ip, dst=target_ip) / UDP() / DNS(rd=1, qd=DNSQR(qname="example.com"))
            send(dns_request, verbose=False)  # Send the packet
            time.sleep(1)  # Adjust the frequency of requests as needed

# Start sending DNS request packets in a separate thread
dns_thread = threading.Thread(target=send_dns_requests)
dns_thread.start()

# Keep the program running
while True:
    time.sleep(1)
