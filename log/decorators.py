from functools import wraps


class LoggerDeco:

    def __init__(self, logger):
        self.logger = logger

    def __call__(self, func):

        @wraps(func)
        def decorated(*args, **kwargs):
            message = 'Function {} called from {} '.format(decorated.__name__, decorated.__module__)
            result = func(*args, **kwargs)
            if args:
                message += f'args: {args},'
            if kwargs:
                message += f'kwargs: {kwargs},'
            if result:
                message += f'result: {result}'
            self.logger.info(message)
            return result

        return decorated
