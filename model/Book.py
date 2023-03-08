class Book():
    field = ["ISBN (-로 구분)", "name", "author", "genre", "price"]
    def __init__(self, *args):
        self.ISBN = args[0]
        self.name = args[1]
        self.author = args[2]
        self.genre = args[3]
        self.price = args[4]

    def __str__(self):
        return f"{self.ISBN}\t{self.name}\t{self.author}\t{self.genre}\t{self.price}"