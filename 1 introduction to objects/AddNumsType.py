# not work polymorphism

class Summer:
    def add_nums_f(self, x: float, y: float) -> float:
        return x + y

    def add_nums(self, f: float, s: str) -> float:
        if type(s) is float:
            return self.add_nums_f(f, s)
        else:
            fsum = f + float(s)
            return fsum


def main():
    summer = Summer()
    print(summer.add_nums(12.0, 2.3))
    print(summer.add_nums(22.3, "13.5"))


if __name__ == '__main__':
    main()
