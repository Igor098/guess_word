def replace_char_at_index(original_string, indices, new_char):
    new_word = list(original_string)
    for index in indices:
        if 0 <= index < len(new_word) and new_word[index] == '❓':
            new_word[index] = new_char
    return "".join(new_word)
