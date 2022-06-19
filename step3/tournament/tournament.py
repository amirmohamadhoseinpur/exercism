def tally(rows):
    table = ["Team                           | MP |  W |  D |  L |  P"]
    teams = dict()
    for i in rows:
        j = i.split(';')
        teams[j[0]] = [0 for k in range(5)]
        teams[j[1]] = [0 for k in range(5)]
    for i in rows:
        j = i.split(';')
        if j[2] == 'win':
            teams[j[0]][0] += 1
            teams[j[0]][1] += 1
            teams[j[0]][4] += 3
            teams[j[1]][0] += 1
            teams[j[1]][3] += 1
        elif j[2] == 'loss':
            teams[j[0]][0] += 1
            teams[j[0]][3] += 1
            teams[j[1]][4] += 3
            teams[j[1]][0] += 1
            teams[j[1]][1] += 1
        else:
            teams[j[0]][0] += 1
            teams[j[0]][2] += 1
            teams[j[0]][4] += 1
            teams[j[1]][0] += 1
            teams[j[1]][2] += 1
            teams[j[1]][4] += 1
    teams = list(teams.items())
    teams.sort(key=lambda x:x[0])
    teams.sort(key=lambda x:(x[1][-1]), reverse=True)
    for i in teams:
        item = "{0:31}|  {1} |  {2} |  {3} |  {4} |{5:>3}".format(i[0], i[1][0], i[1][1], i[1][2], i[1][3], i[1][4])
        table.append(item)
    return table
