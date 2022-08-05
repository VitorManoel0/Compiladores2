from lexico import splitManual


def clearString(string):
    word = ''
    for count, i in enumerate(string):
        if i == '[':
            for j in string[count + 1::]:
                if j != ']':
                    word += j

            return word


class Sintatic:
    def __init__(self):
        self.firstFollow = {'FIRST': {}, 'FOLLOW': {}}
        self.lines = []
        self.grammar = {}
        self.table = {}
        self.symbols = [':=', '/', '*', '-', '+', ';', '.', '(', ')']
        self.reservedWord = ['program', 'real', 'integer', 'begin', 'write', 'end', 'ident', 'read', 'numero_int', 'numero_real']
        self.expression = ''
        self.stack = ['program']

    def configFistAndFollow(self):
        with open('firstfollow.txt', 'r') as f:
            for line in f:
                line = splitManual(line, ' ')

                if 'FIRST' in line[0]:
                    if line[0] not in self.firstFollow['FIRST'].keys():
                        self.firstFollow['FIRST'][clearString(line[0])] = []
                    for i in line[2::]:
                        self.firstFollow['FIRST'][clearString(line[0])].append(i)

                elif 'FOLLOW' in line[0]:
                    if line[0] not in self.firstFollow['FOLLOW'].keys():
                        self.firstFollow['FOLLOW'][clearString(line[0])] = []
                    for i in line[2::]:
                        self.firstFollow['FOLLOW'][clearString(line[0])].append(i)

    def chargeTable(self):
        with open('lalg-rules.txt', 'r') as f:
            for line in f:
                line = splitManual(line, ' ')

                self.createIndex(line[0])

                if line[2] in self.reservedWord or line[2] in self.symbols:
                    self.table[line[0]][line[2]] = line

                elif line[2] == '&':
                    for j in self.firstFollow['FOLLOW'][line[0]]:
                        if line[0] not in self.table[line[0]].keys():
                            self.table[line[0]][j] = line

                else:
                    for i in self.firstFollow['FIRST'][line[0]]:
                        if i == '&':
                            for j in self.firstFollow['FOLLOW'][line[0]]:
                                if line[0] not in self.table[line[0]].keys():
                                    self.table[line[0]][j] = line
                        else:
                            self.table[line[0]][i] = line

        print(self.table)

    def createIndex(self, name):
        if name not in self.table.keys():
            self.table[name] = {}

    # def validateExpression(self, expression):
    #     while True:
    #         if self.stack:
    #             break
    #         if expression[1] == self.stack[-1]:
    #             self.stack.pop()
    #             break
    #         for i in self.table[self.stack[-1]][expression[-1]][2::]:
    #             self.stack.append(i)
    #
    #     print(self.stack)
