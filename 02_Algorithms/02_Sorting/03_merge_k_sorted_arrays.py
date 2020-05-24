def merge(numbers):
    # code here
    fin_ls = numbers[0]
    idx = 0
    n = len(numbers)
    for i in range(1,n):
        cr_ls = list(numbers[i])
        if cr_ls[0] >= fin_ls[-1]:
            fin_ls.extend(cr_ls)
        elif cr_ls[-1] <= fin_ls[0]:
            fin_ls = cr_ls + fin_ls
        else:
            len1, len2 = len(cr_ls), len(fin_ls)
            merged_list = []
            idx_1, idx_2 = 0, 0
            i=0
            while i<(len1+len2):
                i += 1
                if cr_ls[idx_1] < fin_ls[idx_2]:
                    merged_list.append(cr_ls[idx_1])
                    idx_1 += 1
                    if idx_1 == len1:
                        merged_list.extend(fin_ls[idx_2:])
                        fin_ls = merged_list
                        i = len1 + len2 + 1
                else:
                    merged_list.append(fin_ls[idx_2])
                    idx_2 += 1
                    if idx_2 == len2:
                        merged_list.extend(cr_ls[idx_1:])
                        fin_ls = merged_list
                        i = len1 + len2 + 1
    return fin_ls


arr = [[5,9,44],[51,65,88],[2,79,89]]
fin = merge(arr)
print(fin)