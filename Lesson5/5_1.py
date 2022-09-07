# Напишите программу, удаляющую из текста все слова, содержащие "абв".

def check_word(word, key):
    i = 0
    j = 0
    state = False
    while i < len(word):
        if word[i] == key[j]:
            i += 1
            j += 1
            state = True
        else:
            if state:
                state = False
            else:
                i += 1
            j = 0
        if j == len(key):
            return True
    return False

def clear_text(text):
    words = text.split()
    for word in words:
        if check_word(word, "абв"):
            words.remove(word)
    return " ".join(words)


text_to_clear = "аабв Шла сабвша по шоссабве и сосалабв сушку"
cleared_text = clear_text(text_to_clear)

print(text_to_clear)
print(cleared_text)

