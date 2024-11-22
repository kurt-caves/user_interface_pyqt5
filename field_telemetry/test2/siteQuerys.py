import mysql.connector
from mysql.connector import Error
import csvmaker

def loadsites():
    db_config = {
        'host' : 'scwmp-db.cfagskq8wo4y.us-east-2.rds.amazonaws.com',
        'user' : 'admin',
        'password': 'r7bvuOg7cx2frXJUDxOg',
        'port' : 3306,
        'database' : 'WX_DATA' 
''    }

    query = f"SELECT Name FROM Site;"

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    try:
        cursor.execute(query)
        recordList = cursor.fetchall()
    except Error as e:
        print("issue grabbing records:", e)
    
    return recordList

def sitequery(site):
    db_config = {
        'host' : 'scwmp-db.cfagskq8wo4y.us-east-2.rds.amazonaws.com',
        'user' : 'admin',
        'password': 'r7bvuOg7cx2frXJUDxOg',
        'port' : 3306,
        'database' : 'WX_DATA' 
''    }

    site_query = f"SELECT * FROM Site WHERE Site.Name = %s;"
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    try:
        cursor.execute(site_query,(site,))
        record = cursor.fetchall()
        # print(record)
    except Error as e:
        print("issue connection to db", e)
    
    return record

def filetype(site,startdate,enddate):
    db_config = {
        'host': 'scwmp-db.cfagskq8wo4y.us-east-2.rds.amazonaws.com',
        'user': 'admin',
        'password': 'r7bvuOg7cx2frXJUDxOg',
        'port': 3306,
        'database': 'WX_DATA'
    }

    # Prepare the SQL query with placeholders
    site_query = """
    SELECT DISTINCT SUBSTRING_INDEX(SiteInfo, '_', -1) AS FileType
    FROM `Data`
    WHERE TimeStamp BETWEEN %s AND %s
      AND SiteInfo LIKE %s;
    """

    # debug
    # site_query = """SELECT DISTINCT SUBSTRING_INDEX(SiteInfo, '_', -1) AS FileType FROM `Data` WHERE SiteInfo LIKE %s;"""

    # Define the parameters for the query
    start_date = startdate
    end_date = enddate
    site_param = f"%{site}%"  # Add wildcards for the LIKE operator

    try:
        # Establish the database connection
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Execute the query with parameters
        cursor.execute(site_query, (start_date, end_date, site_param))
        #debug
        # cursor.execute(site_query,(site_param,))

        # Fetch all records
        records = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        # Return the records
        print("From method call:", records)
        return records

    except Error as e:
        print("Issue connecting to the database:", e)
        return None

# want to make a csv file based upon the file type, site, start date and end date
def datadownload(site, start_date, end_date, filetype):
    print("inside datadownload")
    print("start date:",start_date)
    print("end date: ", end_date)
    print("site: ", site)
    print("filetype: ", filetype)

    db_config = {
        'host': 'scwmp-db.cfagskq8wo4y.us-east-2.rds.amazonaws.com',
        'user': 'admin',
        'password': 'r7bvuOg7cx2frXJUDxOg',
        'port': 3306,
        'database': 'WX_DATA'
    }

    site_query = """
   SELECT * 
   FROM `Data` 
   WHERE SiteInfo LIKE %s 
   AND SiteInfo LIKE %s 
   AND TimeStamp BETWEEN %s AND %s;
    """

    # Define the parameters for the query
    site_param = f"%_{site}_%"  # Add wildcards for the LIKE operator
    file_param = f"%_{filetype}%"

    try:
        # Establish the database connection
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Execute the query with parameters
        cursor.execute(site_query, (site_param, file_param, start_date, end_date))

        # Fetch all records
        values_tup = cursor.fetchall()
        

        # Close the cursor and connection
        cursor.close()
        connection.close()


    except Error as e:
        print("Issue connecting to the database:", e)
        return None

    # want to get the column names so we can use them for making the csv
    column_names = []
    for description in cursor.description:
        column_names.append(description[0])

    value = csvmaker.makecsv(column_names, values_tup)
    return value