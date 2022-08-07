from lexico import Lexico
from sintatic import Sintatic


def main():
    token = Lexico('lalg.txt')
    sintatic = Sintatic()
    sintatic.configFistAndFollow()
    sintatic.chargeTable()

    while True:
        a = (token.splitTokens())
        if a:
            sintatic.validateExpression(a)
        else:
            break


if __name__ == '__main__':
    main()
