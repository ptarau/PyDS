# Examples
# And(Or(False_(),True_()),True_()).ev()
# True_().ev()
# False_().ev()
# Or(True_(), Or(False_(),False_())).ev()
# Most of the code copied from Tauru Lecture
# And & Or classes ev() by John Long

class Expr:
    pass

class True_(Expr):
    def __init__(self):
        self.x = 1
    def ev(self):
        return self.x

class False_(Expr):
    def __init__(self):
        self.x = 0
    def ev(self):
        return self.x

class Not(Expr):
    def __init__(self, x):
        self.x = x
    def ev(self):
        return 1-self.x.ev()

class Or(Expr):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def ev(self):
        return max(self.x.ev(),self.y.ev())

class And(Expr):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def ev(self):
        return min(self.x.ev(),self.y.ev())

def t1() :
  return And(Or(False_(), True_()), True_()).ev()

def t2() :
  return Or(True_(), Or(False_(), False_())).ev()

def t3() :
  return And(Not(True_()),True_()).ev()
