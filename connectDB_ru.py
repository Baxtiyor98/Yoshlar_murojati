from psycopg2 import connect

host = 'localhost'
username = 'postgres'
password = '!1234567A@'
db_name = 'for_yoshbot'

def get_region_ru():
    try:
        conn = connect(host=host, user=username, password=password, database=db_name)
        cursor = conn.cursor()
        sql = """
                SELECT region_id, region_name FROM viloyat_ru
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
def get_tuman_ru(reg_id):
    try:
        conn = connect(host=host, user=username, password=password, database=db_name)
        cursor = conn.cursor()
        sql = f"""
                SELECT region_id, tuman_id, tuman_name FROM tuman_ru WHERE region_id = {reg_id}
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
def get_menu_ru():
    try:
        conn = connect(host = host, user = username,password = password, database = db_name)
        cursor = conn.cursor()
        sql = f"""
        SELECT menu_id, menu_name FROM main_menu_ru
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
def get_normativ_menu_ru():
    try:
        conn = connect(host = host, user = username,password = password, database = db_name)
        cursor = conn.cursor()
        sql = f"""
        SELECT normativ_id, name FROM normativ_link1_ru 
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
def get_main_menu_link_ru(nm_id):
    try:
        conn = connect(host = host, user = username,password = password, database = db_name)
        cursor = conn.cursor()
        sql = f"""
        SELECT link FROM link_id_ru WHERE id = {nm_id}
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
def get_normativ_link_ru(link_id):
    try:
        conn = connect(host = host, user = username,password = password, database = db_name)
        cursor = conn.cursor()
        sql = f"""
        SELECT link FROM normativ_link2_ru WHERE link_id = {link_id}
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