# ----- LONG WAY -----
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

############################################## This is what map would do under the hood in JS
new_list = []

for num in my_list:
    new_list.append(num + 1)

print("New List 1", new_list)
##############################################

new_list2 = list(map(lambda num: num + 1, my_list)) #turns it into a list
print("New List 2", new_list2)

new_list2 = tuple(map(lambda num : num + 1, my_list)) #turns into a tuple
print("New List 2", new_list2)
##############################################

## [RESULT EXPRESSION for ITEM in COLLECTION]
new_list3 = [num + 1 for num in my_list]
print("New list 3" new_list3))