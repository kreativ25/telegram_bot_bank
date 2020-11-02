import telebot
import echo.config as conf
from telebot.types import ReplyKeyboardRemove

from echo.menu.global_menu import get_base_menu as global_menu
from echo.menu.button_menu_nb import get_base_menu as button_menu_nb
from echo.menu.button_inline_nb_stavki import get_inline_nb_stavki as button_nb_stavki
from echo.menu.button_nb_sr import get_menu_inline_stavka_sr as button_nb_sr
from echo.nbrb.stavka_ref.stavka_ref_one import get_sr as get_sr_1d
from echo.menu.button_inline_nb_stavki_back import get_menu_inline_stavka_sr_2 as button_nb_sr_2
from echo.nbrb.stavka_ref.stavka_ref_all import get_plot_sr_all as button_nb_sr_all
from echo.menu.button_inline_nb_news import get_inline_nb_news as button_nb_news
from echo.nbrb.news.news_nbrb import get_news as news_nb
from echo.nbrb.news.news_press import get_press as news_press
from echo.nbrb.news.news_analitica import get_ayalitic as news_analitic
from echo.nbrb.news.news_statistica import get_statistica as news_statistic
from echo.nbrb.stavki_oper.stavki_oper_nb_one import get_stavki_oper_one as stavki_oper_nb_one
from echo.nbrb.stavki_oper.stavki_oper_nb_all import get_plot_stavki_nb_all as stavki_oper_nb_all
from echo.menu.button_inline_stavki_oper_nb import get_menu_inline_stavki_oper_nb as get_menu_inline_stavki_oper_nb
from echo.menu.button_inline_kurs_nb_global import get_menu_inline_kurs_nb_global as kurs_nb_global
from echo.nbrb.kurs.kurs_nb_one import get_kurs_nb_one as kurs_nb_one
from echo.menu.button_inline_kurs_nb_cur_all import get_menu_inline_kurs_nb_cur_all as kurs_nb_cur_all
from echo.nbrb.kurs.kurs_nb_usd_all import get_kurs_nb_usd_all
from echo.nbrb.kurs.kurs_nb_eur_all import get_kurs_nb_eur_all
from echo.nbrb.kurs.kurs_nb_rub_all import get_kurs_nb_rub_all
from echo.nbrb.kurs.kurs_nb_pln_all import get_kurs_nb_pln_all
from echo.menu.button_inline_metal_nb_global import get_menu_inline_metal_nb_global as menu_metal
from echo.menu.button_inline_metal_nb_name_price import get_menu_inline_metal_nb_price_all as menu_metal_price
from echo.menu.button_inline_metal_nb_name_ingot import get_menu_inline_metal_nb_ignot_all as menu_metal_ignot

from echo.nbrb.metal.nb_gold_price_all import get_nb_gold_price_all as nb_gold_price
from echo.nbrb.metal.nb_platinum_price_all import get_nb_platinum_price_all as nb_platinum_price
from echo.nbrb.metal.nb_silver_price_all import get_nb_silver_price_all as nb_silver_price
from echo.nbrb.metal.nb_palladium_price_all import get_nb_palladium_price_all as nb_palladium_price

from echo.nbrb.metal.nb_gold_ignot import get_gold_ignot
from echo.nbrb.metal.nb_silver_ignot import get_silver_ignot
from echo.nbrb.metal.nb_platinum_ignot import get_platinum_ignot