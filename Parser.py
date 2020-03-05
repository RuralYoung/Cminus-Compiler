token = ''
tokenNum = 0
tokenList = []


def main(inputList):
    global tokenNum, token, tokenList

    #checks to see if the input is empty
    try:
        token = inputList[tokenNum]
        tokenList = inputList
    except IndexError:
        print('REJECT')
        exit()

    #Adds the last Accept
    tokenList.append('$')

    #the beginning of the program (Sends it over to A: Program)
    A()

    if token == '$':
        print('ACCEPT')
    else:
        print('REJECT')


def check(checkToken):
    global tokenNum, token, tokenList
    if token == checkToken:
        #Checks the next token in the list
        tokenNum += 1
        token = tokenList[tokenNum]
    else:
        print('REJECT')
        exit()


def A():
    #A: Program
    B()


def B():
    #B: Declaration List
    C()
    Bprime()


def Bprime():
    #Bprime: Declaration List Prime
    if token == 'int' or token == 'void':
        C()
        Bprime()


def C():
    #C: Declaration
    if token == 'int' or token == 'void':
        E()
        check('ID')
        if token == ';' or token == '[':
            D()
        elif token == '(':
            F()


def D():
    #D: Var-Declaration"
    if token == 'int' or token == 'void':
        C()

    if token == ';':
        check(';')
    elif token == '[':
        check('[')
        check('NUM')
        check(']')
        check(';')


def E():
    #E: Type-Specifier
    if token == 'int':
        check('int')
    elif token == 'void':
        check('void')


def F():
    #F: Fun-Declaration"
    if token == '(':
        check('(')
        G()
        check(')')
        J()


def G():
    #G: Params"
    if token == 'int':
        H()
    elif token == 'void':
        check('void')
        if token == 'ID':
            check('ID')
            if token == '[':
                check('[')
                check(']')
            Hprime()
    else:
        print('REJECT')
        exit()


def H():
    #H: Param-list
    I()
    Hprime()


def Hprime():
    #Hprime: Param-list Prime
    if token == ',':
        check(',')
        I()
        Hprime()


def I():
    #"I: Param
    if token == 'int' or token == 'void':
        E()
        if token == 'ID':
            check('ID')
            if token == '[':
                check('[')
                check(']')


def J():
   #J: Compound STMT
    check('{')
    K()
    L()
    check('}')


def K():
    #K: Local-Declarations
    Kprime()


def Kprime():
    #Kprime: Local-Declarations Prime
    if token == 'int' or token == 'void':
        D()
        Kprime()


def L():
    #L: Statement-List"
    Lprime()


def Lprime():
    #Lprime: Statement-List Prime
    if token == '(' or token == 'ID' or token == ';' or token == 'if' or token == 'NUM' or token == 'return' or token == 'while' or token == '{':
        M()
        Lprime()


def M():
    #M: Statement
    if token == '(' or token == ';' or token == 'ID' or token == 'NUM':
        N()
    elif token == '{':
        J()
    elif token == 'if':
        O()
    elif token == 'while':
        P()
    elif token == 'return':
        Q()


def N():
    #N: Expression-Stmt
    if token == ';':
        check(';')
    elif token == '(' or token == 'ID' or token =='NUM':
        R()
        check(';')


def O():
    #O: Selection-Stmt
    check('if')
    check('(')
    R()
    check(')')
    M()
    if token == 'else':
        check('else')
        M()


def P():
    #P: Iteration-Stmt
    check('while')
    check('(')
    R()
    check(')')
    M()


def Q():
    #Q: Return-Stmt
    check('return')
    if token == ';':
        check(';')
    elif token == '(' or token == 'ID' or token == 'NUM':
        R()
        check(';')


def R():
    #R: Expression
    if token == 'ID':
        # the Try/Catch is implemented just in case an indexoutofbounds occurs
        #Essentially, the "Worst case scenario" when it comes to ID is that it gets sent to T()
        try:
            tempToken = tokenList[tokenNum + 1]
        except IndexError:
            return

        try:
            tempToken2 = tokenList[tokenNum + 4] # Essentially checking if there is a + after
        except IndexError:
            return

        if tempToken == '(':
            T()

        elif tempToken == '=':
            check('ID')
            check('=')
            R()

        elif tempToken == '[':
            if tempToken2 == '=':
                check('ID')
                check('[')
                R()
                check(']')
                check('=')
                R()
            else:
                T()
        else:
            T()

    elif token == '(' or token == 'NUM':
        T()
    else:
        #theres an empty where it shouldn't appear
        print('REJECT')
        exit()

#I included this for posterity but commented it out as it was no longer necessary
#def S():
#    S: Var
#
#    check('ID')
#    check('[')
#    R()
#    check(']')


def T():
    #T: Simple-Expression"
    if token == '(' or token == 'ID' or token == 'NUM':
        V()
        if token == '!=' or token == '<' or token == '<=' or token == '==' or token == '>' or token == '>=':
            U()
            V()


def U():
    #U: Relop
    if token == '!=':
        check('!=')
    elif token == '<':
        check('<')
    elif token == '<=':
        check('<=')
    elif token == '==':
        check('==')
    elif token == '>':
        check('>')
    elif token == '>=':
        check('>=')


def V():
    #V: Additive-Expression
    X()
    Vprime()


def Vprime():
    #Vprime: Additive-Expression Prime
    if token == '+' or token == '-':
        W()
        X()
        Vprime()


def W():
    #W: Addop
    if token == '+':
        check('+')
    elif token == '-':
        check('-')


def X():
     #X: Term
     Z()
     Xprime()


def Xprime():
    #Xprime: Term Prime
    if token == '*' or token == '/':
        Y()
        Z()
        Xprime()


def Y():
    #Y: Mulop
    if token == '*':
        check('*')
    elif token == '/':
        check('/')


def Z():
    #Z: Factor
    if token == '(':
        check('(')
        R()
        check(')')
    elif token == 'NUM':
        check('NUM')
    elif token == 'ID':
        check('ID')
        if token == '[':
            check('[')
            R()
            check(']')
        elif token == '(':
            check('(')
            BB()
            check(')')


#Same with this, I left this as a "This was an original function"
#def AA():
#    AA: Call

#    check('(')
#    BB()
#    check(')')


def BB():
    #BB: Args
    if token == 'ID' or token == '(' or token == 'NUM':
        CC()


def CC():
    #CC: Arg-List
    R()
    CCprime()


def CCprime():
    #CCprime: Arg-List prime
    if token == ',':
        check(',')
        R()
        CCprime()