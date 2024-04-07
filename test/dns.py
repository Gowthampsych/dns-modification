
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
