import datetime as dt
import pymysql as pm
import echo.config as cf

# Блок подключения к БД MySQL
connection = pm.connect(host=cf.host,
                        user=cf.user,
                        password=cf.password,
                        db=cf.db)

date_liq_mysql = []
liq_mysql = []
prt_mysql = []
psi_mysql = []


# выбираем все даты из MySQL
def get_date_liq_all():
    date = (dt.datetime.now().date() - dt.timedelta(days=360))
    cur = connection.cursor()
    cur.execute(f"select date as _date from liq where date > '{date}' ORDER BY date")
    data_mysql = cur.fetchall()
    connection.commit()

    for i in data_mysql:
        date_liq_mysql_prepare = dt.datetime.strptime(dt.datetime.strftime(i[0], '%Y.%m.%d'), '%Y.%m.%d').date()
        date_liq_mysql.append(date_liq_mysql_prepare)

    return date_liq_mysql


# список значений ликвидности
def get_liq_all():
    date = (dt.datetime.now().date() - dt.timedelta(days=360))
    cur = connection.cursor()
    cur.execute(f"select liq as _liq from liq where date > '{date}' ORDER BY date")
    data_mysql = cur.fetchall()
    connection.commit()

    for i in data_mysql:
        liq_mysql.append(i[0])

    return liq_mysql


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
