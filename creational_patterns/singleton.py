class Singleton(type):
    __instances = dict()

    def __call__(cls, *args, **kwargs):
        if not cls.__instances:
            cls.__instances[cls] = super().__call__(*args, **kwargs)
        return cls.__instances[cls]


class GoogleCeo(metaclass=Singleton):
    pass


if __name__ == "__main__":
    ceo1, ceo2 = GoogleCeo(), GoogleCeo()
    print(id(ceo1), id(ceo2))
