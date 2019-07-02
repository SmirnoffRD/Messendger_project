import sys, socket
from libs.consts import PORT
from libs.client_utils import create_presence_message, read_presence_message
from libs.jim_utils import get_message, send_message


if __name__ == '__main__':
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

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, server_port))
    presence = create_presence_message()
    send_message(client, presence)
    presence_answer = get_message(client)
    read_presence_message(presence_answer)
    client.close()