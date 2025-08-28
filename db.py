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

def register(username,password,full_name,email,role):
    query = 'INSERT INTO public."users"(username,password_hash,full_name,email,role) VALUES (%s, %s,%s,%s,%s)'
    executeQuery(query, (username,password,full_name,email,role))

def login(username, password):
    conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_pw, host=db_host)
    cur = conn.cursor()
    query = 'SELECT * FROM public."users" WHERE username = %s AND password_hash = %s'
    cur.execute(query, (username, password))
    user = cur.fetchone()
    cur.close()
    conn.close()
    return user

def getAccount():
    conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_pw, host=db_host)
    cur = conn.cursor()
    cur.execute('SELECT user_id, full_name, email,username, role, status  FROM public."users"')
    account_list = cur.fetchall()
    cur.close()
    conn.close()
    return account_list

def getAccountById(user_id):
    conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_pw, host=db_host)
    cur = conn.cursor()
    cur.execute('SELECT user_id, full_name, email, username, password_hash, role, status FROM public."users" WHERE user_id = %s', (user_id,))
    account = cur.fetchone()
    cur.close()
    conn.close()
    return account


def updateAccounts(full_name, email,username, password, role, status, user_id):
    query = '''
        UPDATE public."users"
        SET full_name = %s, email = %s, username = %s, password_hash = %s,
            role = %s, status = %s, updated_at = NOW()
        WHERE user_id = %s
    '''
    executeQuery(query, (full_name, email, username, password, role, status, user_id))

def deleteAccount(user_id):
    query = 'DELETE FROM public."users" WHERE user_id = %s'
    executeQuery(query, (user_id,))