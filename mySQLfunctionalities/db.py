from scrapers.scraper import Amazon
from dotenv import load_dotenv
import mysql.connector
import os


load_dotenv(f"{os.getcwd()}//environmentVariables//.env")


async def mysql_connections():
    """
    Establishes a connection to the MySQL database using environment variables.
    
    Returns:
        -cnx: MySQL connection object.
    """
    cnx = mysql.connector.connect(
        host = os.getenv('DB_HOST'),
        port = os.getenv('PORT'),
        user = os.getenv('DB_USERNAME'),
        password = os.getenv('DB_PASSWORD'),
        database = os.getenv('DATABASE'),
    )

    return cnx


async def verifyASIN(amazon_asin):
    """
    Checks if the given Amazon ASIN exists in the database.
    
    Args:
        -amazon_asin: Amazon ASIN of the product to check.
    
    Returns:
        -True if ASIN already exists in the database, else None.
    """
    cnx = await mysql_connections()
    cursor = cnx.cursor()
    sql_check_query = """SELECT * FROM asin_collections WHERE ASIN = %s"""
    params = (amazon_asin,)
    cursor.execute(sql_check_query, params)

    if cursor.fetchone():
        cnx.close()
        return True
    else:
        cnx.close()
        return


async def export_to_db(amazon_asin, user = None):
    """
    Exports data for a given Amazon ASIN/ISBN to the databse.
    
    Args:
        -amazon_asin: Amazon ASIN of the product to export.
        
    Returns:
        -Dictionary containing the data for the product if it's already existed in the database,
         else None if the data was successfully exported to the databse.
    """
    cnx = await mysql_connections()
    select_query = f"""SELECT * FROM asin_collections WHERE ASIN = '{amazon_asin}'"""
    cursor = cnx.cursor()
    if await verifyASIN(amazon_asin):
        cursor.execute(select_query)
        row = cursor.fetchone()

        columns = [col[0] for col in cursor.description]

        result_dict = dict(zip(columns, row))
        print(f"{amazon_asin} already exists.")
        cnx.close()
        return result_dict

    else:        
        amazon_datas = await Amazon().dataByAsin(amazon_asin)      

        insert_query = f"""INSERT INTO `asin_collections` (`ASIN`, `Name`, `Price`, `Rating`, `Rating count`, `Availability`, `Hyperlink`, `Image`, `Store`, `Store link`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        values = (amazon_asin, amazon_datas['Name'], amazon_datas['Price'], amazon_datas['Rating'], amazon_datas['Rating count'], amazon_datas['Availability'], amazon_datas['Hyperlink'], amazon_datas['Image'], amazon_datas['Store'], amazon_datas['Store link'])

        cursor.execute(insert_query, values)
        cnx.commit()

        cursor.execute(select_query)
        row = cursor.fetchone()

        columns = [col[0] for col in cursor.description]

        result_dict = dict(zip(columns, row))
        print(f"{amazon_asin} added to database.")
        
        cnx.close()
        return result_dict

