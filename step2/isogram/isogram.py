def is_isogram(string):
    string = string.replace(' ','')
    string = string.replace('-','')
    string = string.lower()
    is_iso = True
    for i in string:
        if string.count(i) > 1:
            is_iso = False
            break
    return is_iso
