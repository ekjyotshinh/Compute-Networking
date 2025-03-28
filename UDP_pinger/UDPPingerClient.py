# Ekjyot Shinh
import time
from socket import *

# Define server address and port
serverName = 'localhost'  # localhost as the server
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Set timeout for socket to 1 second
clientSocket.settimeout(1)

# Send 10 pings to the server
for seq_num in range(1, 11):
    # Record the send time
    send_time = time.time()
    message = f"ping {seq_num}"
    
    try:
        # Send the ping message to the server
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        
        # Wait for a response from the server
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        
        # Record the receive time
        receive_time = time.time()
        
        # Calculate the round-trip time (RTT)
        rtt = receive_time - send_time
        
        # Print the response and RTT
        print(f"Reply from {serverAddress}: {modifiedMessage.decode()}")
        print(f"Calculated RTT = {rtt:.6f} seconds")
    
    except timeout:
        # If no response is received within 1 second, the request times out
        print(f"Request timed out for Ping {seq_num}")
    
    # Wait for a short time before sending the next ping
    time.sleep(1)

# Close the socket after all pings are sent
clientSocket.close()
