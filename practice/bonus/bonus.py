def transform(start_str, end_str, str_list):

    def is_there_substitution(first, second):
        gkey = False
        for i in range(len(first)):
            if first[:i] + first[i + 1:] == second[:i] + second[i + 1:]:
                key = True
                break
        return key

    def is_there_removal(first, second):
        gkey = False
        for i in range(len(first)):
            if first[:i]+first[i+1:]==second:
                gkey=True
                break

        return key

    def is_there_insert(first, second):
        gkey = False
        for j in range(len(second)):
            if first == second[:j] + second[j + 1:]:
                gkey = True
                break

        return gkey

    if start_str==end_str:
        return 1

    temp_array=[]

    for i in str_list:

        if is_there_substitution(start_str, i) :
            temp_array.append(transform(i ,end_str,list(filter(lambda x:x!=i,str_list))))
        if is_there_removal(start_str, i) :
            temp_array.append(transform(i ,end_str,list(filter(lambda x:x!=i,str_list))))
        if is_there_insert(start_str, i) :
            temp_array.append(transform(i ,end_str,list(filter(lambda x:x!=i,str_list))))

    if len(temp_array)==0 or len(temp_array)==temp_array.count(0):
        return 0
    return 1+min(list(filter(lambda x:x!=0,temp_array)))

