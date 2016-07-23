# Year-Game-Attempt
Python script

The year game is a game where you try to use the digits of the current year to build formulas that produce the numbers from 1 to 100. 

For example, in the year 2016, 20 + 16 = 36, so 36 has been found. The more numbers found, the better the player.

This script builds a network of numbers and applies various algorithms to them, doing some fancy optimization along the way to speed things up.
I currently support addition, subtraction, powers, factorials, division, double factorials, and square roots. You can run the algorithm more than once to build a bigger network and potentially find more results, but in my experience 3 times is enough. The runs become exponentially slow.

To run the script change these lines to match the current year, so 2016 would be:
a = Unit(2)
b = Unit(0)
c = Unit(1)
d = Unit(6)
e = Unit(20)
f = Unit(16)
g = Unit(201)
h = Unit(2016)

And experiment with the values in these xrange functions, where smaller is faster but bigger is more accurate. These values work well:
for i in xrange(3):
    for k in xrange(1):

After 5 minutes, it will print the best formulas found for calculating each number. Be sure to double check the answers as there are one or two bugs. If a formula isn't evaluating properly, see if replacing one of the operators with addition works, as the operators default to addition if they hit a problem.

For 2016 we found these formulas (75/100):

powr(2,mult(0,16)) = 1
addn(addn(nega(2),0),sqrt(16)) = 2.0
addn(addn(nega(2),0),addn(nega(1),6)) = 3
rooot(addn(2,nega(fact(0))),sqrt(16)) = 4.0
addn(addn(2,nega(fact(0))),sqrt(16)) = 5.0
addn(addn(2,0),sqrt(16)) = 6.0
addn(addn(2,fact(0)),sqrt(16)) = 7.0
addn(addn(addn(2,nega(fact(0))),1),6) = 8
addn(addn(addn(2,0),1),6) = 9
addn(addn(addn(2,fact(0)),1),6) = 10
subt(fact(addn(2,fact(0))),addn(1,nega(6))) = 11
mult(2,rooot(nega(fact(0)),addn(1,6))) = 12
subt(20,addn(1,6)) = 13
addn(addn(nega(2),0),16) = 14
addn(addn(20,1),nega(6)) = 15
mult(2,rooot(fact(0),addn(1,6))) = 16
addn(addn(2,nega(fact(0))),16) = 17
addn(addn(2,0),16) = 18
addn(addn(2,fact(0)),16) = 19
mult(20,powr(1,6)) = 20
mult(addn(2,fact(0)),addn(1,6)) = 21
addn(fact(addn(2,fact(0))),16) = 22
mult(addn(addn(2,fact(0)),1),6) = 24
subt(20,addn(1,nega(6))) = 25
addn(20,mult(1,6)) = 26
addn(addn(20,1),6) = 27
addn(nega(20),mult(1,dfact(6))) = 28
addn(addn(nega(20),1),dfact(6)) = 29
mult(2,addn(nega(fact(0)),16)) = 30
mult(2,addn(0,16)) = 32
addn(nega(dfact(subt(fact(addn(2,fact(0))),1))),dfact(6)) = 33
mult(2,addn(fact(0),16)) = 34
addn(20,dfact(nega(addn(1,nega(6))))) = 35
addn(20,16) = 36
sqrt(mult(2,rooot(fact(0),addn(1,fact(6))))) = 38.0
addn(nega(dfact(addn(addn(2,fact(0)),1))),dfact(6)) = 40
subt(dfact(fact(addn(2,fact(0)))),addn(1,6)) = 41
addn(dfact(fact(addn(2,fact(0)))),mult(1,nega(6))) = 42
addn(dfact(fact(addn(2,fact(0)))),addn(1,nega(6))) = 43
subt(nega(2),addn(fact(0),addn(1,nega(dfact(6))))) = 44
addn(addn(nega(2),0),addn(nega(1),dfact(6))) = 45
subt(addn(nega(2),fact(0)),addn(1,nega(dfact(6)))) = 46
addn(addn(nega(2),0),addn(1,dfact(6))) = 47
addn(addn(nega(2),fact(0)),addn(1,dfact(6))) = 48
addn(addn(addn(2,0),nega(1)),dfact(6)) = 49
addn(addn(addn(2,nega(fact(0))),1),dfact(6)) = 50
addn(addn(addn(2,0),1),dfact(6)) = 51
addn(addn(addn(2,fact(0)),1),dfact(6)) = 52
subt(fact(addn(2,fact(0))),addn(1,nega(dfact(6)))) = 53
addn(fact(addn(2,fact(0))),mult(1,dfact(6))) = 54
addn(fact(addn(2,fact(0))),addn(1,dfact(6))) = 55
addn(dfact(addn(addn(2,fact(0)),1)),dfact(6)) = 56
addn(dfact(addn(fact(addn(2,fact(0))),1)),nega(dfact(6))) = 57
sqrt(mult(addn(nega(fact(addn(2,fact(0)))),1),nega(fact(6)))) = 60.0
addn(nega(2),powr(addn(fact(0),1),6)) = 62
addn(dfact(subt(fact(addn(2,fact(0))),1)),dfact(6)) = 63
powr(2,rooot(nega(fact(0)),addn(1,6))) = 64
addn(2,powr(addn(fact(0),1),6)) = 66
subt(20,addn(1,nega(dfact(6)))) = 67
addn(20,mult(1,dfact(6))) = 68
addn(addn(20,1),dfact(6)) = 69
sqrt(addn(addn(2,nega(fact(0))),fact(addn(1,6)))) = 71.0
addn(fact(addn(addn(2,fact(0)),1)),dfact(6)) = 72
addn(2,sqrt(addn(fact(0),fact(addn(1,6))))) = 73.0
powr(addn(2,fact(0)),sqrt(16)) = 81.0
addn(nega(20),dfact(addn(1,6))) = 85
mult(dfact(subt(fact(addn(2,fact(0))),1)),6) = 90
mult(2,subt(nega(fact(0)),addn(1,nega(dfact(6))))) = 92
mult(2,rooot(0,addn(nega(1),dfact(6)))) = 94
subt(dfact(fact(addn(2,fact(0)))),addn(1,nega(dfact(6)))) = 95
mult(2,rooot(nega(fact(0)),addn(1,dfact(6)))) = 96
addn(dfact(fact(addn(2,fact(0)))),addn(1,dfact(6))) = 97
mult(2,rooot(0,addn(1,dfact(6)))) = 98
addn(dfact(addn(fact(addn(2,fact(0))),1)),nega(6)) = 99
mult(2,rooot(fact(0),addn(1,dfact(6)))) = 100
Found: 75
[Finished in 294.4s]

Happy coding!
