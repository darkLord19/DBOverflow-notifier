# DBOverflow Notifier
This program checks for auto incrementing fileds of tables of database and notifies on slack if any of the fields is about to run out of its datatypes range. 

It uses Slack's Incoming Channel Webhooks to send messages to channel.

# Dependecies
```
pip install requests mysql-connector
```
Also you'll need mysql-server installed on your machine. Refer to your operating system's guide to install it.

# How to run?
Change database parameters in secrets.py to match your configuration. Change Slack incoming webhook to that of yours.

# python main.py
If there are any tables matching criteria then it will send message to slack channel in the following format:
```
***ATTENTION***
One of the auto incrementing fields in one of your database tables is about to run out of range of its datatype 
Below is the details about that field:
Database Name: test
Table Name: tasks
Field Name: task_id
Data Type of Field: smallint
Maximum Value data Type can hold: 32767
Current Value of Field: 31434
```
Currently it notifies when auto increment value is >=90% of range of that data type. You can change it by changing threshold value in secrets.py.
