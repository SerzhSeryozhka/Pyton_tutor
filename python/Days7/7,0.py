q="(){}[]"
q=list(q)
print(q)
for i in q:
    if i is "(" or i is "[" or i is "{":
        print (True)
    elif i in range(0, len(q)) and i in range(1, len(q)):
        print (True)
    elif "{" in range(0, len(q)) and "}" in range(1, len(q)):
        print (True)
    else:
        print (False)