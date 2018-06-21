# def scoreGrade():
#     for i in range(0,10):
#         print random()
# scoreGrade() 
def scoreGrade(interation):
    import random       
    for x in range(interation):
        grade = random.randint(60,100)
        if grade < 70:
            print "score: ",grade, " -- low"
        if grade > 69 and grade < 80:
            print "score: ",grade, ' -- not so low but not so high'
        if grade > 79 and grade < 90:
            print "score: ",grade, ' -- pretty good'
        if grade > 89 and grade < 101:
            print "score: ",grade, ' -- great job'            

scoreGrade(10)        