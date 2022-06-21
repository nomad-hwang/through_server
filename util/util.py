import copy

def replace_params(default: dict, **kwargs):
    params = copy.deepcopy(default)
    params.update((key, kwargs[key]) for key in set(kwargs).intersection(default))
    return params