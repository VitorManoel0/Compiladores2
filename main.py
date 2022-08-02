from lexico import Lexico


def main():
    token = Lexico('lalg.txt')
    for i in range(10):
        print(token.splitTokens())



if __name__ == '__main__':
    main()
