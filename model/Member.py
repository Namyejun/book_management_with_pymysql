class Member():
    field = ["id", "name", "phone_number('-' 없이 입력)", "address"]

    def __init__(self, *args):
        self.id = args[0]
        self.__name = args[1]
        self.__phone_num = args[2]
        self.__addr = args[3]

    def __str__(self):
        return f"{self.id}\t{self.__name[:1] + '*'*len(self.__name[1:-1]) + self.__name[-1:]}"
    