a={1,2,3,4,5}
b={4,5,6,7,8}
c={1,2,3,4,5}

#union

print(a.union(b))
print(a|b)

#intersection

print(a.intersection(b))
print(a & b)

#difference

print(a.difference(b))
print(a-b)
print(a-c)

#symmetric diffence

print(a.symmetric_difference(b))
print(a^b)