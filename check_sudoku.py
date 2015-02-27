correct = [[1,2,3],
           [2,1,3],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
               
def check_sudoku(p):
    n = len(p)
    digit = 1
    #check digit in matrix
    while (digit <= n):
        i = 0
        #check row
        while (i < n):
            count_row = 0
            count_col = 0
            j = 0
            #check collum and row
            while (j < n):
                print "p[%d][%d]" %(i,j)
                print "p[%d][%d]" %(j,i)
                #count row
                if (p[i][j] == digit):
                    count_row = count_row + 1
                #count collum
                if (p[j][i] == digit):
                    count_col = count_col + 1
                j = j + 1
            if (count_row != 1 or count_col != 1):
                print False
            i = i + 1
        digit = digit + 1
    print True
              

check_sudoku(correct)