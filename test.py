#import mysql.connector

# INSERT INTO vital_signs ( patient_id, oxigen, heart_rate, temperature, resp_rate, weight,height,day_taken, year_taken, month_taken, hour_taken)
# VALUES (1003066575, 90, 180, 30, 120, 180, 90, 12, 2022, 5, 11);
# establishing the connection
# Preparing SQL query to INSERT a record into the database.
#insert_stmt = (
  #          "INSERT INTO vital_signs ( patient_id, oxigen, heart_rate, temperature, resp_rate, weight, height, day_taken, year_taken, month_taken, hour_taken) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
 #       )
#data = (1003066575, 100, 23, 120, 180, 90, 12, 2022, 5, 11)

import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='healthy',
                                         user='root',
                                         password='kodokushi')

    mySql_insert_query = """INSERT INTO vital_signs ( patient_id, oxigen, heart_rate, temperature, resp_rate, weight, height, day_taken, year_taken, month_taken, hour_taken)
                           VALUES 
                           (1003066575, 97, 120, 23, 180, 90, 50, 12, 2022, 6, 12) """

    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Laptop table")
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into Laptop table {}".format(error))

finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")
































