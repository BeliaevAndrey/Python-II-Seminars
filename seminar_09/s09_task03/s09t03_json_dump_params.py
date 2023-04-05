import json
import os
from typing import Callable, Any


def dump_to_json_dec(file_name: str) -> Callable:
    def inner_dec(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> Any:
            if os.path.exists(file_name) and os.path.getsize('testfile.json') > 0:
                with open(file_name, 'r', encoding='utf-8') as f_in:
                    parameters = json.load(f_in)
                parameters.append({})
            else:
                parameters = [{'args': {}, 'kwargs': {}, 'result': None}]
            if args:
                parameters[-1]['args'] = {f'arg{i}': args[i] for i in range(len(args))}
            if kwargs:
                parameters[-1]['kwargs'] = kwargs
            result = func(*args, **kwargs)
            parameters[-1]['result'] = result
            with open(file_name, 'w', encoding='utf-8') as f_out:
                json.dump(parameters, f_out, indent=4)
            return result
        return wrapper
    return inner_dec


if __name__ == '__main__':
    print('Not for separate use')

