def splitManual(line, caracter):
    lineSplited = []
    word = ''
    for letter in line:
        if letter != caracter and letter != '\n' and letter != '\t':
            word += letter
        else:
            lineSplited.append(word)
            word = ''
    if word != '':
        lineSplited.append(word)
    return lineSplited


def reservedWord(word):
    reserved = ['program', 'real', 'integer', 'begin', 'write', 'end', 'read']
    if word in reserved:
        return 'reserved', word
    else:
        return 'ident', word


class Lexico:
    def __init__(self, arq):
        with open(arq, 'r') as f:
            self.text = f.read()
        self.index = 0
        self.word = ''

    def splitTokens(self):
        while True:
            try:
                letter = self.text[self.index]
            except IndexError:
                return None

            # Remove comments
            if letter == '{':
                while self.text[self.index] != '}':
                    self.deallocateFromString(self.index)
                self.deallocateFromString(self.index)
            elif letter == '/' and self.text[self.index + 1] == '*':
                self.deallocateFromString(self.index)
                self.deallocateFromString(self.index)
                while True:
                    if self.text[self.index] == '*' and self.text[self.index + 1] == '/':
                        self.deallocateFromString(self.index)
                        self.deallocateFromString(self.index)
                        break
                    else:
                        self.deallocateFromString(self.index)

            # Return symbols
            elif letter in ':=/*-+;.,()':
                if self.word != '':
                    a = self.word
                    self.word = ''
                    return reservedWord(a)
                elif letter == ':' and self.text[self.index + 1] == '=':
                    self.index += 2
                    return 'symbol', ':='
                elif letter == '*':
                    self.index += 1
                    return 'symbol', '*'
                elif letter == '/':
                    self.index += 1
                    return 'symbol', '/'
                elif letter == '+':
                    self.index += 1
                    return 'symbol', '+'
                elif letter == '-':
                    self.index += 1
                    return 'symbol', '-'
                elif letter == ':':
                    self.index += 1
                    return 'symbol', ':'
                elif letter == ';':
                    self.index += 1
                    return 'symbol', ';'
                elif letter == '.':
                    self.index += 1
                    return 'symbol', '.'
                elif letter == ',':
                    self.index += 1
                    return 'symbol', ','
                elif letter == '(':
                    self.index += 1
                    return 'symbol', '('
                elif letter == ')':
                    self.index += 1
                    return 'symbol', ')'

            else:
                if letter != ' ' and letter != '' and letter != '\n' and letter != '\t':
                    self.index += 1
                    self.word += letter
                else:
                    if self.word != '' and self.word != ' ':
                        if letter == '\n' or letter == '\t':
                            self.deallocateFromString(self.index)
                        a = self.word
                        self.word = ''
                        return reservedWord(a)
                    else:
                        self.index += 1

    def deallocateFromString(self, index):
        a = []
        b = ''
        for i in self.text:
            a.append(i)
        a.pop(index)
        for i in a:
            b += i
        self.text = b
