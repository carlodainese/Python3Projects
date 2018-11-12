v1 = []
for x in range(1,101):
    if x%2 == 0:
        v1.append(1)
    else:
        v1.append(0)

# posso stampare la rappresentazione di una 
# lista su terminale in questo modo:
s_v1 = repr(v1)
print(s_v1)

#oppure posso stamparla su file
f = open("vector.txt", "w")
f.write(s_v1)
f.close()
print("Stampato con successo v1.")

#posso contare i numeri pari e quelli dispari presenti nell'intervallo [1:100]
p = v1.count(1)
d = v1.count(0)

print("I numeri pari tra 1 e 100 compresi sono ", p,
      ".\n", "Mentre quelli dispari sono ", d, ".\n")

#posso cambiare gli elementi di una lista come per un vettore in C
v2 = [0, 1, 2]
print(repr(v2))
v2[2] = 3
print(repr(v2))



