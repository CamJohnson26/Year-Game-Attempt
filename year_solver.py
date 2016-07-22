import math
from decimal import *
getcontext().prec = 3

class Unit:
    value = 0
    path = ""
    nexts = []

    def __init__(self, value, path=None):
        self.value = value
        self.nexts = []
        if path:
            self.path = path
        else:
            self.path = str(value)

    def __str__(self):
        return str(self.value)


class Operator:
    logic = None
    name = ""

    def __init__(self, logic, name):
        self.logic = logic
        self.name = name

    def getName(self, a, b=None):
        if b:
            return self.name + "(" + a.path + "," + b.path + ")"
        else:
            return self.name + "(" + a.path + ")"


def allOpps(ais, bis):
    rv = []
    for a in ais:
        for b in bis:
            for o in opps:
                try:
                    val = o.logic(a, b)
                    rv.append(Unit(val, path=o.getName(a, b)))
                except ZeroDivisionError:
                    pass
    return rv


def print_graph(n, space=""):
    print(space + str(n.path))
    space = space + "\t"
    for nx in n.nexts:
        print_graph(nx, space)


def apply_opp_to_graph(anchor, n, opp):
    cached_nexts = [z for z in n.nexts]
    for nx in cached_nexts:
        new_unit = Unit(opp.logic(n, nx), opp.getName(n, b=nx))
        for nnx in nx.nexts:
            new_unit.nexts.append(nnx)
        isBest = True
        for unit in anchor.nexts:
            if (unit.value == new_unit.value):
                if len(unit.path) <= len(new_unit.path) or len(new_unit.path) > 64:
                    isBest = False
            if (len(new_unit.nexts) < len(unit.nexts)):
                isBest = True
        if new_unit.value > 100000:
            isBest = False
        if isBest:
            anchor.nexts.append(new_unit)
        apply_opp_to_graph(n, nx, opp)


def apply_self_opp_to_graph(anchor, n, opp):
    cached_nexts = [z for z in n.nexts]
    if (n.value <= 10000):
        new_unit = Unit(opp.logic(n), opp.getName(n))
        for nx in n.nexts:
            new_unit.nexts.append(nx)
        isBest = True
        for unit in anchor.nexts:
            if (unit.value == new_unit.value):
                if len(unit.path) <= len(new_unit.path):
                    isBest = False
        if new_unit.value > 100:
            isBest = False
        if new_unit.path.startswith(opp.name + "(" + opp.name + "("):
            isBest = False
        if isBest:
            anchor.nexts.append(new_unit)
    for nx in cached_nexts:
        apply_self_opp_to_graph(n, nx, opp)


def power(a,b):
    try:
        if (b.value < 0 and a.value == 0) or (a.value < 0 and b.value - int(b.value) != 0) or b > 10:
            return a.value + b.value
        else:
            return a.value ** b.value
    except OverflowError:
        return a.value + b.value

def doublefactorial(n):
     if n <= 0:
         return 1
     else:
         return n * doublefactorial(n-2)

sqrtOpp = Operator(lambda a, b: a.value + b.value if a.value == 0 or b.value < 0 or b.value > 5 or a.value > 5 else b.value ** (1.0 / a.value), "rooot")
addOpp = Operator(lambda a, b: a.value + b.value, "addn")
minusOpp = Operator(lambda a, b: a.value - b.value, "subt")
multOpp = Operator(lambda a, b: a.value * b.value, "mult")
powerOpp = Operator(lambda a, b: power(a, b), "powr")
divideOpp = Operator(lambda a, b: a.value + b.value if b.value == 0 else float(a.value) / float(b.value), "divis")
factorial = Operator(lambda a: a.value if a.value < 0 or type(a.value) is not int else math.factorial(a.value), "fact")
doubleFactorial = Operator(lambda a: a.value if ((a.value <= 0) or (not type(a.value) is int) or a.value > 10) else doublefactorial(a.value), "dfact")

sqrt = Operator(lambda a: a.value if a.value < 0 else math.sqrt(a.value), "sqrt")
dsqrt = Operator(lambda a: a.value if a.value < 0 else math.sqrt(math.sqrt(a.value)), "dsqrt")

opps = [addOpp, sqrtOpp, minusOpp, multOpp, divideOpp, powerOpp]
#opps = []
selfopps = [sqrt, factorial, doubleFactorial]
j = Unit(100000000)
a = Unit(2)
b = Unit(0)
c = Unit(1)
d = Unit(6)
e = Unit(20)
f = Unit(16)
g = Unit(201)
h = Unit(2016)

j.nexts.append(a)
j.nexts.append(e)
j.nexts.append(g)
j.nexts.append(h)
a.nexts.append(b)
b.nexts.append(c)
b.nexts.append(f)
c.nexts.append(d)
e.nexts.append(c)
e.nexts.append(f)
g.nexts.append(d)


for i in xrange(4):
    for k in xrange(1):
        for p in selfopps:
            ns = [y for y in j.nexts]
            for n in ns:
                apply_self_opp_to_graph(j, n, p)
    for o in opps:
        for n in j.nexts:
            apply_opp_to_graph(j, n, o)
    for k in xrange(1):
        for p in selfopps:
            ns = [y for y in j.nexts]
            for n in ns:
                apply_self_opp_to_graph(j, n, p)

#print_graph(j)

rv = []
for k in j.nexts:
    if len(k.nexts) == 0:
        rv.append(k)

rv.sort(key = lambda x: x.value*10000000 + len(x.path)/10)

index = 0
for unit in rv:
    if unit.value != index and unit.value - int(unit.value) == 0:
        print(unit.path + " = " + str(unit.value))
    index = unit.value
