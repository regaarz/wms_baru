import psycopg2
db_name = "product"
db_user = "tasklist_user"
db_pw = "Arzula93."
db_host = "localhost"

def getProduct():
    conn = psycopg2.connect(dbname = db_name,user=db_user,password=db_pw,host = db_host)
    cur = conn.cursor()
    cur.execute('SELECT product_id, category_product,due_date, status FROM public."product" ')
    product_list = cur.fetchall()
    cur.close
    conn.close
    return product_list