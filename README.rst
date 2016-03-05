=====       
Deterministic tools
=====

Deterministic tools is a very simple LRU implementation to a full-time cache
of function calls. Cache is stored over a dict stored on the decorator object. 
To use the cache, just use the deterministic decorator in the function. Note 
that as the cache system is very simple it is not thread safe, also there is
just a simple method to control memory usage that can not match your 
requirements, use it with caution.

Quick start. 

1. The deterministic decorator is stored on the deterministic package and can be
imported as follows:

    from deterministic import deterministic

2. The simple use is to decorate the function that must have the cache:

    @deterministic() def foo(): ...
    
* Note that the parethesis are required in this decorator.
    

3. If you want to limit the cache size, you can pass the maximum number of cache
register to the decorator, as:
    
    @deterministic(max_cache_size=10)
    def foo(bar): return bar.process()
