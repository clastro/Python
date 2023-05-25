tuple_list = (['a','b','c','d'],[1,2,3,4])
tuple_list2 = (['aa','bb','cc','dd'],[11,22,33,44])

#Non-Pythonic code
empty_list = []
for i in tuple_list[0]:
    empty_list.append(i)
for i in tuple_list[1]:
    empty_list.append(i)
for i in tuple_list2[0]:
    empty_list.append(i)
for i in tuple_list2[1]:
    empty_list.append(i)
    
#Pythonic code

from itertools import chain
empty_list = list(chain(*list_a, *list_b))

#empty_list : ['a', 'b', 'c', 'd', 1, 2, 3, 4, 'aa', 'bb', 'cc', 'dd', 11, 22, 33, 44]
