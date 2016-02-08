""" deterministic package provides tools for very simple LRU cache strategies.
"""
from collections import OrderedDict

class deterministic(object):
    """ deterministic decorator class to handle the calls to the function. 
        The cache is a very simple collections.OrderedDict that holds the last
        calls args (keys) and results (values).
        The valid options are:
        ::int max_cache_size The max length o the cache dict. Default is None,
            what means that the length is unlimited.
    """
    def __init__(self, max_cache_size=None):
        self.max_cache_size = max_cache_size
        self.__cache = OrderedDict([])
        
    def __call__(self, f):
        def wrapper(*args, **kwargs): 
            results = self.__cache
            if self.max_cache_size and len(results) >= self.max_cache_size:
                del results[results.keys()[0]]
            key = (tuple(args), tuple(kwargs)) 
            if not key in results.keys():
                result = f(*args, **kwargs)
                results[key] = result
                return result
            return results[key]
        return wrapper

