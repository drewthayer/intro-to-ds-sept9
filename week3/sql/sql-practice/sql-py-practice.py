import sqlite3

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_all_tasks(conn, query):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute(query)

    rows = cur.fetchall()

    for row in rows:
        print(row)

# specify SQL query


query = '''
SELECT cu.name as customer,
       cu.city,
       cu.state,
       pu.id as purchase_id,
       pu.date,
       pr.name as product_name,
       pr.id as product_id
FROM customers cu
JOIN purchases pu
ON cu.id = pu.custid
JOIN products pr
ON pu.prodid = pr.id
WHERE pu.date > '2017-01-00';
'''

# execute sql command on database
dbfile = 'sales.db'
conn = create_connection(dbfile)
select_all_tasks(conn, query)
