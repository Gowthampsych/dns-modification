# import csv
# import subprocess
# import time

# blocked_ips = set()

# def block_ip(ip_address):
#     result = subprocess.run(['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name="BlockIP"', 'dir=in', 'action=block', f'remoteip={ip_address}'], capture_output=True, text=True)
#     if result.returncode == 0:
#         blocked_ips.add(ip_address)
#         print(f"Successfully blocked IP: {ip_address}")
#     else:
#         print(f"Failed to block IP: {ip_address}")
#         print("Error:", result.stderr)

# def is_ip_blocked(ip_address):
#     return ip_address in blocked_ips

# def log_event(event):
#     with open('event_log.txt', 'a') as file:
#         file.write(f"{event}\n")

# def monitor_traffic():
#     while True:
#         # Implement your traffic monitoring logic here
#         # For demonstration purposes, let's assume we receive a query from a blocked IP
#         blocked_ip = '192.168.1.100'  # Example blocked IP
#         query = "GET /example HTTP/1.1"  # Example query
#         if is_ip_blocked(blocked_ip):
#             log_event(f"Blocked IP {blocked_ip} attempted to send query: {query}")
#             # Optionally, you can block the IP again if desired:
#             # block_ip(blocked_ip)
#         time.sleep(5)  # Adjust the sleep interval based on your monitoring needs

# # Read IPs from CSV file and block each one
# def block_ips_from_csv(csv_file):
#     with open(csv_file, 'r') as file:
#         reader = csv.reader(file)
#         next(reader)  # Skip header if present
#         for row in reader:
#             ip_address = row[0].strip()  # Assuming IPs are in the first column
#             block_ip(ip_address)

# csv_file_path = 'fastflex_ips.csv'
# block_ips_from_csv(csv_file_path)
# monitor_traffic()



import csv
import subprocess

# Function to read IP addresses from CSV file
def read_blocked_ips_from_csv(file_path):
    blocked_ips = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            blocked_ips.append(row[0].strip())
    return blocked_ips

# Function to block IP addresses using netsh command
def block_ip_with_netsh(ip):
    command = f"netsh advfirewall firewall add rule name='Block_IP_{ip}' dir=in action=block remoteip={ip}"
    subprocess.run(command, shell=True, check=True)

# Function to drop packets from IP addresses using netsh command
def drop_packets_from_ip(ip):
    command = f"netsh advfirewall firewall add rule name='Drop_Packets_{ip}' dir=in action=block remoteip={ip} enable=yes"
    subprocess.run(command, shell=True, check=True)

# Main function
def main():
    # Path to the CSV file containing IP addresses to block
    csv_file_path = "fastflex_ips.csv"
    
    # Read IP addresses from CSV file
    blocked_ips = read_blocked_ips_from_csv(csv_file_path)
    
    # Drop packets from each IP address
    for ip in blocked_ips:
        try:
            drop_packets_from_ip(ip)
            print(f"Dropped packets from IP: {ip}")
        except Exception as e:
            print(f"Failed to drop packets from IP {ip}: {e}")

if __name__ == "__main__":
    main()
