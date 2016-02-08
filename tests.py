import unittest
from deterministic import deterministic
import time

class FunctionsTests(unittest.TestCase):
    
    def test_standalonefunction(self):
        @deterministic()
        def foo(a):
            time.sleep(1)
        for i in range(1, 100):
            foo(i%10)
        self.assertTrue(True)
            
    def test_returningfunction(self):
        @deterministic()
        def foo(a):
            time.sleep(1)
            return a
        for i in range(1, 100):
            self.assertEquals(i%10, foo(i%10))
            
    def test_classmethods(self):
        class foo:
            def __init__(self, id):
                self.id = id
                
            @deterministic()
            def bar(self):
                time.sleep(1)
                return self.id
        
        foos = [foo(i) for i in range(1, 10)]
        
        for i in range(1, 100):
            for f in foos:
                self.assertEquals(f.id, f.bar())
                
    def test_maxcachesize(self):
        @deterministic(max_cache_size=11)
        def foo(a):
            time.sleep(1)
        for i in range(1, 100):
            foo(i%10)
        self.assertTrue(True)
if __name__ == '__main__':
    unittest.main() 
