import logging
from typing import Callable, Any
from functools import wraps

FORMAT = ("{asctime} - {levelname} - "
          "{name} - {funcName}: {msg}")

logging.basicConfig(level=logging.NOTSET,
                    format=FORMAT, style='{',
                    filename='s15t03.log', filemode='a')
logger = logging.getLogger(__name__)


def log_deco(func: Callable) -> Callable:

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        mess_args = 'args: None'
        mess_kwargs = 'kwargs: None'
        if args:
            mess_args = f"args: {','.join([str(arg) for arg in args])}"
        if kwargs:
            kw_string = ', '.join([f'{key}={arg}' for key, arg in kwargs.items()])
            mess_kwargs = f"kwargs: {kw_string}"
        message = f'function {func.__name__}; {mess_args}; {mess_kwargs}'
        logger.info(msg=message)
        return func(*args, **kwargs)
    return wrapper


if __name__ == '__main__':
    print('Not for separate use')
