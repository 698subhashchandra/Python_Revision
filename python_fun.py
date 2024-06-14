
list1 = [24 , 30 , 25 , 12]
list2 = [10, 20, 30, 40]
#+, in   operater
#for , if  control flow
#result=0  dummy variable
#method  len , append

# create a empty list
# calculate the  len of list and compare with help of if and == opreter
# use for loop to gerenrete index nuber
#read element from list1 and list2
#add read element and append result in result_list




if len(list1)==len(list2):
    sum_of_list = []
    for index in range(len(list1)):
        sum_of_element =list1[index]+list2[index]
        sum_of_list.append(sum_of_element)
    print(sum_of_list)


else:
    print("list can not add because number of element are not same")


