
class TxtProcessor:
    def __init__(self, txt_file="text.txt"):
        self.sentences = 0
        self.words = 0
        self.characters = 0
        try:
            with open(txt_file, "r") as file:
                for line in file:
                    self.file = line.strip()
                    self.sentences += self.count_sent()
                    self.words += self.count_word()
                    self.characters += self.count_char()
        except FileNotFoundError:
            raise FileNotFoundError

    def count_sent(self):
        return self.file.count(".")

    def count_word(self):
        __list = self.file.split()
        print(__list)
        return len(__list)

    def count_char(self):
        print(self.file)
        return len(self.file)

    # print(f'Sentences - {len(txt_proc.count_sent())}')
    # print(f'Words - {len(txt_proc.count_word())}')
    # print(f'Chars - {len(txt_proc.count_char())}')