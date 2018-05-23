# -*- coding: utf-8 -*-
"""
*******************************************************************************
"""

import jdbConnection
import jemailRS

def dataOperations():
	#----------------------------------------------------
	# Connect to the database
	#----------------------------------------------------
    
    con=jdbConnection.connect_to_db()
    #Initialize
    
    cur = con.cursor()
    
    try:
        TargetTable		="""'jh_dim_customer'""" 
        
        queryCheckPrev="SELECT count(1) FROM svv_tables WHERE table_name=" + TargetTable
        #print(queryCheckPrev)
        
        cur.execute(queryCheckPrev);
        
        rc = cur.fetchone()
        
        if rc[0]==1:
            jemailRS.main(str(TargetTable))
        else:    
            print(str(TargetTable)+" does not exist..")

    except Exception as e:
        print( 'Exception Main', e)    
        
    cur.close() 
    con.close()
    return "DB run success"