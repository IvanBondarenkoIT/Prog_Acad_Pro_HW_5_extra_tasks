
class TxtProcessor:
    def __init__(self, txt_file="text.txt"):
        try:
            with open(txt_file, "r") as file:
                self.file = file.readlines()
        except FileNotFoundError:
            raise FileNotFoundError

    def count_ch(self):
        return self.file[0].split()
