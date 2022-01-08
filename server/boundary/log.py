import typing as ty


def try_except(message: str, default: ty.Any) -> ty.Any:
    def wrapper(function) -> ty.Any:
        def wrapped(*args, **kwargs) -> ty.Any:
            try:
                return function(*args, **kwargs)
            except Exception as e:
                print(e, message)
                return default

        return wrapped
    return wrapper
