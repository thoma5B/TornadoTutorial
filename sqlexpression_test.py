from sql_metadata import engine, page_table

print "\nInserting\n"

connection = engine.connect()
ins = page_table.insert(
    values=dict(name=u'test', title=u'Test Page', content=u'Some content!')
)
print ins
result = connection.execute(ins)
print result

print "### \nSelecting\n ####"

from sqlalchemy.sql import select
from sqlalchemy.sql import and_, or_, not_

s = select(
		[page_table],
		and_(page_table.c.id <= 10, page_table.c.name.like(u't%')),
	).order_by(
		page_table.c.title.desc(), 
		page_table.c.id,
	)
result = connection.execute(s)
print result.fetchall()

connection.close()