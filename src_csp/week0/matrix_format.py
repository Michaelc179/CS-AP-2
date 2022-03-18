from src_csp.util.option import Option


class MatrixFormat(Option):
    def __init__(self):
        super().__init__()
        self.name = "Matrix Format"
        self.numpad = [[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9],
                       [" ", 0, " "]]

    def tester(self):
        for i in self.numpad:
            for j in i:
                print(j, "", end="")
            print()
