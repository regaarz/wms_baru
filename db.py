import psycopg2

db_name = "product"
db_user = "tasklist_user"
db_pw = "Arzula93."
db_host = "localhost"

def getProduct():
    conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_pw, host=db_host)
    cur = conn.cursor()
    cur.execute('SELECT product_id, product_name, category_product, rfid_tag FROM public."product_warehouse"')
    product_list = cur.fetchall()
    cur.close()
    conn.close()
    return product_list

def executeQuery(query, params=None):
    conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_pw, host=db_host)
    cur = conn.cursor()
    if params:
        cur.execute(query, params)
    else:
        cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()

def addProduct(product, category, rfid):
    query = 'INSERT INTO public."product_warehouse"(product_name, category_product, rfid_tag) VALUES (%s, %s, %s)'
    executeQuery(query, (product, category, rfid))

def updateProduct(product, id):
    query = 'UPDATE public."product_warehouse" SET product_name = %s WHERE product_id = %s'
    executeQuery(query, (product, id))

def deleteProduct(id):
    query = 'DELETE FROM public."product_warehouse" WHERE product_id = %s'
    executeQuery(query, (id,))
