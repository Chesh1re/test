>>> import MySQLdb
>>> conn = MySQLdb.connect(user='root',passwd='admin',host='127.0.0.1')
>>> conn.select_db('week')

>>> cur= conn.cursor()

>>> cur.execute("insert into new_table values('tom','002')")
>>> sql = "insert into new_table values(%s,%s)"
>>> cur.execute(sql,('tomy','003'))
>>> cur.execute("select * from new_table")
executemany(sql,[(),(),()])
delete from ... where
update ... set name='' where ..
>>> cur.fetchone()
>>> cur.fetchmany()
()
>>> cur.scroll(0,"absolute")
>>> cur.fetchmany()
(('amy', '001'),)
>>> cur.fetchmany(3)
(('tom', '002'), ('tomy', '003'))
>>> conn.commit()
>>> cur.close()
>>> conn.close()

