set1 = {1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,4,4,4,4,4,4,5,5,5,5,}
print(set1)

set1.add(6)
print(set1)


set2 = {3,4,5,6,7,8}



diff = set2.difference(set1)
print(diff)

symmetric = set2.symmetric_difference(set1)
print(symmetric)