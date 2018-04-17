
import time
from functools import wraps


def timeit(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start_time = time.time()

        func_return = func(*args, **kwargs)

        end_time = time.time()

        elapsed_time = end_time - start_time
        print('{} is working for {:0.30f}'.format(func.__name__, elapsed_time))
        return func_return
    return inner


def cancel_decorator(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print(func.__name__, 'is cancelled')
    return inner


class Count(object):

    instances = {}

    @staticmethod
    def count_func(func):
        def counter_wrap(*args, **kwargs):
            if func.__name__ in Count.instances.keys():
                Count.instances[func.__name__] += 1
            else:
                Count.instances[func.__name__] = 1
            print('\n{} is called {} times'.format(func.__name__, Count.instances[func.__name__]))
            return func(*args, **kwargs)
        return counter_wrap

def logging(func):
    print('Decorator for {} function is working'.format(func))
    @wraps(func)
    def inner(*args, **kwargs):
        print('1.\"{}\" started'.format(func.__name__))
        func_return = func(*args, **kwargs)
        print('2.\'{}\' stopped'.format(func.__name__))
        return func_return
    return inner


def canceller(func):
    @wraps(func)
    def catcher_wrap(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return 'Exception \'{}\' occured while running \'{}\''.format(e, func.__name__)
    return catcher_wrap


def printing(text):
    print('Some text: {}'.format(text))


@Count.count_func
# @cancel_decorator
@timeit
@logging
def short(text):
    import time
    time.sleep(1)
    print('Short text: ', text)
    return 'short'



short('Ok')
short('Ok')
short('Ok')
short('Ok')


'''
nums = [1, 4, 5, 30, 99]
print(list(map(lambda x: x % 5, nums)))

nums2 = [3, 4, 90, -2]
print(list(map(str, nums2)))

nums3 = ['some', 1, 'v', 40, '3a', str]
print(list(filter(lambda s: isinstance(s, int), nums3)))

nums4 = ['some', 'other', 'value']
print(reduce(lambda a,b: a + b, list(len(x) for x in nums4)))

nums5 = ['some', 'other', 'value']
print(list(len(x) for x in nums5))
'''

