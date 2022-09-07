# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

input_text = ""

with open("input.txt", 'r') as f:
    input_text = f.read()

def RLE_compress(data_for_compress):
    encoded = ""
    i = 0
    j = 0
    count = 1
    while i <= len(data_for_compress) - 1:
        symbol = data_for_compress[i]
        j = i
        while j < len(data_for_compress) - 1:
            curr = data_for_compress[j]
            next = data_for_compress[j + 1]
            if curr == next:
                count += 1
                j += 1
            else:
                break
        encoded += f"{count}|{symbol},"
        count = 1
        i = j + 1
    return encoded
def RLE_decompress(data_for_decompress):
    decoded = ""
    groups = data_for_decompress.split(',')
    for group in groups:
        if len(group) > 0:
            params = group.split('|')
            for i in range(int(params[0])):
                decoded += params[1]
    return decoded

encoded_text = RLE_compress(input_text)
decoded_text = RLE_decompress(encoded_text)

print(input_text)
print(encoded_text)
print(decoded_text)

print(len(input_text))
print(len(encoded_text))
print(len(decoded_text))