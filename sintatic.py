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
        self.reservedWord = ['program', 'real', 'integer', 'begin', 'write', 'end', 'ident', 'read']

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
                if line[0] not in self.table.keys():
                    self.table[line[0]] = {}

                if line[2] in self.reservedWord or line[2] in self.symbols:
                    self.table[line[0]][line[2]] = line

                if line[2] == '&':
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
