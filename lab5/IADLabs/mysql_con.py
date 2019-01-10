import MySQLdb

if __name__ == '__main__':
	db = MySQLdb.connect(
	    host='localhost',
	    user='labuser',
	    passwd='',
	    db='lab6',
	    charset='utf8'
	)
	
	cur = db.cursor()
	
	cur.execute("INSERT INTO lab6_bullet (name,description) VALUES (%s, %s);", ('Продаётся машина','Старый пикап почти на ходу'))
	
	db.commit()
	
	cur.execute("SELECT * FROM lab6_bullet;")
	
	entries = cur.fetchall()
	
	for e in entries:
		print(e)
	
	cur.close()
	db.close()
