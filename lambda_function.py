# -*- coding: utf-8 -*-
"""
Created on Wed May 23 15:35:20 2018

@author: John
"""
import dataOperations   

def lambda_handler(event, context):
 
    print('start')
    dataOperations.main()
    print('end')
    
    return 'Hello from Lambda'
