'''# ______________Task1______________
a = ['banana','mango','chelovek']
b = ['200$','4004','0$']
c = dict(zip(a,b))
print(a, b, c)'''
# ______________Task2______________

def truster (w):
    sorted(w)
    if w==sorted(w):
        return True
    else:
        return False
print(truster([1,2,4,8,9,6,3,2,4]))
print(truster([1,2,4,4,5,6,7,8,8,9]))
'''#q = [1,3,5,7] # true
print(truster(q))
w = [1,5,3,8,0] # false'''