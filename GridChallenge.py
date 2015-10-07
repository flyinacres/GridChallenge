__author__ = 'rfischer'


T = input()

for i in range(0, T):
    N  = input()

    a = []
    for j in range(0, N):
        a.append(sorted(raw_input()))

    success = 1
    for y in range(0, N-1):
        a1 = a[y]
        a2 = a[y+ 1]
        for x in range(0, N):

            if a1[x] > a2[x]:
                success = 0
                break

if success:
    print 'YES'
else:
    print 'No'

#print a