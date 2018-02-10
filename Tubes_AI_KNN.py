import xlrd
import csv

def getData(filename, index_sheet):
	data = xlrd.open_workbook(filename)
	sheet = data.sheet_by_index(index_sheet)
	return sheet

trainfile = getData("train.xlsx",0)
testfile = getData("train_bener.xlsx",0)

def getEuclidean(baris1, baris2):
	temp = 0.0
	for i in range(0,len(baris1)):
		temp += (baris1[i]-baris2[i])**2
	return temp**0.5

def loaddata(file):
	temp = []
	for i in range(1, file.nrows):
		d = [file.cell_value(i,b) for b in range(0,file.ncols)]
		temp.append(d)
	return temp

datatrain = loaddata(trainfile)
datatest = loaddata(testfile)

def getNeigboar(datatest, datatrain, k):
	for test in datatest:
		nearest = []
		for train in datatrain:
			dist = getEuclidean(train[1:-1],test[1:])
			nearest.append(train+[dist])
		nearest = sorted(nearest,key = lambda x:x[len(x)-1], reverse = False)[:k] 
		kelases = [c[-2] for c in nearest]
		if kelases.count(1.0) > kelases.count(0.0):
			test.append(1)
			print "ID data",test[0],"diklasifikasikan : 1"
		else:
			test.append(0)
			print "ID data",test[0],"diklasifikasikan : 0"
	with open("Presentasi.csv","wb") as f:
		writer = csv.writer(f)
		writer.writerows(datatest)

p =  getNeigboar(datatest, datatrain, 7)