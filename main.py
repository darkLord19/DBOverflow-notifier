from db_connection import *
from slack_notify import *


def about_to_run_out(current_field_max, field_maxvalue):
    if (100 * current_field_max) / field_maxvalue >= 90:
        return True
    return False


mydb = connect()
tables_with_auto_incr = get_auto_icr_fld(mydb)

for table in tables_with_auto_incr:
        print(table.table_name)

tables_having_fld_abt_run_out = []

for table in tables_with_auto_incr:
    if about_to_run_out(table.current_max, table.field_maxvalue):
        tables_having_fld_abt_run_out.append(table)

notify(tables_having_fld_abt_run_out)
