import mysql.connector as conn
from secrets import Constants
from table_model import Table


def connect():
    mydb = conn.connect(
        host=Constants.DB_HOST,
        user=Constants.DB_USER,
        passwd=Constants.DB_PWD,
        database=Constants.DB_NAME,
    )
    return mydb


def get_auto_icr_fld(mydb):

    cursor = mydb.cursor()

    tables_with_auto_icr = []

    # http://code.openark.org/blog/mysql/checking-for-auto_increment-capacity-with-single-query
    sql = "SELECT TABLE_NAME, COLUMN_NAME, DATA_TYPE, \
                IF(LOCATE('unsigned', COLUMN_TYPE) > 0,1,0) AS IS_UNSIGNED, \
        (CASE DATA_TYPE \
            WHEN 'tinyint' THEN 255 \
            WHEN 'smallint' THEN 65535 \
            WHEN 'mediumint' THEN 16777215 \
            WHEN 'int' THEN 4294967295 \
            WHEN 'bigint' THEN 18446744073709551615 \
        END >> IF( LOCATE('unsigned', COLUMN_TYPE) > 0, 0, 1) ) AS MAX_VALUE, \
        AUTO_INCREMENT, \
        AUTO_INCREMENT / \
        (CASE DATA_TYPE \
            WHEN 'tinyint' THEN 255 \
            WHEN 'smallint' THEN 65535 \
            WHEN 'mediumint' THEN 16777215 \
            WHEN 'int' THEN 4294967295 \
            WHEN 'bigint' THEN 18446744073709551615 \
        END >> IF(LOCATE('unsigned', COLUMN_TYPE) > 0, 0, 1) ) AS AUTO_INCREMENT_RATIO \
        FROM INFORMATION_SCHEMA.COLUMNS \
            INNER JOIN INFORMATION_SCHEMA.TABLES USING (TABLE_SCHEMA, TABLE_NAME) \
        WHERE \
            TABLE_SCHEMA NOT IN ('mysql', 'INFORMATION_SCHEMA', 'performance_schema') \
        AND EXTRA='auto_increment' "

    cursor.execute(sql)

    for field in cursor:
        tables_with_auto_icr.append(
            Table(field[0], field[1], field[2], field[3], field[4], field[5])
        )

    return tables_with_auto_icr
