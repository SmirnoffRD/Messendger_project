import socket
import sys
import select
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
    server_socket.settimeout(0.2)

    clients = []

    while True:
        try:
            client_socket, client_address = server_socket.accept()
            presence = get_message(client_socket)
            response = create_response_message(presence)
            send_message(client_socket, response)
        except OSError as e:
            pass
        else:
            print(f"Client {client_address} connected")
            clients.append(client_socket)
        finally:
            r = []
            w = []
            try:
                r, w, e = select.select(clients, clients, [], 10)
            except:
                pass
            messages = []
            for client_r in r:
                try:
                    messages.append(client_r.recv(1024).decode('UTF-8'))
                except:
                    clients.remove(client_r)
            if messages:
                for client_w in w:
                    for mess in messages:
                        try:
                            client_w.send(mess.encode('UTF-8'))
                        except:
                            clients.remove(client_w)
