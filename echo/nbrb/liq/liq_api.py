import datetime as dt
import pymysql as pm
import echo.config as cf

# Блок подключения к БД MySQL
connection = pm.connect(host=cf.host,
                        user=cf.user,
                        password=cf.password,
                        db=cf.db)


# возвращаем данные на последнюю дату в MySQL
def get_liq_data_old():
    date = (dt.datetime.now().date() - dt.timedelta(days=30))
    cur = connection.cursor()
    cur.execute(f"select date as _date, liq as _liq, prt as _prt, psi as _psi from liq where date > '{date}' "
                f"ORDER BY date")
    data_mysql = cur.fetchall()
    connection.commit()

    return data_mysql[-1]


def get_liq_delta():
    date = (dt.datetime.now().date() - dt.timedelta(days=30))
    cur = connection.cursor()
    cur.execute(f"select date as _date, liq as _liq, prt as _prt, psi as _psi from liq where date > '{date}'"
                f" ORDER BY date")
    data_mysql = cur.fetchall()
    connection.commit()

    liq_delta = {
        'liq': int(float(data_mysql[-1][1]) - float(data_mysql[-2][1])),
        'prt': int(float(data_mysql[-1][2]) - float(data_mysql[-2][2])),
        'psi': int(float(data_mysql[-1][3]) - float(data_mysql[-2][3])),

    }
    return liq_delta
