class SomeClass:
    class_var: str = "foo"
    class_var_two: str = "bar"
    
    def __init__(self):
        self.something = SomeClass.class_var + SomeClass.class_var_two

if __name__ == "__main__":
    sc = SomeClass()
    sc.something = "foo_bar_changed"
    print(sc.something)
    print(sc.class_var)
    print(SomeClass.class_var)
    
    sc_two = SomeClass()
    print(sc_two.something)
    
    