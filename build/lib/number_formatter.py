def num_format(num:int):
    list = []
    for i in str(num):
        list.append(i)
    length = len(list)
    if length == 4:
        list.insert(1, ',')
    elif length == 5:
        list.insert(2, ',')
    elif length == 6:
        list.insert(3, ',')
    elif length == 7:
        list.insert(1, ',')
        list.insert(5, ',')
    elif length == 8:
        list.insert(2, ',')
        list.insert(6, ',')
    elif length == 9:
        list.insert(3, ',')
        list.insert(7, ',')
    elif length == 10:
        list.insert(1, ',')
        list.insert(5, ',')
        list.insert(9, ',')
    elif length == 11:
        list.insert(2, ',')
        list.insert(6, ',')
        list.insert(10, ',')
    elif length == 12:
        list.insert(3, ',')
        list.insert(7, ',')
        list.insert(11, ',')
    elif length == 13:
        list.insert(1, ',')
        list.insert(5, ',')
        list.insert(9, ',')
        list.insert(13, ',')
    elif length == 14:
        list.insert(2, ',')
        list.insert(6, ',')
        list.insert(10, ',')
        list.insert(14, ',')
    elif length == 15:
        list.insert(3, ',')
        list.insert(7, ',')
        list.insert(11, ',')
        list.insert(15, ',')
    elif length == 16:
        list.insert(1, ',')
        list.insert(5, ',')
        list.insert(9, ',')
        list.insert(13, ',')
        list.insert(17, ',')
    elif length == 17:
        list.insert(2, ',')
        list.insert(6, ',')
        list.insert(10, ',')
        list.insert(14, ',')
        list.insert(18, ',')
    elif length == 18:
        list.insert(3, ',')
        list.insert(7, ',')
        list.insert(11, ',')
        list.insert(15, ',')
        list.insert(19, ',')
    elif length == 19:
        list.insert(1, ',')
        list.insert(5, ',')
        list.insert(9, ',')
        list.insert(13, ',')
        list.insert(17, ',')
        list.insert(21, ',')
    elif length == 20:
        list.insert(2, ',')
        list.insert(6, ',')
        list.insert(10, ',')
        list.insert(14, ',')
        list.insert(18, ',')
        list.insert(22, ',')
    elif length == 21:
        list.insert(3, ',')
        list.insert(7, ',')
        list.insert(11, ',')
        list.insert(15, ',')
        list.insert(19, ',')
        list.insert(23, ',')
    elif length > 21:
        print('num_format Reached Capacity')
    f = ''.join(str(h) for h in list)
    return f
