from telegram.ext import Updater, CommandHandler
from telegram import ParseMode
import os
import strings
import time_updater
import page_parser as pp
import config as cfg

updater = Updater(token=cfg.TOKEN)
dispatcher = updater.dispatcher
time_updater.run()


def hello(bot, update):
    update.message.reply_text(strings.hello_mes)


def send_stats(bot, update):
    raw_stats = pp.get_current_stats()
    stats = cfg.ABIT_LIST_URL + '\n'
    tab4 = "\t\t\t\t"
    tab8 = tab4 * 2
    for stat in raw_stats:
        stats += "Конкурсная группа: {0}\n" \
                 "Кол. мест: {1}\n" \
                 "Заявления\n" \
                 "%sВсего: {2}\n" \
                 "%sБВИ: {3}\n" \
                 "%sПо номерам\n" \
                 "%s1: {4}\n" \
                 "%s2: {5}\n" \
                 "%s3: {6}\n\n".format(*stat) % (tab4, tab4, tab4, tab8, tab8, tab8)
    update.message.reply_text(stats)


def send_faq(bot, update):
    update.message.reply_text(strings.faq, parse_mode=ParseMode.MARKDOWN)


def format_abit_info(abit):
    tab4 = "\t\t\t\t"
    abit = ['-' if el == '' else el for el in abit]
    return "№ п/п: {0}\n" \
           "Номер заявления: {1}\n" \
           "ФИО: {2}\n" \
           "Вступительные испытания\n" \
           "%sВид: {3}\n" \
           "%sМатематика: {4}\n" \
           "%sРусский язык: {5}\n" \
           "%sИнформатика: {6}\n" \
           "%sЕГЭ + ИД: {7}\n" \
           "%sЕГЭ: {8}\n" \
           "%sИД: {9}\n" \
           "Наличие оригинала документов: {10}\n" \
           "Наличие согласия на зачисление: {11}\n" \
           "Преимущественное право: {12}\n" \
           "Олимпиада: {13}\n" \
           "Статус: {14}\n\n".format(*abit) % (tab4, tab4, tab4, tab4, tab4, tab4, tab4)


def search(bot, update, args):
    if len(args) == 0:
        update.message.reply_text(strings.tip_mes)
        return
    abits = pp.get_abit(args)
    if len(abits) == 0:
        update.message.reply_text(strings.not_found_mes)
        return
    if len(abits) > 10:
        update.message.reply_text(strings.too_many_abits)
        return
    result_text = ""
    for abit in abits:
        result_text += format_abit_info(abit)
    update.message.reply_text(result_text)


def links(bot, update):
    update.message.reply_text(strings.links_mes)


def new(bot, update):
    new_abits = pp.get_new_abits()
    if len(new_abits) == 0:
        update.message.reply_text(strings.no_abits)
        return
    n = len(new_abits)
    reply_mes = "*На сегодня {0} новых заявок на поступление БВИ*\n".format(n)
    if n % 10 == 1 and n != 11:
        reply_mes = "*На сегодня {0} новая заявка на поступление БВИ*\n".format(n)
    elif (2 <= n % 10 <= 4) and n != 12 and n != 13 and n != 14:
        reply_mes = "*На сегодня {0} новые заявки на поступление БВИ*\n".format(n)
    for i in range(len(new_abits)):
        reply_mes += format_abit_info(new_abits[i])
        if i % 10 == 9:
            update.message.reply_text(reply_mes, parse_mode=ParseMode.MARKDOWN)
            reply_mes = ""
    update.message.reply_text(reply_mes, parse_mode=ParseMode.MARKDOWN)

dispatcher.add_handler(CommandHandler('start', hello))
dispatcher.add_handler(CommandHandler('help', hello))
dispatcher.add_handler(CommandHandler('stats', send_stats))
dispatcher.add_handler(CommandHandler('new', new))
dispatcher.add_handler(CommandHandler('search', search, pass_args=True))
dispatcher.add_handler(CommandHandler('links', links))
dispatcher.add_handler(CommandHandler('faq', send_faq))

updater.start_webhook(listen="0.0.0.0",
                      port=int(os.environ.get('PORT', '5000')),
                      url_path=cfg.TOKEN)
updater.bot.set_webhook(cfg.HOST + cfg.TOKEN)
updater.idle()

