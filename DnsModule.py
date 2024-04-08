import csv
import subprocess

def block_ip(ip):
    try:
        subprocess.run(['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name="BlockedIP"', 'dir=in', 'action=block', f'remoteip={ip}/32'], check=True)
        print(f"Blocked IP: {ip}")
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to execute command. Return code: {e.returncode}. Output: {e.output}")
    except Exception as e:
        print(f"Failed to block IP {ip}: {e}")

def main():
    csv_file = 'download.csv'

    try:
        with open(csv_file, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip header if exists
            for row in csv_reader:
                ip = row[0].strip()  # Assuming IP is in the first column
                block_ip(ip)
    except FileNotFoundError:
        print(f"File '{csv_file}' not found.")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()

