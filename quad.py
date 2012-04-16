# Enter your code here. Read input from STDIN. Print output to STDOUT
from sys import *

def solve(query,points):
    choice = query[0]
    start = int(query[1])-1
    end = int(query[2])-1
    
    if choice == 'C':
        one = 0
        two = 0
        three = 0
        four = 0
        
        while start <= end:
            p = points[start]
            start+=1
            if p[0] > 0 and p[1] > 0:
                one+=1
            elif p[0] > 0 and p[1] < 0:
                four+=1
            elif p[0] < 0 and p[1] > 0:
                two+=1
            else:
                three+=1
        print "%d %d %d %d" % (one,two,three,four)
    elif choice == 'X':
		while start <= end:
			p = points[start]
			start+=1
			p[1]*=-1
    else:
        while start <= end:
			p = points[start]
			start+=1
			p[0]*=-1
    return
                
num_points =  int(stdin.readline())

points = []
for i in range(num_points):
    temp = stdin.readline().split() 
    temp[0] = int(temp[0])
    temp[1] = int(temp[1])
    points.append(temp)
   

num_queries = int(stdin.readline())
for j in range(num_queries):
    solve(stdin.readline().split(),points)
