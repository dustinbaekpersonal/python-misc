from with_property import AboutMe

class MoreAboutMe(AboutMe):
    def __init__(self, something: str):
        self.something = something
        self.__company: str = "AnywhereButDeloitte"
        # need to supercharge to use inherited attributes and methods.
        super().__init__()

    @property
    def programming(self) -> list[str]:
        """Overwrite programming property."""
        return self._programming

    @programming.setter
    def programming(self, value):
        if not isinstance(value, str):
            raise ValueError(f"Give me a string!!!")
    

class AnotherAboutMe(MoreAboutMe):
    def __init__(self):
        super().__init__("asdf")
        self.hello = "hello"
    
    def hey(self):
        return "hi"

class TheOtherAboutMe(AnotherAboutMe):
    def __init__(self):
        pass
    

if __name__ == "__main__":
    asdf = MoreAboutMe("asdf")
    print(asdf._AboutMe__company)
    print(asdf)
    
    print(asdf.programming)
    # This raises ValueError newly defined in MoreAboutMe class.
    asdf.programming = 100
    print(asdf.programming)

    asdfasdf = AnotherAboutMe()
    print(asdfasdf.something)
    print(asdfasdf._workspace)
    
    # use of double underscore for attribute name.
    print(asdfasdf._AboutMe__company)
    print(asdfasdf._MoreAboutMe__company)
    
    print(asdfasdf.hey())
    
    asdfasdfasdf = TheOtherAboutMe()
    # method can still be used by inheritance.
    print(asdfasdfasdf.hey())
    # attributes can only be used by super()
    print(asdfasdfasdf.hello)
