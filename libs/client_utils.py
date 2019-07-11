import time
from libs.errors import ToLongUserName, WrongResponseCodeLength, NoActionCode, WrongResponseCode
from libs.consts import RESPONSE, CODES_TUPLE, ACTION, TIME, USER, PRESENCE
import logging
import log.client_log_config
from log.decorators import LoggerDeco

# Getting logger object for client
logger = logging.getLogger('client')


@LoggerDeco(logger)
def create_presence_message(account='Guest'):
    if isinstance(account, str):
        if len(account) > 25:
            raise ToLongUserName(account)
        else:
            presence_message = {
                ACTION: PRESENCE,
                TIME: time.time(),
                USER:
                    {
                        'account_name': account
                    }
            }
            return presence_message
    else:
        raise TypeError


@LoggerDeco(logger)
def read_presence_message(message):
    if RESPONSE not in message:
        raise NoActionCode
    response_code = message[RESPONSE]
    if len(str(response_code)) != 3:
        raise WrongResponseCodeLength()
    if response_code not in CODES_TUPLE:
        raise WrongResponseCode
    print(f'Response = {message}, status = connected')
