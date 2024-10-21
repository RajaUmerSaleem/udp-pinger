# 2023-cs-609
#optionla task no#2 udp heartbeats 
import time
import socket
port = 12000
server_address = ('127.0.0.1', port)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
seq_num = 0
print("Sending heartbeats to the server...")
try:
    while True:
        seq_num += 1
        message = f'{seq_num} {time.time()}'
        client_socket.sendto(message.encode(), server_address)
        time.sleep(1)
except KeyboardInterrupt:
    print("Client stopped")
finally:
    client_socket.close()