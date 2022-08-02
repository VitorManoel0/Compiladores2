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


class Lexico:
    def __init__(self, arq):
        with open(arq, 'r') as f:
            self.text = f.read()

    def splitTokens(self):
        for count, letter in enumerate(self.text):
            if letter == '{':
                while self.text[count] != '}':
                    self.deallocateFromString(count)
                self.deallocateFromString(count)
            elif letter == '/' and self.text[count+1] == '*':
                self.deallocateFromString(count)
                self.deallocateFromString(count)
                while True:
                    if self.text[count] == '*' and self.text[count+1] == '/':
                        self.deallocateFromString(count)
                        self.deallocateFromString(count)
                        break
                    else:
                        self.deallocateFromString(count)
            elif letter == '*':
                self.deallocateFromString(count)
                return 'op_mul', '*'
            elif letter == '/':
                self.deallocateFromString(count)
                return 'op_mul', '/'
            elif letter == '+':
                self.deallocateFromString(count)
                return 'op_ad', '+'
            elif letter == '-':
                self.deallocateFromString(count)
                return 'op_ad', '-'

    def deallocateFromString(self, index):
        a = []
        b = ''
        for i in self.text:
            a.append(i)
        a.pop(index)
        for i in a:
            b += i
        self.text = b
