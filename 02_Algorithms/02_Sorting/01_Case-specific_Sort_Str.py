def caseSort(s,n):
    #code here
    sml, cpt, fin = "","",""
    for c in s:
        if ord(c)<97:
            cpt += c
        else:
            sml += c
    cpt=''.join(sorted(cpt))
    sml=''.join(sorted(sml))
    x,y = 0, 0
    for c in s:
        if ord(c)<97:
            fin += cpt[x]
            x+=1
        else:
            fin+=sml[y]
            y+=1
    return fin