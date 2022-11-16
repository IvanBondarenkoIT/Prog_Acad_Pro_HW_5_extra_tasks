
class TxtProcessor:
    def __init__(self, txt_file="text.txt"):
        try:
            with open(txt_file, "r") as file:
                self.file = file.readlines()
        except FileNotFoundError:
            raise FileNotFoundError

    def count_sent(self):
        __list = []
        for i in self.file:
            __list = i.split(".")
        try:
            __list.remove('\n')
        except ValueError:
            pass
        return __list

    def count_word(self):
        __list = []
        for i in self.file:
            __list = i.split()
        try:
            __list.remove('\n')
        except ValueError:
            pass
        return __list

    def count_char(self):
        __list = []
        for i in self.file:
            __list = i.split()
        try:
            __list.remove('\n')
        except ValueError:
            pass
        return "".join(__list)
