#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand):
        self.brand = brand
        self._size = None
    
    def get_size(self):
        print(self._size)
        return self._size
    
    def set_size(self, size):
        if type(size) in (int, float) and 0 <= size <= 100:
            self._size = size
        else:
            print("size must be an integer")
    
    def cobble(self):
        self.condition = "New" if hasattr(self, "condition") else "You must set an initial condition first!"
        print("Your shoe is as good as new!")
    
    size = property(get_size, set_size)

stan_smith = Shoe("Adidas")
if __name__ == '__main__':
    import ipdb; ipdb.set_trace()
stan_smith.size = 11