import time
import contextlib
import io
import textwrap
import inspect
from inspect import signature

def dump_decorator(fcn):

    def timer(*args):
        timer.cnt += 1
        start = time.perf_counter()

        with contextlib.redirect_stdout(io.StringIO()) as f:
            fcn(*args)
        end = time.perf_counter()
        
        print(fcn.__name__, ' call ', timer.cnt, ' executed in ', end - start, ' sec')
        
        with contextlib.redirect_stdout(io.StringIO()) as f:
            out = [['Name:', fcn.__name__], ['Type:', type(fcn)], ['Sign:', signature(fcn)], ['Args:', tuple([*args])], ['Doc:', inspect.getdoc(fcn)], 
                ['Source:', inspect.getsource(fcn)], ['Output:', fcn(*args)]]
        
        for i in range(len(out)):
            if type(out[i][1]) == str:
                text = out[i][1].splitlines()     # Cuts a new piece from string as soon as it finds '\n' and then adds it into a list
                for j in range(len(text)):
                    text[j] = text[j].strip()     #Deletes tabulation in string
                
                for j in range(len(text)):
                    if j == 0:
                        print(out[i][0], ' ' * (7 - len(out[i][0])), text[j])

                    else:
                        print(' ' * 8, text[j])
            
            else:
                print(out[i][0], ' ' * (7 - len(out[i][0])), out[i][1])
    
    timer.cnt = 0
    
    return timer