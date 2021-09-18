import time
import contextlib
import io
import inspect
from inspect import signature

class class_decorator:
    global cnt
    cnt = 0
    global times
    times = [['PROGRAM', 'TIME ELAPSED', ' | RANK | ', '']]

    def __init__(self, fcn):
        self.fcn = fcn
    
    def __call__(self, *args):

        def timer(*args):
            global cnt
            cnt += 1
            timer.cnt += 1

            with contextlib.redirect_stdout(io.StringIO()) as f:
                out = [['Name:', self.fcn.__name__], ['Type:', type(self.fcn)], ['Sign:', signature(self.fcn)], ['Args:', tuple([*args])], 
                    ['Doc:', inspect.getdoc(self.fcn)], ['Source:', inspect.getsource(self.fcn)], ['Output:', self.fcn(*args)]]
            
            with open("Downloads\Report.txt", "a") as s:
                start = time.perf_counter()

                with contextlib.redirect_stdout(io.StringIO()) as f:
                    self.fcn(*args)
                end = time.perf_counter()

                s.write(self.fcn.__name__ + ' call ' + str(timer.cnt) + ' executed in ' + str(end - start) + ' sec\n')
                
                # Writes down the function's execution time into a .txt file

                times.append([self.fcn.__name__, end - start, cnt, 's'])
                
                if cnt >= 4:     # Ranking of the functions and the table creation
                    pts = []

                    for i in range(len(times)):
                        f_n = 0
                        max = 0
                        pt = 0
                        for j in range(1, len(times)):     # Execution time ranking
                            if max < times[j][1] and j not in pts:
                                max = times[j][1]
                                pt = j
                        
                        for j in range(len(times)):     # Function's name length ranking
                            if f_n < len(times[j][0]):
                                f_n = len(times[j][0])
                        
                        pts.append(pt)
                    
                    for i in range(len(times)):
                        if i == 0:
                            print(times[i][0], ' ' * (f_n - len(times[i][0])), ' ' * (int((len(times[0][2]) - len(times[i][2])) / 2) + 1), times[i][2],
                                ' ' * int((len(times[0][2]) - len(times[i][2])) / 2), times[i][1] + times[i][3])
                        
                        else:
                            print(times[pts[i - 1]][0], ' ' * (f_n - len(times[pts[i - 1]][0])), ' ' * (int((len(times[0][2]) - 1) / 2) + 1), times[i][2], 
                                ' ' * int((len(times[0][2]) - 1) / 2), str(times[pts[i - 1]][1]) + times[pts[i - 1]][3])

                for i in range(len(out)):
                    if type(out[i][1]) == str:
                        text = out[i][1].splitlines()     # Cuts a new piece from string as soon as it finds '\n' and then adds it into a list
                        for j in range(len(text)):
                            text[j] = text[j].strip()     # Deletes tabulation in string

                        for j in range(len(text)):     # Writes the function data into a .txt file
                            if j == 0:
                                s.write(out[i][0] + ' ' * (8 - len(out[i][0])) + text[j] + '\n')

                            else:
                                s.write(' ' * 8 + text[j] + '\n')

                    else:
                        s.write(out[i][0] + ' ' * (8 - len(out[i][0])) + str(out[i][1]) + '\n')
                
                s.close()
        
        timer.cnt = 0

        return timer(*args)
