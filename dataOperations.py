# -*- coding: utf-8 -*-
"""
*******************************************************************************
"""

import jdbConnection
import jemailRS

def main():
	#----------------------------------------------------
	# Connect to the database
	#----------------------------------------------------
    
    con=jdbConnection.connect_to_db()
    #Initialize
    
    cur = con.cursor()
    
    try:
        TargetTableStr		="""'jh_dim_customer'""" 
        TargetTable 		="jh_dim_customer" 
        
        queryCheckPrev="SELECT count(1) FROM svv_tables WHERE table_name=" + TargetTableStr
        #print(queryCheckPrev)
        
        cur.execute(queryCheckPrev);
        
        rc = cur.fetchone()
        
        if rc[0]==1:
            print(TargetTable)
            queryExec="select count(1) from " + TargetTable
            cur.execute(queryExec);
            rc = cur.fetchone()
            jemailRS.main(str(TargetTable)+ " contains "+str(rc[0])+" records")
        else:    
            print(str(TargetTable)+" does not exist..")

    except Exception as e:
        print( 'Exception Main', e)    
        
    cur.close() 
    con.close()
    return "DB run success"