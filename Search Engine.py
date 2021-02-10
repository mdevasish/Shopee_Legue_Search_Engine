# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 15:39:48 2020

@author: mdevasish
"""

def input_data(n_tcs,n_entries,n_queries):
    entries = []
    queries = []
    for each in range(n_tcs):
        for entry in range(n_entries):
            x = input('Enter the entries of the db:').lower()
            entries.append(x)
        for query in range(n_queries):
            x = input('Enter the queries to the db:').lower()
            queries.append(x)
    return entries,queries
    
def cal_response(entries,queries):
    for i,query in enumerate(queries):
        print(query)
        count = 0
        length = len(query.split(' '))
        if length > 1 :
            for o,entry in enumerate(entries):
                if query in entry:
                    count = count+1
        else:
            for o,entry in enumerate(entries):
                final = entry.split(' ')
                if query in final:
                    count = count+1
        print(count)
    return None

    
if __name__ =="__main__":
    x = int(input('Enter the number of test cases:'))
    n,q = input('Enter the number of entries and queries').split(' ')
    n,q = int(n),int(q)
    if (x == 0) or (n == 0) or (q == 0):
        raise Exception('I am sorry, Number of Test cases/entries/queries can be zero')
    entries,queries = input_data(x,n,q)
    k = cal_response(entries,queries)
    
