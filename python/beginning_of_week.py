"""
The problem: You have a time series in Pandas or whatever, indexed by datetime 
objects. For any date in the time series, you want to find the date of the 
beginning of the week that it is in (Monday in the case of Python) or the end 
of the week that it is in (Sunday in the case of python).

You may use datetime module where necessary.

As you are going to TDD the solution, I've only stubbed one function, but you 
will be creating two in total. The tests will guide you as to the functions 
needed, types expected and returned.

>>> week_start_date(datetime(2016,1,28))
datetime.datetime(2016, 1, 25, 0, 0)
>>> week_start_date(datetime(2016,2,29))
datetime.datetime(2016, 2, 29, 0, 0)
>>> week_end_date(datetime(1957,12,25))
datetime.datetime(1957, 12, 29, 0, 0)

"""
from datetime import datetime, timedelta

def week_start_date(dt):
    return dt - timedelta(days=dt.weekday())

def week_end_date(dt):
    return dt + timedelta(days=(6-dt.weekday()))


if __name__ == '__main__':
   import doctest
   doctest.testmod()

