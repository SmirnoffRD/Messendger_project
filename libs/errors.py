# Project exceptions


class WrongResponseCode(Exception):
    """
    Extra exception class for wrong code
    """

    def __str__(self):
        return f'Code not in available codes'


class WrongResponseCodeLength(Exception):
    """
    Extra exception class for wrong code length
    """

    def __str__(self):
        return f'Wrong code length not equal 3'


class ToLongUserName(Exception):
    """
    Extra exception class for too long username
    """
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return 'Username is too long'


class NoActionCode(Exception):
    """
    Error raise while no action code in message
    """
    def __str__(self):
        return 'No action code error'
