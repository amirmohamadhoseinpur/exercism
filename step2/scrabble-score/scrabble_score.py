def score(word):
    word = word.upper()
    answer = 0
    for i in word:
        if i in ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T']:
            answer += 1
        elif i in ['D' , 'G']:
            answer += 2
        elif i in ['B', 'C', 'M', 'P' ]:
            answer += 3
        elif i in ['F', 'H', 'V', 'W', 'Y' ]:
            answer += 4
        elif i in ['K']:
            answer += 5
        elif i in ['J', 'X']:
            answer += 8
        elif i in ['Q', 'Z']:
            answer += 10
    return answer
