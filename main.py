from lexico import Lexico
from sintatic import Sintatic
from semantic import Semantic


def main():
    token = Lexico('lalg.txt')
    semantic = Semantic()
    sintatic = Sintatic()
    sintatic.configFistAndFollow()
    sintatic.chargeTable()
    stack = []
    while True:
        a = (token.splitTokens())
        if a:
            sintatic.validateExpression(a)
            stack.append(a)
        else:
            break
    language = semantic.createLanguages(stack)
    print(language)


if __name__ == '__main__':
    main()
