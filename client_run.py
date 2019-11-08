import socket
import sys
import threading

from libs.client_utils import create_presence_message, read_presence_message
from libs.consts import PORT
from libs.jim_utils import get_message, send_message


def read_mess(server):
    while True:
        message = server.recv(1024).decode("UTF-8")
        print(f'Message: {message}\n')


if __name__ == '__main__':
    '''
    Main client run script.
    Takes args from system start script.
    '''
    r = False
    w = False
    if '-ip' in sys.argv:
        try:
            server_ip = sys.argv[sys.argv.index('-ip') + 1]
        except IndexError:
            print('Run script with non-default args "client_run -ip IP -p PORT"')
            sys.exit(0)
    else:
        server_ip = 'localhost'
    if '-p' in sys.argv:
        try:
            server_port = int(sys.argv[sys.argv.index('-p') + 1])
        except IndexError:
            print('Run script with non-default args "client_run -ip IP -p PORT"')
            sys.exit(0)
    else:
        server_port = PORT
    if 'r' in sys.argv:
        r = True
    if 'w' in sys.argv:
        w = True

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, server_port))
    presence = create_presence_message()
    send_message(client, presence)
    presence_answer = get_message(client)
    read_presence_message(presence_answer)
    reading_thread = threading.Thread(target=read_mess, args=(client,))
    reading_thread.start()
    while True:
        mess = input('Input your message: ')
        client.send(mess.encode('UTF-8'))
