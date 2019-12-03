from MyPy import io as io

class Tasbih:

    def __init__(self):
        self.get_args()

    @staticmethod
    def name():
        return('Tasbih')

    def get_args(self):
        print('Besmeh. Please enter the number: ', end='')
        c = input()
        self.__N = int(c) 
        self.__ctr = 0

    def start(self):
        io.cls()
        print('**********************')
        while True:
            c = io.getch()
            if c.capitalize() == 'E':
                break
            self.__ctr += 1
            print('\r', self.__ctr, end='')
            if self.__ctr == self.__N:
                break
        print('\r**********************')
