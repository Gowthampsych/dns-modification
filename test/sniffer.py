# import pyshark

# def packet_callback(pkt):
#     if 'DNS' in pkt:
#         print("DNS Packet Captured:")
#         print("Source IP:", pkt.ip.src)
#         print("Destination IP:", pkt.ip.dst)
#         print("Query:", pkt.dns.qry_name)

# # Capture loopback traffic
# capture = pyshark.LiveCapture(interface='Adapter for loopback traffic capture', bpf_filter='udp port 53')


# # Start capturing packets
# print("Capturing DNS packets on loopback interface. Press Ctrl+C to stop...")
# try:
#     for packet in capture.sniff_continuously(packet_count=10):  # Capture 10 packets
#         packet_callback(packet)
# except KeyboardInterrupt:
#     print("Capture stopped by user.")

# # Close the capture when done
# capture.close()




# import pyshark
# import time
# import csv

# def packet_callback(pkt, ip_count):
#     if 'DNS' in pkt:
#         ip = pkt.ip.src
#         if ip not in ip_count:
#             ip_count[ip] = 0
#         ip_count[ip] += 1

# def capture_dns_packets(duration):
#     ip_count = {}
#     start_time = time.time()
#     capture = pyshark.LiveCapture(interface='Adapter for loopback traffic capture', bpf_filter='udp port 53')

#     print("Capturing DNS packets on loopback interface. Press Ctrl+C to stop...")
#     try:
#         while time.time() - start_time < duration:
#             capture.apply_on_packets(lambda pkt: packet_callback(pkt, ip_count))
#             time.sleep(2)  # Capture packets for every 2 seconds
#     except KeyboardInterrupt:
#         print("Capture stopped by user.")

#     capture.close()
#     return ip_count

# def generate_csv(ip_count):
#     with open('continuous_ips.csv', mode='w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(['IP', 'Count'])
#         for ip, count in ip_count.items():
#             if count >= duration / 2:  # If the IP appeared continuously for at least half the duration
#                 writer.writerow([ip, count])

# if __name__ == "__main__":
#     duration = 60  # Capture duration in seconds
#     ip_count = capture_dns_packets(duration)
#     generate_csv(ip_count)
#     print("CSV file generated.")





# import pyshark
# import time
# import csv

# def packet_callback(pkt, ip_count):
#     if 'DNS' in pkt:
#         print("Incoming Source IP:", pkt.ip.src)
#         print("Destination IP:", pkt.ip.dst)
#         print("Query:", pkt.dns.qry_name)
        
#         ip = pkt.ip.src
#         if ip not in ip_count:
#             ip_count[ip] = 0
#         ip_count[ip] += 1

# def capture_dns_packets(duration):
#     ip_count = {}
#     start_time = time.time()
#     capture = pyshark.LiveCapture(interface='Adapter for loopback traffic capture', bpf_filter='udp port 53')

#     print("Capturing DNS packets on loopback interface. Press Ctrl+C to stop...")
#     try:
#         while time.time() - start_time < duration:
#             capture.apply_on_packets(lambda pkt: packet_callback(pkt, ip_count))
#             time.sleep(2)  # Capture packets for every 2 seconds
#     except KeyboardInterrupt:
#         print("Capture stopped by user.")

#     capture.close()
#     return ip_count

# def generate_csv(ip_count):
#     with open('continuous_ips.csv', mode='w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(['IP', 'Count'])
#         for ip, count in ip_count.items():
#             if count >= duration / 2:  # If the IP appeared continuously for at least half the duration
#                 writer.writerow([ip, count])

# if __name__ == "__main__":
#     duration = 60  # Capture duration in seconds
#     ip_count = capture_dns_packets(duration)
#     generate_csv(ip_count)
#     print("CSV file generated.")



import pyshark
import time
import csv

def packet_callback(pkt, ip_count):
    """
    Callback function to process each captured packet.
    
    Args:
        pkt: The packet object captured by PyShark.
        ip_count: Dictionary to store IP addresses and their counts.
    """
    if 'DNS' in pkt:
        ip = pkt.ip.src
        if ip not in ip_count:
            ip_count[ip] = {'count': 0, 'last_seen': time.time()}
        else:
            if time.time() - ip_count[ip]['last_seen'] <= 2:  # Check if the IP was seen within 2 seconds
                ip_count[ip]['count'] += 1
            else:
                ip_count[ip]['count'] = 0
            ip_count[ip]['last_seen'] = time.time()

        # Print live updates
        print("Incoming Source IP:", pkt.ip.src)
        print("Destination IP:", pkt.ip.dst)
        print("Query:", pkt.dns.qry_name)
        print()

def capture_dns_packets(duration, ip_count):
    """
    Function to capture DNS packets continuously for a specified duration.

    Args:
        duration: The duration of the capture in seconds.
        ip_count: Dictionary to store IP addresses and their counts.
    """
    start_time = time.time()
    capture = pyshark.LiveCapture(interface='Adapter for loopback traffic capture', bpf_filter='udp port 53')

    print("Capturing DNS packets on loopback interface for", duration, "seconds. Press Ctrl+C to stop...")
    try:
        packet_count = 0
        while True:
            for packet in capture.sniff_continuously(packet_count=10):
                packet_callback(packet, ip_count)
                packet_count += 1
                if time.time() - start_time >= duration:
                    break
            if time.time() - start_time >= duration:
                break
    except KeyboardInterrupt:
        print("Capture stopped by user.")

    capture.close()

def generate_csv(ip_count):
    """
    Function to generate a CSV file with IP addresses and their counts.

    Args:
        ip_count: Dictionary containing IP addresses and their counts.
    """
    with open('fastflex_ips.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['IP'])
        for ip, data in ip_count.items():
            writer.writerow([ip])

def main(duration):
    """
    Main function to control the capture and CSV generation process.

    Args:
        duration: The duration of the capture in seconds.
    """
    ip_count = {}
    capture_dns_packets(duration, ip_count)
    generate_csv(ip_count)

if __name__ == "__main__":
    duration = 20  # Capture duration in seconds
    main(duration)




