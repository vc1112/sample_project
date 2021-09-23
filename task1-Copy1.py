#!/usr/bin/env python
# coding: utf-8

# In[14]:


#code to access database table in the form of list

import pyodbc
server = 'internship-azure.database.windows.net'
database = 'myDB_task1'
username = 'vineetchoudhary@outlook.com@internship-azure'
password = '{Vineet@1011}'   
driver= '{ODBC Driver 13 for SQL Server}'
tagslist = []
with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM key_values")
        row = cursor.fetchone()
        while row:
            x = (str(row[0]) + " " + str(row[1]))
            x = x.split()
            tagslist.append(x)
            row = cursor.fetchone()


# In[38]:





# In[4]:


#final code

from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
import os
credential = AzureCliCredential()

subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"] = "d996b784-5ecf-4de8-8b53-15edeb828d0a"

resource_group = os.getenv("RESOURCE_GROUP_NAME", "Internship")

resource_client = ResourceManagementClient(credential, subscription_id)

group_list = resource_client.resource_groups.list()

# Show the groups in formatted output
column_width = 50

#print("Resource Group".ljust(column_width) + "tags")
#print("-" * (column_width * 2))

for group in list(group_list):
    a = group.location
    b = group.name
    #print(f"{group.name:<{column_width}}{group.tags}")
    if len(group.tags) == 0:
        resource_client.resource_groups.create_or_update(
            b,
            {
                "location" : a,
                "tags" : { tagslist[0][0]:tagslist[0][1],tagslist[1][0]:tagslist[1][1] }
            }
        )  
    if list(group.tags.values())==['']:
        for i in range(0,3):
            if tagslist[i][0]==list(group.tags.keys())[0]:
                resource_client.resource_groups.create_or_update(
                b,
                {
                    "location" : a,
                    "tags" : { tagslist[0][0]:tagslist[0][1] }
                }
            )  
        
        

