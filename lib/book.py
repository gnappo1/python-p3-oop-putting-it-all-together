#!/usr/bin/env python3

class Book:
    def __init__(self, title):
        self.title = title
        self._page_count = 0
    
    def get_page_count(self):
        print(self._page_count)
        return self._page_count
    
    def set_page_count(self, count):
        if type(count) in (int, float):
            self._page_count = count
        else:
            print("page_count must be an integer")
            return "page_count must be an integer"
    
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    
    page_count = property(get_page_count, set_page_count,)

hp = Book("Harry Potter")
if __name__ == '__main__':
    import ipdb; ipdb.set_trace()