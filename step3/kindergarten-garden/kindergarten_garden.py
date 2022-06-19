class Garden:
    def __init__(self, diagram, students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']):
        self.diagram = diagram
        self.students = students
    def plants(self, name):
        rows = self.diagram.split('\n')
        sorted_students = sorted(self.students)
        ind = sorted_students.index(name)
        plants = list()
        for i in rows:
            plants.extend(i[2*ind : 2*ind+2])
        answer = list()
        for i in plants:
            if i == 'C':
                answer.append('Clover')
            elif i == 'G':
                answer.append('Grass')
            elif i == 'V':
                answer.append('Violets')
            else:
                answer.append('Radishes')
        return answer