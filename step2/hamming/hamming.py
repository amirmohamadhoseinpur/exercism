def distance(strand_a, strand_b):
    count = 0
    try:
        lenght = max([len(strand_a) , len(strand_b)])
        for i in range(lenght):
            if strand_a[i] != strand_b[i]:
                count += 1
        return count
    except :
        raise ValueError("Strands must be of equal length.")
