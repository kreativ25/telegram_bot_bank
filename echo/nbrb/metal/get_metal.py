import datetime as dt
import pymysql as pm
import echo.config as cf

# Блок подключения к БД MySQL
connection = pm.connect(host=cf.host,
                        user=cf.user,
                        password=cf.password,
                        db=cf.db)


def get_metall_all(metal_name, term):
    date_cur = (dt.datetime.now().date() - dt.timedelta(days=term))

    con = connection.cursor()
    con.execute(f"select date, {metal_name} from metal "
                    f"WHERE date > '{date_cur}' ")
    all_bd = con.fetchall()
    connection.commit()

    return all_bd

# print(get_metall_all('gold', 10))
