# 2023-cs-609
#optionla task no#2 udp heartbeats 
import time
import socket
port = 12000
server_address = ('127.0.0.1', port)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(server_address)
clients = {}

print("Server is ready to receive heartbeats")

while True:
    message, address = server_socket.recvfrom(1024)
    current_time = time.time()
    message = message.decode()
    seq_num, timestamp = message.split()
    seq_num = int(seq_num)
    timestamp = float(timestamp)
    time_diff = current_time - timestamp
    if address in clients:
        last_seq_num, last_timestamp = clients[address]
        if seq_num != last_seq_num + 1:
            print(f"Packet loss detected from {address}. Expected {last_seq_num + 1}, got {seq_num}")
    else:
        print(f"New client detected: {address}")
    clients[address] = (seq_num, current_time)
    print(f"Received heartbeat from {address}: seq_num={seq_num}, time_diff={time_diff:.6f} seconds")