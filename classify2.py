N = int(raw_input())
if N <= 100:
    for i in range(N):
        line = raw_input()
        if "Apple" in line:
            print "computer-company"
        else:
            print "fruit"