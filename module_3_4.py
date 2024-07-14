def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        w = root_word.lower()
        v = i.lower()
        if v.count(w) > 0 or w.count(v) > 0:
            same_words.append(i)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)


