nabytek = ["stul","židle","skřín","komoda","katedra","almara"]
y = len(nabytek)
print(y)

nabytek.append("šuplík")
nabytek.pop(1)


for y in nabytek:
    print(y)
    
print(                     )
nabytek.sort(reverse=True)

for y in nabytek:
    print(y)