import datetime as dt
import pymysql as pm
import echo.config as cf

# Блок подключения к БД MySQL
connection = pm.connect(host=cf.host,
                        user=cf.user,
                        password=cf.password,
                        db=cf.db)


def max_date_curs_nb():
    cur = connection.cursor()
    cur.execute("select max(date) from curs_nb")
    max_date_mysql = cur.fetchone()
    connection.commit()

    return max_date_mysql[0]


def curs_nb_one(max_date):
    cur = connection.cursor()
    cur.execute(f"select date, usd, eur, rub, uah, pln from curs_nb where date = '{max_date}'")
    data_curs = cur.fetchone()
    connection.commit()

    data = {
        'date': data_curs[0],
        'usd': data_curs[1],
        'eur': data_curs[2],
        'rub': data_curs[3],
        'uah': data_curs[4],
        'pln': data_curs[5],
    }

    return data


def curs_nb_all(cur_type, max_date_curs_nb, term):
    date_cur = (max_date_curs_nb - dt.timedelta(days=term))

    cur = connection.cursor()
    cur.execute(f"select date, {cur_type} from curs_nb where date > '{date_cur}'")
    data_curs = cur.fetchall()
    connection.commit()

    return data_curs


# print(curs_nb_all('usd', max_date_curs_nb(), 2))