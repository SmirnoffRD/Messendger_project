import socket
import sys
from libs.consts import *
from libs.jim_utils import get_message, send_message
from libs.server_utils import create_response_message


if __name__ == '__main__':
    '''
    Main client run script.
    Takes args from system start script.
    '''
    if '-ip' in sys.argv:
        try:
            host_ip = sys.argv[sys.argv.index('-ip') + 1]
        except IndexError:
            print('Run script with non-default args "server_run -ip IP -p PORT"')
            sys.exit(0)
    else:
        host_ip = IP
    if '-p' in sys.argv:
        try:
            host_port = int(sys.argv[sys.argv.index('-p') + 1])
        except IndexError:
            print('Run script with non-default args "server_run -ip IP -p PORT"')
            sys.exit(0)
    else:
        host_port = PORT

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host_ip, host_port))
    server_socket.listen(SERVER_CONNECTIONS)

    while True:
        client_socket, client_address = server_socket.accept()
        presence = get_message(client_socket)
        response = create_response_message(presence)
        send_message(client_socket, response)
        client_socket.close()
