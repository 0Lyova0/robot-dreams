
set_1 = {0, 1, 2, 3, 4, 5, 8, 10}
set_2 = {0, 2, 2, 5, 5, 4, 6, 7, 8, 9, 10}


# ====== task 1
def same_elements():
    print(set_1 & set_2)

same_elements()

# ====== task 2
def unique():
     print(set_1 | set_2)

unique()


# ===== Maybe I dont understand it right.
#
# list_1 = (0, 1, 2, 3, 4, 5, 8, 10)
# list_2 = (0, 2, 2, 5, 5, 4, 6, 7, 8, 9, 10)
#
# new_set1 = set(list_1)
# new_set2 = set(list_2)
#
# def same_elements_2():
#     print(new_set1 & new_set2)
#
# def uniue_2():
#     print(set(list_1) | set(list_2))
#
#
# same_elements_2()
# uniue_2()