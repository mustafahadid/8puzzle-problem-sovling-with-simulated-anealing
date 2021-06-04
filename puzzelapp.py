from puzzle import*
import math, sys, random


def if_(test, result, alternative):
    if test:
        return result
    else:
        return alternative

schedule = lambda t: if_(t <1000, 200 *math.exp(-0.005*t ), 0)

for t in range(10):
    print(schedule(t))

def simulated_annealing(prob):
    current = prob.getStartState()
    
    for t in range(sys.maxsize):
        T = schedule(t)
        
        if T ==0:
            return current
        current.printState()
        print("T value is ", T)
        succs = prob.getSuccessor(current)
        next = random.choice(succs)
        delta_e = hvalue(next[0])-hvalue(current)
        if delta_e < 0 or probability(math.exp(delta_e/T)):
            current = next[0]


def probability(p):
    return p > random.uniform(0.0, 1.0)



    
state = PuzzleState([1,2,3,4,0,5,6,7,8])
prob = SearchProblem(state)
s = simulated_annealing(prob)
print ("final result")
s.printState()

