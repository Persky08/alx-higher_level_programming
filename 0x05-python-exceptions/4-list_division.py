def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    for i in range(list_length):
        try:
            element_1 = my_list_1[i]
            element_2 = my_list_2[i]

            if not (isinstance(element_1, (int, float)) and
                    isinstance(element_2, (int, float))):
                raise TypeError("Wrong type")

            result = element_1 / element_2 if element_2 != 0 else 0
        except (TypeError, ZeroDivisionError, IndexError) as e:
            print(e)
            result = 0
        finally:
            result_list.append(result)

    return result_list
