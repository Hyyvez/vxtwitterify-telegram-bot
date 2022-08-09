import os
import telebot
import time
from telebot import types

TOKEN = os.environ["TOKEN"]

PARSER_START_TIME = time.time()

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def test(message):
    bot.send_message(
        message.chat.id,
        "This is a bot which can adding 'vx' prefix to a twitter link automagically. send me a twitter link, This bot will sent the twitter link with 'vx' prefix."
        + "\n\n发送推特链接，机器人会转换为带 vx 前缀的推特链接。")
    bot.send_message(
        message.chat.id,
        "  How to use: Just add the bot to a channel or group. (Also, due to limitations of the Telegram Bot API, bots in groups cannot see messages sent by another bot) (If required delete original messages, promote bot to admin and give it access of delete messages.) "
        +
        "\n\nIf required convert link across channel or group. send /menu for a list of commands"
        +
        "\n\n使用方法：将机器人添加至频道或群组即可。（另外，由于Telegram Bot API的限制，机器人在 群组 中无法转换另一个机器人发送的消息） （如果需要删除原消息，将bot设置为 admin 给予删除消息的权限即可）。"
        + "\n\n如果需要让bot跨频道或群组自动转换，发送 /menu 获取功能列表")


def if_hasvx(message):
    text = message.text
    # message.json['entities'][0]['type'] == url 这行代码#考虑到一些，发送一个包含推特的网址但是指向其他网址的乐子，这里不把这种链接进行转换
    if message.date > PARSER_START_TIME and 'https://twitter.com' in text and message.json[
            'entities'][0]['type'] == 'url':
        return True
    else:
        return False


#general channel parser
@bot.channel_post_handler(func=if_hasvx)
def channel_vxtwitterify(message):
    link = message.text
    vxed = link.partition('twitter.com')[0] + 'vxtwitter.com' + link.partition(
        'twitter.com')[2]
    #bot.send_message(message.chat.id, vxed)
    bot.send_message(chat_id=message.chat.id,
                     text=vxed,
                     disable_notification=True)
    bot.delete_message(chat_id=message.chat.id, message_id=message.id)


#general group parser
@bot.message_handler(func=if_hasvx)
def vxtwitterify(message):
    link = message.text
    #一些用户可能没有 last name
    if message.from_user.last_name:
        user_last_name = " " + message.from_user.last_name
    else:
        user_last_name = ""
    user_display_name = message.from_user.first_name + user_last_name
    user_id_clickable_link = '<a href="tg://user?id=' + str(
        message.from_user.id) + '">' + user_display_name + "</a>"
    vxed = link.partition('twitter.com')[0] + 'vxtwitter.com' + link.partition(
        'twitter.com')[2]
    text = user_id_clickable_link + ":\n" + vxed

    bot.send_message(
        chat_id=message.chat.id,
        text=text,
        parse_mode='HTML',
        disable_notification=True,
    )
    bot.delete_message(chat_id=message.chat.id, message_id=message.id)


"""@bot.message_handler(commands=["create"])
def create_parser(msg):
  

@bot.message_handler(commands=["delete"])
def delete_parser(msg):
  """
"""@bot.message_handler(commands=["close"])
def close_menu(msg):
  markup = types.ReplyKeyboardRemove(selective=False)
  bot.send_message(chat_id = msg.chat.id, text="done!",   reply_markup=markup)
"""


@bot.message_handler(commands=["menu"])
def send_menu_message(msg):
    markup = types.ReplyKeyboardMarkup(row_width=3)
    btn1 = types.KeyboardButton("/create")
    btn2 = types.KeyboardButton("/close")
    btn3 = types.KeyboardButton("/delete")
    markup.add(btn1, btn2, btn3)
    bot.send_message(
        chat_id=msg.chat.id,
        text=
        "create - parser twiitter link from a channel, send the message with 'vx' prefix to a channel or group    create - 从一个频道接收推特链接，发送对应的有vx前缀的链接到一个频道或群组",
        reply_markup=markup)


#bot.infinity_polling()
bot.polling()
