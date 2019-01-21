from db_connection import *
from slack_notify import *

mydb = connect()
tables_with_auto_incr = get_auto_icr_fld(mydb)

print(tables_with_auto_incr)
