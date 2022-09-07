def get_uniq(array):
    uniq = []
    for item in array:
        if item not in uniq:
            uniq.append(item)
        else:
            uniq.remove(item)
    return uniq


in_list = [6, 1, 2, 1, 3, 12, 12, 4, 5, 6] # [2, 3, 4, 5]
print(get_uniq(in_list))