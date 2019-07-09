from libs.consts import ACTION, PRESENCE, TIME, RESPONSE, ERROR
import logging
import log.server_log_config

#Getting logger object for server
logger = logging.getLogger('server')

def create_response_message(client_presence_message):
    if client_presence_message[ACTION] == PRESENCE and \
                    TIME in client_presence_message:
        if isinstance(client_presence_message[TIME], float):
            res = 'response: {}'.format({RESPONSE: 200})
            logger.info('{} - {} - {}'.format(res, create_response_message.__name__, __name__))
            return {RESPONSE: 200}
        else:
            raise TypeError
    else:
        return {RESPONSE: 400, ERROR: 'Не верный запрос'}
