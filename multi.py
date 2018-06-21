# Multiples
# Part I - Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise.

# def multi(low,high):
#     y = []
#     for x in range(low,high+1):
#         y.append(x)
#     print y
# multi(1,1000)    



# Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000.

# def five(low,high):
#     t=[]
#     for i in range(low,high+1):
#         if i%5 == 0:
#             t.append(i)
#         else:
#             continue
#     print t                
# five(5,1000000)



# Sum List
# Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]

# def sum(arr):
#     a = 0
#     b = 0
#     for n in range(0,len(arr)):
        
#         a = arr[n]
#         b = b + a
#     print b   
# sum([1, 2, 5, 10, 255, 3])



# Average List
# Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]

def sum(arr):
    a = 0
    b = 0
    for n in range(0,len(arr)):    
        a = arr[n]
        b = b + a
    print b/len(arr)
sum([1, 2, 5, 10, 255, 3])

