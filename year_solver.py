import math
from decimal import *
import uuid

getcontext().prec = 3

class Unit:
    value = 0
    path = ""
    nexts = []
    guid = None

    def __init__(self, value, path=None):
        self.value = value
        self.nexts = []
        if path:
            self.path = path
        else:
            self.path = str(value)
        self.guid = uuid.uuid4()

    def __str__(self):
        return str(self.value)

    def getLength(self):
        if len(self.nexts) == 0:
            return 0
        else:
            return max([u.getLength() for u in self.nexts]) + 1


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


class Applicator:
    processed = {}

    def __init__(self):
        self.processed = {}

    def apply_opp_to_graph(self, anchor, n, opp):
        cached_nexts = [z for z in n.nexts]
        for nx in cached_nexts:
            new_unit = Unit(opp.logic(n, nx), opp.getName(n, b=nx))
            for nnx in nx.nexts:
                new_unit.nexts.append(nnx)
            isBest = True
            for unit in anchor.nexts:
                if (unit.value == new_unit.value):
                    if new_unit.getLength() == unit.getLength():
                        isBest = False
                if new_unit.value > 1000000 or new_unit.value < -1000000:
                    isBest = False
            if isBest:
                anchor.nexts.append(new_unit)
            self.apply_opp_to_graph(n, nx, opp)

    def apply_selfopp(self, j, opp):
        self.processed = {}
        ns = [y for y in j.nexts]
        for n in ns:
            self.apply_self_opp_to_graph(j, n, opp)
        self.processed = {}

    def apply_self_opp_to_graph(self, anchor, n, opp):
        try:
            self.processed[n.guid]
            return
        except KeyError:
            self.processed[n.guid] = True
            if (n.value <= 10000):
                new_unit = Unit(opp.logic(n), opp.getName(n))
                for nx in n.nexts:
                    new_unit.nexts.append(nx)
                isBest = True
                for unit in anchor.nexts:
                    if (unit.value == new_unit.value):
                        if new_unit.getLength() == unit.getLength():
                            isBest = False
                if new_unit.value > 1000000 or new_unit.value < -1000000:
                    isBest = False
                if isBest:
                    anchor.nexts.append(new_unit)
            cached_nexts = [z for z in n.nexts]
            for nx in cached_nexts:
                self.apply_self_opp_to_graph(n, nx, opp)


def power(a, b):
    try:
        if (b.value < 0 and a.value == 0) or (a.value < 0 and b.value - int(b.value) != 0) or b > 10:
            return a.value + b.value
        else:
            return a.value ** b.value
    except OverflowError:
        return a.value + b.value

def sqrtopp(a, b):
    try:
        if a.value == 0 or b.value < 0 or a.value < 0 or b.value > 5 or a.value > 5 or ((b.value ** (1.0 / a.value)) ** 2 == b.value):
            return a.value + b.value
        else:
            return b.value ** (1.0 / a.value)
    except OverflowError:
        return a.value+b.value

def doublefactorial(n):
     if n <= 0:
         return 1
     else:
         return n * doublefactorial(n-2)

sqrtOpp = Operator(lambda a, b: sqrtopp(a, b), "rooot")
addOpp = Operator(lambda a, b: a.value + b.value, "addn")
minusOpp = Operator(lambda a, b: a.value - b.value, "subt")
multOpp = Operator(lambda a, b: a.value * b.value, "mult")
powerOpp = Operator(lambda a, b: power(a, b), "powr")
divideOpp = Operator(lambda a, b: a.value + b.value if b.value == 0 else float(a.value) / float(b.value), "divis")
factorial = Operator(lambda a: a.value if a.value < 0 or type(a.value) is not int else math.factorial(a.value), "fact")
doubleFactorial = Operator(lambda a: a.value if ((a.value <= 0) or (not type(a.value) is int) or a.value > 10) else doublefactorial(a.value), "dfact")

sqrt = Operator(lambda a: a.value if a.value < 0 else math.sqrt(a.value), "sqrt")
dsqrt = Operator(lambda a: a.value if a.value < 0 else math.sqrt(math.sqrt(a.value)), "dsqrt")
nega = Operator(lambda a: -1 * a.value, "nega")

opps = [addOpp, sqrtOpp, minusOpp, multOpp, divideOpp, powerOpp]
#opps = []
opps = [addOpp,sqrtOpp,minusOpp,multOpp,divideOpp,powerOpp]
selfopps = [sqrt, factorial, doubleFactorial, nega]

j = Unit(100000000)
a = Unit(2)
b = Unit(0)
c = Unit(1)
d = Unit(6)
e = Unit(20)
f = Unit(16)
g = Unit(201)
h = Unit(2016)
i = Unit(2.0)
k = Unit(2.01)
l = Unit(2.016)
m = Unit(20.1)
n = Unit(20.16)
o = Unit(201.6)
p = Unit(0.1)
q = Unit(0.16)
r = Unit(1.6)
s = Unit(0.2)
u = Unit(0.1)
v = Unit(0.6)
w = Unit(0.201)
x = Unit(0.2016)

j.nexts.append(a)
j.nexts.append(e)
j.nexts.append(g)
j.nexts.append(h)
j.nexts.append(i)
j.nexts.append(k)
j.nexts.append(l)
j.nexts.append(m)
j.nexts.append(n)
j.nexts.append(o)
j.nexts.append(p)
j.nexts.append(q)
j.nexts.append(u)
j.nexts.append(w)
j.nexts.append(x)

a.nexts.append(b)
a.nexts.append(p)
a.nexts.append(q)

b.nexts.append(c)
b.nexts.append(f)
b.nexts.append(p)
b.nexts.append(q)
b.nexts.append(r)
b.nexts.append(u)

c.nexts.append(d)
c.nexts.append(v)

e.nexts.append(c)
e.nexts.append(f)
e.nexts.append(p)
e.nexts.append(q)
e.nexts.append(r)
e.nexts.append(u)

g.nexts.append(d)
g.nexts.append(v)

i.nexts.append(c)
i.nexts.append(f)
i.nexts.append(p)
i.nexts.append(q)
i.nexts.append(r)
i.nexts.append(u)

k.nexts.append(d)
k.nexts.append(v)

m.nexts.append(d)
m.nexts.append(v)

p.nexts.append(d)
p.nexts.append(v)

s.nexts.append(b)
s.nexts.append(p)
s.nexts.append(q)

u.nexts.append(d)
u.nexts.append(v)

w.nexts.append(d)
w.nexts.append(v)

app = Applicator()

for i in xrange(3):
    for k in xrange(1):
        for p in selfopps:
            app.apply_selfopp(j, p)
    for o in opps:
        for n in j.nexts:
            app.apply_opp_to_graph(j, n, o)
    # for k in xrange(2):
    #     for p in selfopps:
    #         app.apply_selfopp(j, p)

#print_graph(j)

rv = []
for k in j.nexts:
    if len(k.nexts) == 0:
        rv.append(k)

rv.sort(key = lambda x: x.value*10000000 + len(x.path)/10)

index = 0
found = 0
for unit in rv:
    if index >= 100:
        break
    if unit.value != index and unit.value - int(unit.value) == 0:
        print(unit.path + " = " + str(unit.value))
        if index > 0:
            found += 1
    index = unit.value
print("Found: " + str(found))