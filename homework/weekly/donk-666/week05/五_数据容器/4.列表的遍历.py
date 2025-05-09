#用while循环遍历
def list_while_fun():
    my_list=['jiaoyu','heima','python']
    index=0
    while index<len(my_list):
        element=my_list[index]
        print(element)
        index+=1
list_while_fun()

def list_for_fun():
    mylist=[1,2,3,4,5]
    for element in mylist:
        print(element)
list_for_fun()