#!usr/bin/python3
def list_division(my_list1, my_list2, list_length):
    formed_list = []
    div = 0
    for i in range(0, list_length):
        try:
            div = my_list1[i] / my_list2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of ranage")
        finally:
            formed_list.append(div)
            div = 0
    return formed_list
