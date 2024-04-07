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
        for packet in capture.sniff_continuously(packet_count=10):
            packet_callback(packet, ip_count)
            packet_count += 1
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
