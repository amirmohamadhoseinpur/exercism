def abbreviate(words):
    for i in words:
        if not i.isalpha() and i not in ['-' , ' ']:
            words = words.replace( i , '' )
    words = words.split(' ')
    new_words = list()
    for i in words:
        new_words.extend(i.split('-'))
    answer = ''
    for i in new_words:
        if i not in ['-' , ' ' , '']:
            answer += i[0]
    answer = answer.upper()
    return answer
