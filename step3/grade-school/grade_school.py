class School:
    def __init__(self):
        self.students = dict()
        self.name_added = list()
    def add_student(self, name, grade):
        if name not in self.students:
            self.students[name] = grade
            self.name_added.append(True)
        else:
            self.name_added.append(False)
    def roster(self):
        if self.students == {}:
            return []
        else:
            answer = list()
            for i in range(max(self.students.values())):
                temp = [j for j in self.students if self.students[j]==i+1]
                temp.sort()
                answer.extend(temp)
            return answer

    def grade(self, grade_number):
        grade_students = list()
        for i in self.students:
            if self.students[i] == grade_number:
                grade_students.append(i)
        grade_students.sort()
        return grade_students

    def added(self):
        return self.name_added
