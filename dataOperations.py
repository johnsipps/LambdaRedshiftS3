# -*- coding: utf-8 -*-
"""
*******************************************************************************
"""

import jdbConnection

#----------------------------------------------------
# Connect to the database
#----------------------------------------------------
con=jdbConnection.connect_to_db()

#Initialize
cur = con.cursor()

#----------------------------------------------------
#Declaration
#----------------------------------------------------

try:
    
    #----------------------------------------------------
 
    TargetTable		='jh_dim_customer' 

    queryCheckPrev="SELECT count(1) FROM svv_tables WHERE table_name=" + str(TargetTable)
    
    cur.execute(queryCheckPrev);
    
    rc = cur.fetchone()
    
    if rc[0]==1:
        print str(TargetTable)+" exists.."     
    else:    
        print str(TargetTable)+" does not exist.."




except Exception as e:
    print 'Exception Main', e
    cur.execute('rollback')    
    ErrorMsg=str.replace(str(e),"'","")
    #Truncating the Error message to 200
    ErrorMsgTrunc = (ErrorMsg[:200] + '..') if len(ErrorMsg) > 200 else ErrorMsg    

cur.close() 
con.close()
