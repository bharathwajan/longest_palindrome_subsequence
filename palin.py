counter = []  # just holds the values not a exact palindrom


def max_len_palin(data):
    print("input data :", data)
    # if len equals 1 ,this if logic will append it twice to the list that may result in error
    if len(data) > 0 and len(data) != 1:
        print("inside")
        data = data
        ref = data[0]  # reference pointer
        match = data[len(data)-1]  # match pointer
        print(ref)
        print(match)
        if ref == match:
            counter.append(ref)
            counter.append(match)
            data = data[1:len(data)-1]  # decresing both the sides
            return (max_len_palin(data))
        else:
            data = data[0:len(data)-1]
            return(max_len_palin(data))
    elif len(data) == 1:
        counter.append(data)
        data = data[0:len(data)-1]
        return(max_len_palin(data))
    else:
        print("rechead last part")
        return counter


data = "etiyntje"
print("the given palindrome is", data)
result = max_len_palin(data)
print("length of the biggest palundrome :", len(result))
