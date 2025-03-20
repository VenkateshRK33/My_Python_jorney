import itertools

n=int(input("enter the number off alpha: "))
elements=input("enter the alpha: ").split()
k=int(input("enter number off combination"))

combi=list(itertools.combinations(elements,k))

count=0
for combo in combi:
    if 'a' in combo:
        count+=1

print("a is in comibation: ",count)

prob=count/len(combi)
print("probabilty is: "+"{0:.4f}".format(prob))