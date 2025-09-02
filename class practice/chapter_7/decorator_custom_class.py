
class Custom_class:
    def __call__(self, *args, **kwds):
        print("Custom_class instance was called!")
        print("Positional args:", args)
        print("Keyword args:", kwds)
        

custom_1 = Custom_class()

custom_1(10, 20, 44, 55, name="Uluru", lang="Python")