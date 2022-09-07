# [f(x) if condition else g(x) for x in sequence]

def get_uniq(array):
    uniq = []
    [uniq.append(item) if item not in uniq else uniq.remove(item) for item in array]
    return uniq


in_list = [6, 1, 2, 1, 3, 7, 12, 12, 4, 5, 6] # [2, 3, 4, 5]
print(get_uniq(in_list))