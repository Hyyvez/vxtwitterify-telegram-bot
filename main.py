import os
import telebot
from telebot import types
from keep_alive import keep_alive
from local_parser import if_hasvx, channel_vxtwitterify

TOKEN = os.environ["TOKEN"]
bot = telebot.TeleBot(TOKEN)


#general channel parser
@bot.channel_post_handler(func=if_hasvx)
def channel_(message):
  channel_vxtwitterify(message,bot)
"""#general group parser
vxit = types.BotCommand("vxit","reply you with a vxed prefix twitter link of last but 3 twitter links messaages before this ")
my_commands_list = [vxit]
bot.set_my_commands(commands=my_commands_list)
@bot.message_handler(commands=my_commands_list,timeout=120)
def group_(message):
  group_vxtwitterify(message,bot)
"""

@bot.message_handler(commands=["start"])
def test(message):
    bot.reply_to(
        message=message,
      text="How to use: Just add the bot to a channel, the bot will automatically edit the message, prefixing the twitter link with vx."
        +
        "\n\nIf required forward vxed message to a group from channel. use /menu for a list of commands"
        +
        "\n\n使用方法：将机器人添加至任意 channel 即可。机器人会自动编辑消息，在推特链接前加上 vx 前缀。"
        + "\n\n如果需要从 channel 转发加 vx 前缀后的信息到群组，发送 /menu 获取功能列表。")


@bot.message_handler(commands=["menu"])
def send_menu_message(msg):
    markup = types.ReplyKeyboardMarkup(row_width=3)
    btn1 = types.KeyboardButton("/create_route")
    btn2 = types.KeyboardButton("/my_route")
    btn3 = types.KeyboardButton("/FAQ")
    btn3 = types.KeyboardButton("/delete")
    btn4 = types.KeyboardButton("/close")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(
        chat_id=msg.chat.id,
        text=
        "create_route - parser twiitter link from a channel, send the message with 'vx' prefix to a channel or group    create_route - 从一个频道接收推特链接，发送对应的有vx前缀的链接到一个频道或群组",
        reply_markup=markup)



"""@bot.message_handler(commands=["create_route"])
def create_parser(msg):
  

@bot.message_handler(commands=["FAQ"])
def FAQ(msg):
bot.send_message(
        message.chat.id,
        "Q-为什么机器人不转换另一个机器人的消息？\n
         A-由于 Telegram Bot API 的限制，机器人在 group 中无法转换另一个机器人发送的消息。不过可以将两个机器人加入同一个 channel，然后将此机器人源频道设置为两个机器人所在的 channel，目标设置为要转发到的群组。\n
        所以该机器人在 github 上开源 https://github.com/Hyyvez/vxtwitterify-telegram-bot（        
        + "\n\n如果需要让bot跨频道或群组自动转换，发送 /menu 获取功能列表")


@bot.message_handler(commands=["delete"])
def delete_parser(msg):
  """
"""@bot.message_handler(commands=["close"])
def close_menu(msg):
  markup = types.ReplyKeyboardRemove(selective=False)
  bot.send_message(chat_id = msg.chat.id, text="done!",   reply_markup=markup)
"""




keep_alive()

bot.infinity_polling()
#bot.polling()
