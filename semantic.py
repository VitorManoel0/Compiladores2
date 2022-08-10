class Semantic:
    def __init__(self):
        self.stack = []
        self.C = []
        self.loc = 0
        self.input = ''
        self.reservedWord = ['program', 'real', 'integer', 'begin', 'write', 'end', 'ident', 'read', 'numero_int',
                             'numero_real']
        self.adress = -1
        self.tableSymbol = {}

    def createLanguages(self, stack):
        self.input = stack
        self.programa()
        for i in self.C:
            print(i)

    def CRCT(self, k):
        """
        :param k: element

        Carrega constante k no topo da pilha D
        """
        self.stack.append(k)

    def CRVL(self, n):
        """
        :param n: endereço

        Carrega valor de endereço n no topo da pilha D
        """

        self.stack.append(self.stack[n])

    def SOMA(self):
        """
        Soma o elemento antecessor com o topo da pilha; desempilha os dois e empilha o resultado
        """
        a = self.stack.pop(-1)
        b = self.stack.pop(-1)
        self.stack.append(a + b)

    def SUBT(self):
        """
        Subtrai o antecessor pelo elemento do topo
        """
        a = self.stack.pop(-1)
        b = self.stack.pop(-1)
        self.stack.append(b - a)

    def MULT(self):
        """
        Multiplica elemento antecessor pelo elemento do topo
        """
        a = self.stack.pop(-1)
        b = self.stack.pop(-1)
        self.stack.append(b * a)

    def DIVI(self):
        """
        Divide o elemento antecessor pelo elemento do topo
        """
        a = self.stack.pop(-1)
        b = self.stack.pop(-1)
        self.stack.append(b / a)

    def INVE(self):
        """
        Inverte sinal do topo
        """
        a = self.stack.pop(-1)
        self.stack.append(-1 * a)

    def CONJ(self):
        """
        Conjunção de valores lógicos. F=0; V=1
        """
        a = self.stack.pop(-1)
        b = self.stack.pop(-1)
        self.stack.append(int(a == b))

    def DISJ(self):
        """
        Disjunção de valores lógicos
        """
        a = self.stack.pop(-1)
        b = self.stack.pop(-1)
        self.stack.append(int(a or b))

    def NEGA(self):
        """
        Negação lógica
        """
        a = self.stack.pop(-1)
        self.stack.append(-1 * a)

    def CPME(self):
        """
        Comparação de menor entre o antecessor e o topo
        """
        a = self.stack.pop(-1)
        b = self.stack.pop(-1)
        self.stack.append(int(b < a))

    def CPMA(self):
        """
        Comparação de maior
        """
        a = self.stack.pop(-1)
        b = self.stack.pop(-1)
        self.stack.append(int(b > a))

    def CPIG(self):
        """
        Comparação de igualdade
        """
        a = self.stack.pop(-1)
        b = self.stack.pop(-1)
        self.stack.append(int(b == a))

    def CDES(self):
        """
        Comparação de desigualdade
        """
        a = self.stack.pop(-1)
        b = self.stack.pop(-1)
        self.stack.append(int(b != a))

    def CPMI(self):
        """
        Comparação menor-igual
        """
        a = self.stack.pop(-1)
        b = self.stack.pop(-1)
        self.stack.append(int(b <= a))

    def CMAI(self):
        """
        Comparação maior-igual
        """
        a = self.stack.pop(-1)
        b = self.stack.pop(-1)
        self.stack.append(int(b >= a))

    def ARMZ(self, n):
        """
        :param n: Endereço
        Armazena o topo da pilha no endereço n de D
        """
        self.stack[n] = self.stack.pop(-1)

    def DSVI(self, p):
        """
        :param p: Endereço
        Desvio incondicional para a instrução de endereço p
        i: Aponta para próxima instrução a ser executada
        """
        i = p
        return i

    def DSVF(self, p):
        """
        :param p: Endereço
        Desvio incondicional para a instrução de endereço p
        i: Aponta para próxima instrução a ser executada
        """
        if self.stack.pop(-1):
            i = p
            return i

    def programa(self):
        self.C.append('INPP')
        self.loc += 1
        self.loc += 1
        self.corpo()
        self.loc += 1
        self.C.append('PARA')

    def corpo(self):
        self.dc()
        self.loc += 1
        self.comandos()
        self.loc += 1

    def dc(self):
        if self.input[self.loc][1] in ['real', 'integer']:
            self.dc_v()
            self.mais_dc()

    def mais_dc(self):
        if self.input[self.loc][1] == ';':
            self.loc += 1
            self.dc()

    def dc_v(self):
        type_var = self.tipo_var()
        self.loc += 1
        self.variaveis(type_var)

    def tipo_var(self):
        self.loc += 1
        if self.input[self.loc][1] == 'real':
            return 'real'
        else:
            return 'integer'

    def variaveis(self, type_var):
        if self.input[self.loc] not in self.reservedWord:
            self.C.append('ALME 1')
            self.adress += 1
            self.tableSymbol[self.input[self.loc][1]] = [type_var, [self.input[self.loc][1]], self.adress]
            self.loc += 1
            self.mais_var(type_var)

    def mais_var(self, type_var):
        if self.input[self.loc][1] == ',':
            self.loc += 1
            self.variaveis(type_var)

    def comandos(self):
        self.comando()
        self.mais_comandos()

    def mais_comandos(self):
        if self.input[self.loc][1] == ';':
            self.loc += 1
            self.comandos()

    def comando(self):
        if self.input[self.loc][1] in ['read', 'write']:
            a = self.input[self.loc][1]
            self.loc += 1
            self.loc += 1
            if self.input[self.loc][1] not in self.reservedWord and self.input[self.loc][1] in self.tableSymbol.keys():
                if a == 'read':
                    self.C.append('LEIT')
                    self.adress += 1
                    self.C.append(f'ARMZ {self.tableSymbol[self.input[self.loc][1]][2]}')
                else:
                    self.C.append(f'CRVL {self.tableSymbol[self.input[self.loc][1]][2]}')
                    self.adress += 1
                    self.C.append('IMPR')
                self.loc += 1
                self.loc += 1

        else:
            if self.input[self.loc][1] not in self.reservedWord and self.input[self.loc][1] in self.tableSymbol.keys():
                ident = self.input[self.loc][1]
                self.loc += 1
                self.loc += 1
                self.expressao()
                self.C.append(f'ARMZ {self.tableSymbol[ident][2]}')

    def expressao(self):
        self.termo()
        self.outros_termos()

    def termo(self):
        op_un = self.op_un()
        self.fator(op_un)
        self.mais_fatores()

    def op_un(self):
        if self.input[self.loc][1] == '-':
            self.loc += 1
            return '-'

    def fator(self, op_un):
        if self.input[self.loc][1] == '(':
            self.loc += 1
            self.expressao()
            if op_un:
                self.C.append('INVE')
            self.loc += 1
        else:
            if self.input[self.loc][0] == 'ident':
                if self.input[self.loc][1] not in self.reservedWord and self.input[self.loc][1] in self.tableSymbol.keys():
                    self.C.append(F'CRVL {self.tableSymbol[self.input[self.loc][1]][2]}')
                else:
                    self.C.append(f'CRVL {self.input[self.loc][1]}')
                if op_un:
                    self.C.append('INVE')
                self.loc += 1

    def outros_termos(self):
        if self.input[self.loc][1] in ['+', '-']:
            op_ad = self.op_ad()
            self.termo()
            if op_ad == '+':
                self.C.append('SOMA')
            else:
                self.C.append('SUBT')
            self.outros_termos()

    def op_ad(self):
        op = self.input[self.loc][1]
        self.loc += 1
        return op

    def mais_fatores(self):
        if self.input[self.loc][1] in ['*', '/']:
            op_mul = self.op_mul()
            self.fator(None)
            if op_mul == '*':
                self.C.append('MULT')
            else:
                self.C.input('DIVI')
            self.mais_fatores()

    def op_mul(self):
        op = self.input[self.loc][1]
        self.loc += 1
        return op
