def remove_char_at(str, n):
    index = 0
    string = ""
    for char in str:
        if index == n:
            string = string
        else:
            string += char
        index += 1
    return string 
