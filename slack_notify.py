import requests, json
from secrets import Constants


def notify(table_list):
    headers = {"Content-type": "application/json"}

    for table in table_list:
        msg = "***ATTENTION***\nOne of the auto incrementing fields in \
                one of your database tables is about to run out of range of its datatype\n \
                Below is the details about that field:\n"
        msg = (
            msg
            + "Database Name: "
            + Constants.DB_NAME.upper()
            + "\
            Table Name: "
            + table.table_name[0].upper()
            + "\
            Field Name: "
            + table.field_name[0].upper()
            + "\
            Data Type of Field: "
            + table.field_datatype[0].upper()
            + "\
            Maximum Value data Type can hold: "
            + table.field_maxvalue
            + "\
            Current Value of Field: "
            + table.current_max
        )

        data = {"text": msg}

    response = requests.post(
        Constants.WEBHOOK, data=json.dumps(data), headers=headers, verify=False
    )
    if response.status_code != 200:
        raise ValueError(
            "Request to slack returned an error %s, the response is:\n%s"
            % (response.status_code, response.text)
        )
