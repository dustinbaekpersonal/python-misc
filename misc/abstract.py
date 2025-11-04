from abc import ABC, abstractmethod

class Foo(ABC):
    def __init__(self, foo: int, foo2: int):
        self.foo = foo
        self.foo2 = foo2
    

    @abstractmethod
    def print_foo(self, num: int):
        # print(self.foo + num)
        ...

class Bar(Foo):
    def __init__(self, bar):
        super().__init__(bar, bar)
    
    def print_foo(self, hello):
        print(self.foo + hello)

if __name__ == "__main__":
    bar = Bar(30) 

    bar.print_foo(20)