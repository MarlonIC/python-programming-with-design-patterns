class Namer:
    def __init__(self):
        self.last = ''
        self.first = ''


class FirstFirst(Namer):
    def __init__(self, namestring: str):
        super().__init__()
        i = namestring.find(' ')
        if i > 0:
            names = namestring.split(' ')
            self.first = names[0]
            self.last = names[1]
        else:
            self.last = namestring


class LastFirst(Namer):
    def __init__(self, namestring: str):
        super().__init__()
        i = namestring.find(',')
        if i > 0:
            names = namestring.split(',')
            self.last = names[0].strip()
            self.first = names[1].strip()
        else:
            self.last = namestring


class NamerFactory:
    def __init__(self, namestring: str):
        self.name = namestring

    def getNamer(self):
        i = self.name.find(',')
        if i > 0:
            return LastFirst(self.name)
        else:
            return FirstFirst(self.name)


class Builder:
    def compute(self):
        name = ''
        while name != 'quit':
            name = input('Enter name: ')
            namerFact = NamerFactory(name)
            namer = namerFact.getNamer()
            print(namer.first, namer.last)


def main():
    bld = Builder()
    bld.compute()


if __name__ == '__main__':
    main()
