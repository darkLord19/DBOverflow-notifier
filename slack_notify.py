import requests, json
from secrets import Constants


def notify(table_list):
    headers = {"Content-type": "application/json"}

    # Nofify for every table found
    for table in table_list:
        msg = "***ATTENTION***\nOne of the auto incrementing fields in one of your database tables is about to run out of range of its datatype \nBelow is the details about that field:\n"
        msg = (
            msg
            + "Database Name: "
            + Constants.DB_NAME
            + "\nTable Name: "
            + table.table_name[0:]
            + "\nField Name: "
            + table.field_name[0:]
            + "\nData Type of Field: "
            + table.field_datatype[0:]
            + "\nMaximum Value data Type can hold: "
            + str(table.field_maxvalue)
            + "\nCurrent Value of Field: "
            + str(table.current_max)
        )

        data = {"text": msg}

        # Send message to slack using slack incoming webhook
        response = requests.post(
            Constants.WEBHOOK, data=json.dumps(data), headers=headers, verify=False
        )
        if response.status_code != 200:
            raise ValueError(
                "Request to slack returned an error %s, the response is:\n%s"
                % (response.status_code, response.text)
            )
