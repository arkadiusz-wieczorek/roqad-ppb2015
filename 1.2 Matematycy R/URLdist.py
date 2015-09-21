import fileinput

lista = []
devices =[]

# trzeba wczytać odpowiedni csv
dataset=open('.\listaURL.csv').readlines() 
for row in dataset:
	device_id = row[0:row.find(',')]
	list = row[row.find('[')+1:row.find(']')]
	list = list.replace("'", "")
	list = list.replace(" ", "")
	sp = list.split(',')
	lista.append(sp)
	devices.append(device_id)
pass

def devlistnum( dev_id ):
	for i in range(1,len(devices)-1):
		if devices[i] == dev_id:
			return i

def inter(a,b):
	c=[]
	for e in a:
		if e in b:
			c.append(e)
	return c

# ogległość między urlami (z powtórzeniami)
def dist(a,b):
	l1 = lista[devlistnum(a)] 
	l2 = lista[devlistnum(b)] 
	x = len(inter(l1,l2))/float(min(len(l1),len(l2)))
	return 1-x

def unique(l):
	nowa=[]
	for c in set(l):
		nowa.append(c)
	return nowa

# ogległość między unikalnymi urlami
def distunique(a,b):
	l1 = unique(lista[devlistnum(a)]) 
	l2 = unique(lista[devlistnum(b)]) 
	x = len(inter(l1,l2))/float(min(len(l1),len(l2)))
	return 1-x

# wywołuje się wpisując dev_id
print dist('dev_100019','dev_100020')
print distunique('dev_100019','dev_100020')
