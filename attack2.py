from scapy.all import *
import threading
import time
import csv

# Function to read IPs from CSV file
def read_ips_from_csv(filename):
    ips = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header
        for row in csv_reader:
            ips.append(row[0])  # Assuming IP addresses are in the first column
    return ips

# Function to send DNS response packets using the list of IPs repeatedly
def send_dns_requests(source_ips):
    while True:
        for src_ip in source_ips:
            target_ip = "127.0.0.1"  # Use the fixed target IP address
            print("Target ip", target_ip)
            print(f"Generated IP that is attacking: {src_ip}")  # Print generated IP
            dns_request = IP(src=src_ip, dst=target_ip) / UDP() / DNS(rd=1, qd=DNSQR(qname="example.com"))
            #send(dns_request, verbose=False) 
            time.sleep(1)  # Adjust the frequency of requests as needed

# Start sending DNS request packets in a separate thread
def main():
    source_ips = read_ips_from_csv('download.csv')
    dns_thread = threading.Thread(target=send_dns_requests, args=(source_ips,))
    dns_thread.start()

    # Keep the program running
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()
