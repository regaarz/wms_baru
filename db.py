import psycopg2
db_name = "product"
db_user = "tasklist_user"
db_pw = "Arzula93."
db_host = "localhost"

def getProduct():
    conn = psycopg2.connect(dbname = db_name,user=db_user,password=db_pw,host = db_host)
    cur = conn.cursor()
    cur.execute('SELECT product_id, product_name, category_product,due_date, created_at, update_at, status FROM public."product_warehouse" ')
    product_list = cur.fetchall()
    cur.close
    conn.close
    return product_list

def addTask(product,category,date,status):
    conn = psycopg2.connect(dbname = db_name,user=db_user,password=db_pw,host = db_host)
    cur = conn.cursor()
    cur.execute('INSERT INTO public."product_warehouse"(product_name, category_product, created_at, update_at, due_date, status) VALUES (%s, %s, NOW(), NOW(), %s, %s)', (product,category,date,status))
    conn.commit() 
    cur.close
    conn.close