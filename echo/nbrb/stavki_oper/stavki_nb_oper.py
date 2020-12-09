import datetime as dt
import pymysql as pm
import echo.config as cf


data_stavki_mysql = []
kredit_over_stavki_mysql = []
depozit_over_stavki_mysql = []
dabl_kredit_mysql = []


def get_data_st():
    connection = pm.connect(host=cf.host,
                            user=cf.user,
                            password=cf.password,
                            db=cf.db)

    cur = connection.cursor()
    cur.execute(
        'select data_stavki as ds, kredit_over as ko, depozit_over as do, dabl_kredit as dk from stavki_nb_oper')
    data_mysql = cur.fetchall()

    return data_mysql


# выбираем все даты из MySQL
def get_data_stavki_all():
    for i in get_data_st():
        data_stavki_mysql_prepare = dt.datetime.strftime(i[0], '%Y.%m.%d')
        data_stavki_mysql.append(data_stavki_mysql_prepare)

    return data_stavki_mysql


# выбираем последнюю дату изменения ставок в MySQL
def get_data_stavki_one():
    data_stavki_one = get_data_stavki_all()
    data_stavki_one = data_stavki_one[-1]

    return data_stavki_one


# список ставок по кредиту овернайт
def get_kredit_over_stavki():
    for i in get_data_st():
        kredit_over_stavki_mysql.append(i[1])

    return kredit_over_stavki_mysql


# выбираем последнюю ставку по кредиту овернайт
def get_kredit_over_stavki_one():
    kredit_over_stavki_one = get_kredit_over_stavki()
    kredit_over_stavki_one = kredit_over_stavki_one[-1]

    return kredit_over_stavki_one


# список ставок по депозиту овернайт
def get_depozit_over_stavki():
    for i in get_data_st():
        depozit_over_stavki_mysql.append(i[2])

    return depozit_over_stavki_mysql


# выбираем последнюю ставку по депозиту овернайт
def get_depozit_over_stavki_one():
    depozit_over_stavki_one = get_depozit_over_stavki()
    depozit_over_stavki_one = depozit_over_stavki_one[-1]

    return depozit_over_stavki_one


# список ставок по двусторонним кредитам
def get_dabl_kredit_stavki():
    for i in get_data_st():
        dabl_kredit_mysql.append(i[3])

    return dabl_kredit_mysql


# выбираем последнюю ставку по двусторонним кредитам
def get_dabl_kredit_stavki_one():
    dabl_kredit_stavki_one = get_dabl_kredit_stavki()
    dabl_kredit_stavki_one = dabl_kredit_stavki_one[-1]

    return dabl_kredit_stavki_one
