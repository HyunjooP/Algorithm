
def findMinIndex(ary) :
    Minindex = 0
    for i in range(1, len(ary)) :
        if ( ary[Minindex] > ary[i] ) :
            Minindex = i
    return Minindex            

testAry = [55, 88, 33, 77]


minPos = findMinIndex(testAry)
print('최소값은', testAry[minPos])