def get_value(obj, path):
    keys = path.split('/')
    current = obj

    for key in keys:
        if isinstance(current, dict):
            if key not in current:
                raise KeyError(f'Key "{key}" is not found in the dictionary')
            current = current[key]
        else:
            raise TypeError(f'Not an object/dictionary that can be accessed with key - "{key}" on type {type(current)}')
    return current
         