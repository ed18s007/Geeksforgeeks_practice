def formatArray(a,n):
    # add code here
    if len(a) <= 1:
        return a
    for i in range(1,n,2):
        if a[i] < a[i-1]:
            a[i-1], a[i] = a[i], a[i-1]
    return a

if __name__ == "__main__":
	t = int(input())
	for j in range(t):
		n = int(input())
		a = list(map(int, input().split()))
		b = formatArray(a,n)
		if len(b)==len(a):
			for k in range(1,n,2):
				if b[k]<b[k-1]:
					flag = 0
			if flag==0:
				print(0)
			else:
				b.sort()
				a.sort()
				for p in range(0,n):
					if (a[p]!=b[p]):
						flag=0
				print(flag)
		else:
			print(0) 