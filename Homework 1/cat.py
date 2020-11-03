class Cat:
    def __init__(self, name):
        self.name = name

    def greet(self, otherCat):
        print(f"Hello I am {self.name}! I see you are also a cool fluffy kitty {otherCat.name}, let's together purr at the human so they shall give us food.")