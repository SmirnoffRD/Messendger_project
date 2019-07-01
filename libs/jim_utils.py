import json
from libs.consts import ENCODING


def send_message(sock, message):
    """
    Sending message as json as bytes object
    :param sock: socket object
    :param message: message as dict object
    """
    if isinstance(message, dict):
        message_json = json.dumps(message)
        sock.send(message_json.encode(ENCODING))
    else:
        raise TypeError


def get_message(sock):
    """
    Getting and decoding message
    :param sock: socket object
    :return: dict object message
    """
    message_b = sock.recv(1024)
    if isinstance(message_b, bytes):
        message_json = message_b.decode(ENCODING)
        return json.loads(message_json)
    else:
        raise TypeError
