#绘制点阵图
import matplotlib.pyplot as plt

fzx = []#辅助线绘制
fzy = []#辅助线绘制
chrgff1 = []
genegff1 = []
chrgff2 = []
genegff2 = []
chrlins1 = []
lon1 = []
chrlins2 = []
lon2 = []
def sq1gff():
	chrgff1 = []
	k = 0
	genegff1 = []
	for line in open("cc.gff",mode = 'r'):#
		x = line.strip("\n")
		x = x.split("\t")
		chrgff1.append(x[0])
		k = k + 1
		genegff1.append(k)
	return chrgff1,genegff1
def sq2gff():
	chrgff1 = []
	k = 0
	genegff1 = []
	for line in open("vv.12x.gff",mode = 'r'):#
		x = line.strip("\n")
		x = x.split("\t")
		chrgff2.append(x[0])
		k = k + 1
		genegff2.append(k)
	return chrgff2,genegff2
def sq1lens():
	chrlens1 = []
	lon1 = []
	for line in open("cc.lens",mode = 'r'):#
		x = line.strip("\n")
		x = x.split("\t")
		chrlins1.append(x[0])
		lon1.append(int(x[2]))
	return chrlins1,lon1
def sq2lens():
	chrlens2 = []
	lon2 = []
	for line in open("vv.12x.lens",mode = 'r'):#
		x = line.strip("\n")
		x = x.split("\t")
		chrlins2.append(x[0])
		lon2.append(int(x[2]))
	return chrlins2,lon2
chrgff1,genegff1 = sq1gff()
chrgff2,genegff2 = sq2gff()
chrlins1,lon1 = sq1lens()
chrlins2,lon2 = sq2lens()
#print(lon1)
#print(lon2)

k = 0
for i in range(len(lon2)):
	k = k + lon2[i]
	fzx.append(k)
k = 0
for i in range(len(lon1)):
	k = k + lon1[i]
	fzy.append(k)
#print(fzx)
#print(fzy)

gene1 = []
gene2 = []
gene3 = []
gene4 = []
for line in open("cc.vv.pep.1e-3.outfmt6",mode = 'r'):#
	x = line.strip("\n")
	x = x.split("\t")
	if (float(x[11]) < 1000 and float(x[11]) > 500):#设置筛选值
		a = int(x[0][2:-6])
		b = int(x[1][2:-6])
		gene1.append(fzy[a - 1] - lon1[a - 1] + int(x[0][5:]))
		gene2.append(fzx[b - 1] - lon2[b - 1] + int(x[1][5:]))
	if (float(x[11]) > 1000):#设置筛选值
		a = int(x[0][2:-6])
		b = int(x[1][2:-6])
		gene3.append(fzy[a - 1] - lon1[a - 1] + int(x[0][5:]))
		gene4.append(fzx[b - 1] - lon2[b - 1] + int(x[1][5:]))
#fzx=[1000,1500,2000,2500]#辅助线绘制
#print(max(max(gene1),max(gene3)))
#print(max(max(gene2),max(gene4)))

plt.figure(figsize = (10,10), dpi = 100)
plt.rcParams['figure.dpi'] = 100 #分辨率

#xmax = max(max(gene2),max(gene4))
#ymax = max(max(gene1),max(gene3))
plt.title("dotplot")
plt.xlim(xmax = max(genegff1),xmin = 0)
plt.ylim(ymax = max(genegff2),ymin = 0)
plt.xlabel("Coffea canephora")#物种名字
plt.ylabel("Vitis vinifera")#物种名字
plt.plot(gene1,gene2,'o',markersize = 0.3,color = "b")
plt.plot(gene3,gene4,'o',markersize = 0.3,color = "r")
plt.vlines(fzy, 0, max(genegff2), colors = 'cyan', label = '',linewidth = 0.5) #辅助线对应vv染色体
plt.hlines(fzx, 0, max(genegff1), colors = 'cyan', label = '',linewidth = 0.5) #辅助线对应cc染色体
plt.savefig('./plot.png', dpi=500,bbox_inches = 'tight')
#plt.show()
print ("ok！\nmake by Charles Lan")
#make by Charles Lan
#2020/5/25