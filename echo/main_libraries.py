import telebot
import echo.config as conf
from telebot.types import ReplyKeyboardRemove

from echo.menu.global_menu import get_base_menu as global_menu
from echo.menu.button_menu_nb import get_base_menu as button_menu_nb
from echo.menu.button_inline_nb_stavki import get_inline_nb_stavki as button_nb_stavki
from echo.menu.button_nb_sr import get_menu_inline_stavka_sr as button_nb_sr
from echo.stavka_ref import get_sr as get_sr_1d
from echo.menu.button_inline_nb_stavki_back import get_menu_inline_stavka_sr_2 as button_nb_sr_2
from echo.nbrb.stavka_ref.stavka_ref_all import get_plot_sr_all as button_nb_sr_all
from echo.menu.button_inline_nb_news import get_inline_nb_news as button_nb_news
from echo.nbrb.news.news_nbrb import get_news as news_nb
from echo.nbrb.news.news_press import get_press as news_press
from echo.nbrb.news.news_analitica import get_ayalitic as news_analitic
from echo.nbrb.news.news_statistica import get_statistica as news_statistic