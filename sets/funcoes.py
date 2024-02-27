conjunto1 = {1, 2, 3, 4, 5, "Nycolas"}
conjunto2 = {"Nycolas", "Atylas", "Davi", 2, 4, 5 }

print("\nunion --- ---")
conjunto3 = conjunto1.union(conjunto2)
print(conjunto3)

# O intersection devemos atribuir ele a uma variavel
print("\nintersection --- ---")
print(conjunto1.intersection(conjunto2))

print("\nintersection_update --- ---")
conjunto1.intersection_update(conjunto2)
print(conjunto1)



