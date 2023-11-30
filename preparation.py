import socket
import os


with open(os.path.expanduser('~/.bashrc'), 'a') as bash_file:
    connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    connection.connect(('www.google.com', 443))
    ip, port = connection.getsockname()
    
    bash_file.write(f'export IP={ip}\n')
    connection.close()