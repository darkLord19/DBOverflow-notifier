from db_connection import *
from slack_notify import *
from secrets import Constants


def about_to_run_out(current_field_max, field_maxvalue):
    if (100 * current_field_max) / field_maxvalue >= Constants.THRESHOLD:
        return True
    return False


mydb = connect()
tables_with_auto_incr = get_auto_icr_fld(mydb)

tables_having_fld_abt_run_out = []

if len(tables_with_auto_incr) > 0:
    for table in tables_with_auto_incr:
        if about_to_run_out(table.current_max, table.field_maxvalue):
            tables_having_fld_abt_run_out.append(table)
    if len(tables_having_fld_abt_run_out) > 0:
        notify(tables_having_fld_abt_run_out)
    else:
        print("Your Database is safe for now.")
else:
    print("Your Database doesn't have any auto incrimenting field.")
