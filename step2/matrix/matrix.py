class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self, index):
        rows = self.matrix_string.split('\n')
        answer = rows[index-1]
        answer = answer.split(' ')
        answer = [int(i) for i in answer]
        return answer

    def column(self, index):
        rows = self.matrix_string.split('\n')
        rows = [i.split(' ') for i in rows]
        answer = list()
        for i in rows:
            answer.append(int(i[index - 1]))
        return answer
