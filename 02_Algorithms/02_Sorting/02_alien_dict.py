def printOrder(alien_dict,n,k):
    # code here
    fin = []
    set1 =set()
    for i in range(n):
        word = alien_dict[i]
        if word[0] not in fin:
            fin.append(word[0])
        for char in word:
            set1.add(char)
    print(fin)
    fin = "".join(fin)
    set2 = set(fin)
    set2 = set1 - set2
    print(set1, set2)
    return fin