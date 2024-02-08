import socket
import os


with open(os.path.expanduser('./.env'), 'w+') as env_file:
    connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    connection.connect(('www.google.com', 443))
    ip, _ = connection.getsockname()
    
    env_file.write(f'IP={ip}\n')
    connection.close()