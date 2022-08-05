from lexico import Lexico
from sintatic import Sintatic


def main():
    token = Lexico('lalg.txt')
    # while True:
    #     a = (token.splitTokens())
    #     if a:
    #         print(a)
    #     else:
    #         break

    sintatic = Sintatic()
    sintatic.configFistAndFollow()
    sintatic.chargeTable()


if __name__ == '__main__':
    main()
