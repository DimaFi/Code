# 15 номер: Написать не возвращающую значение функцию, которая изменяет список, 
# переданный в качестве параметра, в соответствии с заданием удалить четные элементы, 
# стоящие после максимального.

def modify_list(lst):
    if not lst:
        return

    max_value = max(lst)
    max_index = lst.index(max_value)
    
    lst[:] = lst[:max_index + 1] + [x for x in lst[max_index + 1:] if x % 2 != 0]

my_list = [1, 3, 5, 9, 4, 6, 7, 8, 1]
modify_list(my_list)
print(my_list)
