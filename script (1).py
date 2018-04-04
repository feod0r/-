import math
class Vector(object):
	x = float
	y = float
	def setBNumbers(self,x,y):
		self.x = x
		self.y = y
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def setFList(self,lilpep):
		self.x = lilpep[0]
		self.y = lilpep[1]
	def __add__(self,other):
		return Vector(self.x+other.x,self.y+other.y)
	def __sub__(self,other):
		return Vector(self.x-other.x,self.y-other.y)
	def __str__(self):
		return '({}, {})'.format(self.x, self.y)
	def __mul__(self,number):
		return Vector(self.x*number,self.y*number)
	def __lt__(self,other):
		if (self.x**2-(self.x*self.y)+3*(self.y**2)-self.x)<(other.x**2-(other.x*other.y)+3*(other.y**2)-other.x):
			return 1
		else:
			return 0
	def __gt__(self,other):
		if (self.x**2-(self.x*self.y)+3*(self.y**2)-self.x)>(other.x**2-(other.x*other.y)+3*(other.y**2)-other.x):
			return 1
		else:
			return 0			

#функция генерации приращения		
def increments(n,m):
	return([round((math.sqrt(n+1)-1)/(n*math.sqrt(2))*m,3 ),round((math.sqrt(n+1)+n-1)/(n*math.sqrt(2))*m,3 )])
#вычисление вершин симплекса
def topsFInc(Vector1,Vector2):
	return(Vector1+Vector2)	
#Центр тяжести вершин
def pivotPoint2D(Vector1,Vector2):
	return (Vector(round((Vector1.x+Vector2.x)/n, 3),round((Vector1.y+Vector2.y)/n, 3)))
def pivotPoint3D(Vector1,Vector2,Vector3):
	return (Vector(round((Vector1.x+Vector2.x+Vector3.x)/3, 3),round((Vector1.x+Vector2.x+Vector3.x)/3, 3)))
#координаты отраженной вершины
def coordMirorred(Vector1,Vector2,MaxVector):
	return (Vector(round(n*pivotPoint2D(Vector1,Vector2).x - MaxVector.x, 3),round(n*pivotPoint2D(Vector1,Vector2).y - MaxVector.y, 3)))
#делает что-то там с симплексом
def iterN(vectors):
	flag = 1
	for i in range(3):
		if functionV(vectors[i]-pivotPoint3D(vectors[0],vectors[1],vectors[2]))<eps:
			flag = flag * 0
		else: 
			flag = flag * 1
	return flag

#Вектор из списка
def VectorFList(lilpep,bool):
	if bool:
		return Vector(lilpep[0],lilpep[1])
	else:
		return Vector(lilpep[1],lilpep[0])
	
#исходная функция	
def function(x1,x2):
	return round((x1**2-(x1*x2)+3*(x2**2)-x1), 3)
def functionV(Vector1):
	return function(Vector1.x,Vector1.y)

eps = 0.1
n = 2
m = 0.25
table = []

table.append(Vector(0,0))
table.append(table[0] + VectorFList(increments(n, m), 1))
table.append(table[0] + VectorFList(increments(n, m), 0))
table.sort()
d=0
while not iterN(table):
	print("Итерация:",d)
	if not iterN(table):
		table.append(pivotPoint2D(table[0],table[1])*2-table[2])
	table.sort()
	print("вершина","(x1, x2)","f(x)")
	for i in range(3):
		print(i,table[i], function(table[i].x,table[i].y))
	d +=1

print (iterN(table))