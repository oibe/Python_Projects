import sys

class Matrix:
	def __init__(self, row , col,str):
		vals = str.split()
		self.row_len =row
		self.col_len = col
		matrix = []
		for x in range(row):
			curr_row = []
			for y in range(col):
				curr_row.append(int(vals[x*col+y]))
			matrix.append(curr_row)
		self.rows = matrix

	def transpose(self,a):
		return 	map(lambda i: 
					map(lambda x:x[i],a.rows),
				range(len(a.rows[0])))
	
	def add(a, b):
		if(a.row_len != b.row_len and a.col_len != b.col_len):
			return None
		return map(lambda val1,val2: 
				map(lambda i,j: i+j,val1,val2)
			,a.rows,b.rows)
			
	def multiply(a,b):
		if a.col_len != b.row_len:
			return None
		return map(lambda row:
		map(lambda col:
		reduce(lambda acumm,curr: acumm+curr , map(lambda i,j: i*j,row,col)),b.transpose(b)),a.rows)
		
		
	def __str__(self):
		return str(self.rows)

a = Matrix(3,3,'1 2 3 4 5 6 7 8 9')
b = Matrix(3,3,'100 200 300 400 500 600 700 800 900')
a_mult = Matrix.multiply(a,b)

c = Matrix(4,2,'1 2 3 4 5 6 7 8')
d = Matrix(2,4,'100 200 300 400 500 600 700 800')
c_mult = Matrix.multiply(c,d)

print c_mult

