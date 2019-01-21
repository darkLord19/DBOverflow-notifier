import requests, json
from secrets import Constants

headers = {"Content-type": "application/json"}

data = {"text": "Sent using python code!"}

response = requests.post(
    Constants.WEBHOOK,
    data=json.dumps(data),
    headers={"Content-Type": "application/json"},
    verify=False,
)
if response.status_code != 200:
    raise ValueError(
        "Request to slack returned an error %s, the response is:\n%s"
        % (response.status_code, response.text)
    )
