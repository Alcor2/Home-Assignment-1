from task1 import time_decorator
from task2 import dump_decorator
from task3 import class_decorator
from task4 import error_decorator

def power(nmb, pwr):
    '''
    This function raises 'nmb' to the power of 'pwr'.
    
    Keyword arguments:
    nmb -- a list of numbers to be raised to the power given;
    pwr -- a list of numbers to be used as power of nmb elements.
    '''

    ans = lambda nmb, pwr: [nmb ** pwr for nmb, pwr in zip(nmb, pwr)]
    return ans(nmb, pwr)

def mltp_strings(string, number):
    '''
    This function multiplicates strings.

    Keyword arguments:
    string -- a list of strings to be copied;
    number -- a list of numbers to copy the string elements given number of times.
    '''

    res = lambda string, number: [string * number for string, number in zip(string, number)]
    return res(string, number)

def qdr_eq(a, b, c):
    '''
    This function solves quadratic equations only with real solutions.
    
    Keyword arguments:
    a -- the quadratic equation coefficient near x^2;
    b -- the quadratic equation coefficient near x^1;
    c -- the quadratic equation coefficient near x^0.
    '''

    D = b ** 2 - 4 * a * c
    ans = []
    if D == 0:
        ans.append(-b / (2 * a))
    
    elif D > 0:
        ans.append((-b + D ** 0.5) / (2 * a))
        ans.append((-b - D ** 0.5) / (2 * a))
    
    else:
        ans.append('The equation has imaginary solutions!')
    
    return ans

def pscl_trgl(n):
    '''
    This function prints Pascal Triangle till nth row.
    
    Keyword arguments:
    n -- number of rows of Pascal Triangle to be typed.
    '''

    top = [1]
    app = [0]
    for i in range(n):
        print(top)
        top = [l + r for l, r in zip(app + top, top + app)]

td_power = time_decorator(power)                   # Declaration of a new decorated with the time_decorator function 'power'
td_power.__doc__ = power.__doc__
td_mltp_strings = time_decorator(mltp_strings)     # Declaration of a new decorated with the time_decorator function 'mltp_strings'
td_mltp_strings.__doc__ = mltp_strings.__doc__
td_qdr_eq = time_decorator(qdr_eq)                 # Declaration of a new decorated with the time_decorator function 'qdr_eq'
td_qdr_eq.__doc__ = qdr_eq.__doc__
td_pscl_trgl = time_decorator(pscl_trgl)           # Declaration of a new decorated with the time_decorator function 'pscl_trgl'
td_pscl_trgl.__doc__ = pscl_trgl.__doc__

if __name__ == "__main__":
    td_pscl_trgl(9)
    td_qdr_eq(3, 2, 1)
    td_qdr_eq(4, 3, -2)
    td_pscl_trgl(5)
    td_power([2, 5], [3, 2])
    td_mltp_strings(['sf', 'a'], [3, 2])
    td_qdr_eq(3, 2, 1)
    print('\n')

dd_power = dump_decorator(power)                   # Declaration of a new decorated with the dump_decorator function 'power'
dd_power.__doc__ = power.__doc__
dd_mltp_strings = dump_decorator(mltp_strings)     # Declaration of a new decorated with the dump_decorator function 'mltp_strings'
dd_mltp_strings.__doc__ = mltp_strings.__doc__
dd_qdr_eq = dump_decorator(qdr_eq)                 # Declaration of a new decorated with the dump_decorator function 'qdr_eq'
dd_qdr_eq.__doc__ = qdr_eq.__doc__
dd_pscl_trgl = dump_decorator(pscl_trgl)           # Declaration of a new decorated with the dump_decorator function 'pscl_trgl'
dd_pscl_trgl.__doc__ = pscl_trgl.__doc__

if __name__ == "__main__":
    dd_qdr_eq(7, 1, 2)
    print('\n')

cd_power = class_decorator(power)                   # Declaration of a new decorated with the class_decorator function 'power'
cd_power.__doc__ = power.__doc__
cd_mltp_strings = class_decorator(mltp_strings)     # Declaration of a new decorated with the class_decorator function 'mltp_strings'
cd_mltp_strings.__doc__ = mltp_strings.__doc__
cd_qdr_eq = class_decorator(qdr_eq)                 # Declaration of a new decorated with the class_decorator function 'qdr_eq'
cd_qdr_eq.__doc__ = qdr_eq.__doc__
cd_pscl_trgl = class_decorator(pscl_trgl)           # Declaration of a new decorated with the class_decorator function 'pscl_trgl'
cd_pscl_trgl.__doc__ = pscl_trgl.__doc__

if __name__ == "__main__":
    cd_qdr_eq.__call__(7, 1, 2)
    cd_power.__call__([2, 3], [4, 5])
    cd_mltp_strings.__call__(['dhf', 'sjd', 'x'], [3, 2, 5])
    cd_pscl_trgl.__call__(7)
    print('\n')

ed_power = error_decorator(power)                   # Declaration of a new decorated with the error_decorator function 'power'
ed_power.__doc__ = power.__doc__
ed_mltp_strings = error_decorator(mltp_strings)     # Declaration of a new decorated with the error_decorator function 'mltp_strings'
ed_mltp_strings.__doc__ = mltp_strings.__doc__
ed_qdr_eq = error_decorator(qdr_eq)                 # Declaration of a new decorated with the error_decorator function 'qdr_eq'
ed_qdr_eq.__doc__ = qdr_eq.__doc__
ed_pscl_trgl = error_decorator(pscl_trgl)           # Declaration of a new decorated with the error_decorator function 'pscl_trgl'
ed_pscl_trgl.__doc__ = pscl_trgl.__doc__

if __name__ == "__main__":
    ed_pscl_trgl('l')
    ed_qdr_eq(7, 1, 2)
