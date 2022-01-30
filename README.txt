# THIS TUTORIAL IS TO LEARN HOW TO USE AZURE SQL DATABASE WITH PYTHON 
#########################################################################################################
##############################################################################################################
# Instructions
################
1) Azure portal home --> create resources
2) sql database
3) make resource group, db name and create new server
4) configure compute + storage (configure database)
5) under service tier click basic and make maximum gb size 2 4 dollars a month 
6) in additional settings click sample database.. adventureworks 
7) create database and wait
8) go to resource db1 ((if click server name you are going to server level (server can have 1 or more databases)))
9) go to overview then firewall settings so outside users can access db 
10) add our ip address to firewall by clicking add client ip
11) go  to preview database go to query editor on left pane and login with pass
12) you should be able to see the database
13) select top 10 and go to ide and use string to pull data from IDE

https://gist.github.com/timmyreilly/f4a351eda5dd45aa9d56411d27573d7c

################################################
# Other sql related resources
################
# REFERENCES
################################################
# https://docs.microsoft.com/en-us/azure/mysql/connect-python?fbclid=IwAR16iuj_qCcRxgi-t3YLN4gzrCa_4aaRANSVGYOi7x884BxV5u8ezEKfEgM
# https://docs.microsoft.com/en-us/azure/mysql/quickstart-create-mysql-server-database-using-azure-portal
# https://www.udemy.com/course/70532-azure/learn/lecture/20554556#overview
# https://docs.microsoft.com/en-us/azure/azure-sql/database/design-first-database-tutorial
# https://github.com/mkleehammer/pyodbc/wiki/Getting-started
# https://gist.github.com/timmyreilly/f4a351eda5dd45aa9d56411d27573d7c?fbclid=IwAR2GOzVLkE0qTsAuHBaxk2MR5fXndyEmyVImYoV1zMHClGfIEQYSAPEpFy0
