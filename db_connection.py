import mysql.connector as conn
from secrets import Constants

mydb = conn.connect(
    host=Constants.DB_HOST,
    user=Constants.DB_USER,
    passwd=Constants.DB_PWD,
    database=Constants.DB_NAME,
)

print(mydb)

cursor = mydb.cursor()

cursor.execute("SHOW TABLES")

for x in cursor:
    sql = "SELECT COLUMN_NAME, DATA_TYPE, \
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

    for y in cursor:
        print(y)
