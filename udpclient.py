# 2023-cs-609
#UDP pinger client 
import time
import socket
server_address = ('localhost', 12000)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(1)
rtts = []
lost_packets = 0
for i in range(1, 11):
    message = f'Ping {i} {time.time()}'
    
    try:
        start_time = time.time()
        client_socket.sendto(message.encode(), server_address)
        response, _ = client_socket.recvfrom(1024)
        end_time = time.time()
        rtt = end_time - start_time
        rtts.append(rtt)
        print(f'Received from server: {response.decode()}')
        print(f'RTT: {rtt:.6f} seconds')
    
    except socket.timeout:
        lost_packets += 1
        print('Request timed out')
client_socket.close()

# for optional task#1
if rtts:
    min_rtt = min(rtts)
    max_rtt = max(rtts)
    avg_rtt = sum(rtts) / len(rtts)
else:
    min_rtt = max_rtt = avg_rtt = 0

packet_loss_rate = (lost_packets / 10) * 100

# Print statistics
print(f'\n Optional task#1')
print(f'10 packets transmitted, {10 - lost_packets} packets received, {packet_loss_rate}% packet loss')
print(f'RTT min = {min_rtt:.6f}seconds')
print(f'RTT max = {max_rtt:.6f}seconds')
print(f'RTT avg = {avg_rtt:.6f}seconds')
