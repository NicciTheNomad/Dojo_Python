def coinToss(toss):
    import random
    head = 0
    tail = 0
    for i in range(0,toss):
        value = random.random()
        newValue = round(value)
        if newValue == 0.0:
            head += 1
        if newValue == 1.0:
            tail += 1
    print "heads occurred ",head
    print ' times. tails occurred',tail,' time. tosses attempted was: ',toss
coinToss(300)        