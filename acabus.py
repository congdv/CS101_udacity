#########################################################################
#                 10-row School abacus
#                         by
#                      Michael H
#########################################################################
#       Description partially extracted from from wikipedia 
#
#  Around the world, abaci have been used in pre-schools and elementary
#
# In Western countries, a bead frame similar to the Russian abacus but
# with straight wires and a vertical frame has been common (see image).
# Helps schools as an aid in teaching the numeral system and arithmetic
#
#         00000        row factor 1000000000
#         00000        row factor 100000000
#         00000        row factor 10000000 
#         00000        row factor 1000000
#         00000        row factor 100000
#         00000        row factor 10000
#         00000        row factor 1000
#         00000        row factor 100      1
#         00000        row factor 10       2
#         00000        row factor 1        3
#                                        -----------    
#                             Sum                123 
#
# Each row represents a different row factor, starting with x1 at the
# bottom, ascending up to x1000000000 at the top row.     
######################################################################

# TASK
# Define a procedure print_abacus(integer) that takes a positive integer
# and prints a visual representation (image) of an abacus setup for a 
# given positive integer value.
# 
# Ranking
# 1 STAR solved the problem!
# 2 STARS 6  lines = 9
# 3 STARS 3  lines = 6
# 4 STARS 0  lines = 3

def print_abacus(value):
    re_value = 0
    time = 10
    while(value != 0):
        times = 1
        for i in range(time):
            times = times * 10
        re_value = re_value + ((value % 10) * times)
        time = time - 1
        value = value / 10
    print re_value
    for i in range(10):
        x = re_value % 10
        re_value = re_value  / 10
        if (x == 0):
            print '00000       '
        elif (x == 1):
            print '00000      *'
        elif (x == 2):
            print '00000     **'
        elif (x == 3):
            print '00000    ***'
        elif (x == 4):
            print '00000   ****'
        elif (x == 5):
            print '00000   ****'
        elif (x == 6):
            print '0000   0****'
        elif (x == 7):
            print '000   00****'
        elif (x == 8):
            print '00   000****'
        else:
            print '0   0000****'
                
###  TEST CASES
print 'Abacus showing 0:'
print_abacus(0)
#00000   
#00000   
#00000   
#00000   
#00000   
#00000   
#00000   
#00000   
#00000   
#00000   
print "Abacus showing 12345678"
print_abacus(12345678)
#00000   
#00000   
#00000   
#00000   
#00000   
#00000   
#00000   
#00000
#00000
#00000
print "Abacus showing 1337"
print_abacus(1337)
#00000   
#00000   
#00000   
#00000   
#00000   
#00000   
#00000   
#00000   
#00000   
#000   00
