class Math(object):
    def __init__(self):
        self.value = 0

    def add(self, *nums):
        for num in nums:
            if type(num) == list or type(num) == tuple:
                for i in num:
                    self.value += i
            else:    
                self.value += num
        return self

    def sub(self, *nums):
        for num in nums:
            self.value -= num
        return self

    def result(self):
        print self.value
        return self       

md = Math()
md.add([2,2,4]).result()
m2 = Math()
print m2.add(2).add(2,5).sub(3,2).value



# ---------------------
# class MathDojo(object):
#     def __init__(self):
#         self.result = 0
#     def add(self, *args):
#         for i in args:
#             if type(i) == list or type(i) == tuple:
#                 for k in i:
#                     self.result += k
#             else:
#                 self.result += i
#         return self





