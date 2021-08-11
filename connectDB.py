from psycopg2 import connect

host = 'localhost'
username = 'postgres'
password = '!1234567A@'
db_name = 'for_yoshbot'

def get_region():
    try:
        conn = connect(host=host, user=username, password=password, database=db_name)
        cursor = conn.cursor()
        sql = """
                SELECT region_id, region_name FROM viloyat
                ORDER BY region_id ASC
                """
        conn.autocommit = True
        cursor.execute(sql)
        res = []
        for i in cursor.fetchall():
            res.append(i)
        conn.close()
        return res

    except Exception as e:
        print('Error', e)
print(get_region())
def get_tuman(reg_id):
    try:
        conn = connect(host=host, user=username, password=password, database=db_name)
        cursor = conn.cursor()
        sql = f"""
                SELECT region_id, tuman_id, tuman_name FROM tuman WHERE region_id = {reg_id}
                
            """
        conn.autocommit = True
        cursor.execute(sql)
        res = []
        for i in cursor.fetchall():
            res.append(i)
        conn.close()
        return res

    except Exception as e:
        print('Error', e)
print(get_tuman(3))
def tuman_write(tum_id):
    try:
        conn = connect(host=host, user=username, password=password, database=db_name)
        cursor = conn.cursor()
        sql = f"""
                SELECT tuman_id, tuman_name FROM tuman WHERE tuman_id = {tum_id}

            """
        conn.autocommit = True
        cursor.execute(sql)
        res = []
        for i in cursor.fetchall():
            res.append(i)
        conn.close()
        return res

    except Exception as e:
        print('Error', e)
print((tuman_write(68))[0][0])
def get_tuman(reg_id):
    try:
        conn = connect(host=host, user=username, password=password, database=db_name)
        cursor = conn.cursor()
        sql = f"""
            SELECT region_id, tuman_id, tuman_name FROM tuman WHERE region_id = {reg_id}

             """
        conn.autocommit = True
        cursor.execute(sql)
        res = []
        for i in cursor.fetchall():
            res.append(i)
        conn.close()
        return res

    except Exception as e:
        print('Error', e)
def get_menu():
    try:
        conn = connect(host = host, user = username,password = password, database = db_name)
        cursor = conn.cursor()
        sql = f"""
        SELECT menu_id, menu_name FROM main_menu
        """
        conn.autocommit = True
        cursor.execute(sql)
        res = []
        for i in cursor.fetchall():
            res.append(i)
        conn.close()
        return res
    except Exception as e:
        print('Error',e)
def get_normativ_menu():
    try:
        conn = connect(host = host, user = username,password = password, database = db_name)
        cursor = conn.cursor()
        sql = f"""
        SELECT normativ_id, name FROM normativ_link1 
        """
        conn.autocommit = True
        cursor.execute(sql)
        res = []
        for i in cursor.fetchall():
            res.append(i)
        conn.close()
        return res
    except Exception as e:
        print('Error',e)
def get_main_menu_link(nm_id):
    try:
        conn = connect(host = host, user = username,password = password, database = db_name)
        cursor = conn.cursor()
        sql = f"""
        SELECT link FROM link_id WHERE id = {nm_id}
        """
        conn.autocommit = True
        cursor.execute(sql)
        res = []
        for i in cursor.fetchall():
            res = i
        conn.close()
        return res
    except Exception as e:
        print('Error',e)
def get_normativ_link(link_id):
    try:
        conn = connect(host = host, user = username,password = password, database = db_name)
        cursor = conn.cursor()
        sql = f"""
        SELECT link FROM normativ_link2
         WHERE link_id = {link_id}
         ORDER BY link_id ASC
        """
        conn.autocommit = True
        cursor.execute(sql)
        res = []
        for i in cursor.fetchall():
            res.append(i)
        conn.close()
        return res
    except Exception as e:
        print('Error',e)
def is_logged(tg_id):
    try:
        conn = connect(host=host, user=username, password=password, database=db_name)
        cursor = conn.cursor()
        sql = f"""
        SELECT * FROM joiner
        WHERE tg_id = {tg_id} 
        """
        conn.autocommit = True
        cursor.execute(sql)
        r = len(cursor.fetchall()) == 1
        conn.close()
        return r
    except Exception as e:
        print('Error', e)
def delete_acc(tg_id):
    try:
        conn = connect(host = host, user = username,password = password, database = db_name)
        cursor = conn.cursor()
        sql = f"""
        DELETE FROM public.joiner WHERE tg_id = {tg_id};
        """
        conn.autocommit = True
        cursor.execute(sql)
        conn.close()
    except Exception as e:
        print('Error',e)