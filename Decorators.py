from functools import wraps
import time

def zeitmessung(func):
    @wraps(func)
    def wrapped_zeitmesser(*args, **kwargs):

        time1 = time.perf_counter()
        result = func(*args, **kwargs)
        time2 = time.perf_counter()
        time_sum = time2 - time1
        print(f'Die Funktion {func.__name__}{args} hat {time_sum:.6f} Sekunden gedauert')
        return result
    return wrapped_zeitmesser