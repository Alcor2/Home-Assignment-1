import time
import contextlib
import io

def time_decorator(fcn):

    def timer(*args):
        timer.cnt += 1
        start = time.perf_counter()

        with contextlib.redirect_stdout(io.StringIO()) as f:
            fcn(*args)
        end = time.perf_counter()
        
        print(fcn.__name__, ' call ', timer.cnt, ' executed in ', end - start, ' sec')
    
    timer.cnt = 0
    
    return timer
