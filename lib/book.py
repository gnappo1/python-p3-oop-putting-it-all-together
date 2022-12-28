#!/usr/bin/env python3
# Using attribute as decorator

class Book:
    def __init__(self, title):
        self.title = title
        self._page_count = 0
    
    @property
    def page_count(self):
        print(self._page_count)
        return self._page_count
    
    @page_count.setter
    def page_count(self, count):
        if type(count) in (int, float):
            self._page_count = count
        else:
            print("page_count must be an integer")
            return "page_count must be an integer"
    
    @page_count.deleter
    def page_count(self):
        del self._page_count

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    
    # page_count = property(get_page_count, set_page_count,)

hp = Book("Harry Potter")
if __name__ == '__main__':
    import ipdb; ipdb.set_trace()