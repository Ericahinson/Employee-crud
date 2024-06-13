from mscon import connect_to_database

# Establish database connection
db = connect_to_database()
# cursor object c
c = db.cursor()
 
# delete statement for tblemployee
# which deletes employee Aishwarya having empid 3
employeetbl_delete = "DELETE FROM tblemployee WHERE empid=3"
 
# execute the delete statement and commit to the database
c.execute(employeetbl_delete)
db.commit()
 
# finally closing the database connection
db.close()