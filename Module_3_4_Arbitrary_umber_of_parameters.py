def single_root_words(root_word, *other_words):
    root_word_down = root_word.lower()
    same_words = []
    for q in other_words:
        word_down = q.lower()
        if root_word_down in word_down or word_down in root_word_down:
            same_words.append(q)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
print(result1)
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result2)
result3 = single_root_words('Корен', 'корневой','корешок','кореннелый',
                            'коренастый','корнеплод','корень зла')
print(result3)