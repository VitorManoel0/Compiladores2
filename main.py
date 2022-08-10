from lexico import Lexico
from sintatic import Sintatic
from semantic import Semantic
from interpreter import Interpreter


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
    # print(language)
    interpreter = Interpreter()
    interpreter.readLanguages()

if __name__ == '__main__':
    main()
