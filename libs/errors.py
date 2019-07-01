from libs.consts import CODES_TUPLE
# Project exceptions
class WrongResponseCode(Exception):
    """
    Extra exception class for wrong code
    """
    def __init__(self, code):

        self.code = code

    def __str__(self):
        return f'Code {self.code} not in available codes {CODES_TUPLE}'


class WrongResponseCodeLength(Exception):
    """
    Extra exception class for wrong code length
    """
    def __init__(self, code):
        self.code = str(code)

    def __str__(self):
        return f'Wrong code length ({len(self.code)}), not equal 3'


class ToLongUserName(Exception):
    """
    Extra exception class for too long username
    """
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return f'{self.username.capitalize} is too long'

class NoActionCode(Exception):
    """
    Error raise while no action code in message
    """
    def __str__(self):
        return 'No action code error'
