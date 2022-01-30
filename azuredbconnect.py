# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 09:18:39 2022

@author: btindol
"""

import pyodbc
import pandas as pd

# Specifying the ODBC driver, server name, database, etc. directly
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=servername.database.windows.net;DATABASE=databasename;UID=blakeusername;PWD=blakepassword!!')


queryadventureworks = pd.read_sql("SELECT TOP (1000) * FROM [SalesLT].[Customer]",cnxn)

print(queryadventureworks)


