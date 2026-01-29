def list_to_dict(list1:list, list2:list) -> dict:
    """
    Docstring for list_to_dict
        :param list1: must be keys of dictionary
        :type list1: list
        :param list2: must be values of dictionary
        :type list2: list
    
    """
    if len(list1) == len(list2):
        list_of_all_keys_and_values_with_zip_func = list(zip(list1, list2))
        # print(list_of_all_keys_and_values_with_zip_func)
        dictionary_result = {}
        for item in list_of_all_keys_and_values_with_zip_func:
            dictionary_result[item[0]] = item[1]
        print(dictionary_result)
    else:
        minLen = min(len(list1), len(list2))
        list1 = list1[:minLen]
        list2 = list2[:minLen]
        list_to_dict(list1, list2)



name_list = ["Reza", "Ali", "Abolfazl", "Mohammad", "a"]
age_list = [25,24,24,26, 1, 2, 3, 4]

list_to_dict(name_list, age_list)