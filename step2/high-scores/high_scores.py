class HighScores:
    def __init__(self, scores):
        self.scores = scores
    
    def latest(self):
        answer = self.scores[-1]
        return answer
    
    def personal_best(self):
        answer = max(self.scores)
        return answer

    def personal_top_three(self):
        answer = list()
        self.scores2 = self.scores[:]
        if len(self.scores2) >= 3:
            rg = 3
        else:
            rg = len(self.scores2)
        for i in range(rg):
            maxi = max(self.scores2)
            ind = self.scores2.index(maxi)
            answer.append(self.scores2.pop(ind))
        return answer

    
