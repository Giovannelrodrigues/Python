#conjunto usa-se {}, so pode ter um elemento de cada
conjunto = {1,2,3,4}

#adicionar elemento
conjunto.add(5)

#remover
conjunto.discard(2)
conjunto.remove(2)

#unir conjutos

conj1 = {1,2,3,4,5}
conj2 = {5,6,7,8}

conjuni = conj1.union(conj2)

#intersecção

conjinter = conj1.intersection(conj2)

#diferença

conjdife = conj1.difference(conj2)

#diferença simetrica

conjuto_diff_simetrica = conj1.symmetric_difference(conj2)

#pertinencia
conja = {1,2,3,4}
conjb = {1,2,3,4,5}
conjutosub = conjb.issubset(conja )

#superset ao contrário do issubset

conjunto_superset = conja.issuperset(conjb)

#tranforma

lista = [1,1,2,2,3,3]
conjuntonum = set(lista)

#"""""""" ao contrário
conjuntooo = {1,2,3}
listanum = list(conjuntooo)