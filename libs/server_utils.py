from libs.consts import ACTION, PRESENCE, TIME, RESPONSE, ERROR


def create_response_message(client_presence_message):
    if client_presence_message[ACTION] == PRESENCE and \
                    TIME in client_presence_message:
        if isinstance(client_presence_message[TIME], float):
            return {RESPONSE: 200}
        else:
            raise TypeError
    else:
        return {RESPONSE: 400, ERROR: 'Не верный запрос'}