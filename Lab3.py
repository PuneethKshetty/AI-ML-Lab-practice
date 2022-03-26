import csv
d = list(csv.reader(open('training.csv')))
for i in d:
    if i[-1] == 'Y':
        imp = i[:-1]
        break
s = ['?' for i in range(len(imp))]
g = [['?' for j in range(len(imp))] for i in range(len(imp))]
flag = False
k = 0
print("S[{}] : {} \n G[{} : {} \n".format(k,['?']*len(imp),k,['?']*len(imp)))
for i in d:
    if i[-1] == 'Y':
        for b in s:
            if b!='?':
                flag = True
                break
        if not flag:
            s = i[:-1]
        for j in range(len(imp)):
            if i[j]!=imp[j]:
                s[j] = '?'
                g[j][j] = '?'
    elif i[-1] == 'N':
         for j in range(len(imp)):
            if i[j]!=imp[j]:
                g[j][j] = imp[j]
            else:
                g[j][j] = '?'
    gh = []
    k+=1
    for a in g:
        for j in a:
            if j!='?':
                gh.append(a)
    if len(gh) == 0:
        gh = ['?' for i in range(len(imp))]
    print("S[{}] : {} \n G[{} : {} \n".format(k,s,k,gh))
