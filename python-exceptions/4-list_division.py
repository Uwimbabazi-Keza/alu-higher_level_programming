#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            d = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            d = 0
            print("division by 0")
            continue
        except (TypeError, ValueError):
            d = 0
            print("wrong type")
            continue
        except IndexError:
            d = 0
            print("out of range")
        finally:
            new_list.append(d)
    return new_list
