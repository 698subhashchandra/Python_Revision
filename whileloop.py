list1 = [10, 524, 10, 22]
list2 = [1,40, 25, 23]


sum_of_list = []


if len(list1) == len(list2):

    index = 0
    index += 1

    while index < len(list1):

        element1 = list1[index]
        element2 = list2[index]

       
        sum_of_element = element1 + element2



        sum_of_list.append(sum_of_element)




    print(sum_of_list)
else:
    print("Lists cannot be added because the number of elements is not the same.")
