from lexico import Lexico


def main():
    token = Lexico('lalg.txt')
    a = 1
    while True:
        a = (token.splitTokens())
        if a:
            print(a)
        else:
            break


if __name__ == '__main__':
    main()
