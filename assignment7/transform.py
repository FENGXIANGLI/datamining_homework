import re
f = open('ecoli.data')
foutput = open('ecoli.processed.data','w+')
line = f.readline()
while line:
	datas = re.split(r'[" "]\s*',line)    
	print(datas)
	for i in range(0,len(datas) - 1):
		foutput.write(datas[i])
		foutput.write(',')
	foutput.write(datas[len(datas) - 1])
	line = f.readline()
