#!/usr/bin/env python
# coding: utf-8

# In[13]:


import os
import csv


# In[14]:


#path of csv
csvpath = os.path.join('Resources', 'election_data.csv')

voterid = []
county = []
candidate = []


# In[20]:


with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    #get total votes using len command and lists
    total_votes = len(list(csvreader))
    print(total_votes)
    
    for row in csvreader:
#         voterid.append(row[0])
#         county.append(row[1])
#         candidate.append(row[2])
        print(row)
#         if not row[2] in candidate:
#             candidate.append(row[2])
#     print(len(list(candidate)))
    


# In[ ]:





# In[ ]:




