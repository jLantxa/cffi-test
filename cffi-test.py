import sys

from klass import Klass

if __name__ == "__main__":
    number = int(sys.argv[1])
    klass = Klass(number)

    klass.SayHello()
    print(klass.Square(number))
