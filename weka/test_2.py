import tokenize
import re
import sys
import pymysql

f_2 = open('test_3.arff','w')

conn = pymysql.connect(host='localhost', user='root', password='',db='mesh', charset='utf8')
 
curs = conn.cursor()
query = "SELECT  SYMBOL FROM LUNG_GENES_TEST GROUP BY SYMBOL HAVING AVG(MAX_SCORE)>5 AND COUNT(*)>50"
curs.execute(query)
symbols = curs.fetchall()
query = "SELECT  DISTINCT PM_ID FROM LUNG_GENES_TEST"
curs.execute(query)
pm_ids = curs.fetchall()
f_2.write('@relation LUNG_CANCER.symbolic'+'\n\n')
for sym in symbols:
	f_2.write('@attribute '+sym[0]+' {0,1}\n')
f_2.write('@data\n')

thesis = []
for pm_id in pm_ids:
	del thesis[:] 
	query = "SELECT  SYMBOL FROM LUNG_GENES_TEST WHERE  PM_ID="+str(pm_id[0])+" AND MAX_SCORE > 5;" 
	curs.execute(query)
	match = curs.fetchall()
	#print match
	for sym in symbols:
		if sym in match:
			#print sym
			#print match
			thesis.append('1')
		else:
			thesis.append('?')
	outstr = ', '.join(thesis)
	#print outstr
	f_2.write(outstr+'\n')
conn.close()	


