import time

PARSER_START_TIME = time.time()


def if_hasvx(message):
  text = message.text
  #print(message)
  if message.date > PARSER_START_TIME and 'twitter.com' in text:
    return True
  else:
    return False

  #general channel parser
def channel_vxtwitterify(message, bot):
    link = message.text
    vxed = link.partition('twitter.com')[0] + 'vxtwitter.com' + link.partition(
        'twitter.com')[2]
    bot.edit_message_text(text=vxed,
                          chat_id=message.chat.id,
                          message_id=message.id,
                         )


#general group parser
def group_vxtwitterify(message, bot):
    text = message.text
    # #一些用户可能没有 last name
    # if message.from_user.last_name:
    #     user_last_name = " " + message.from_user.last_name
    # else:
    #     user_last_name = ""
    # user_display_name = message.from_user.first_name + user_last_name
    # user_id_clickable_link = '<a href="tg://user?id=' + str(
    #     message.from_user.id) + '">' + user_display_name + "</a>"
    vxed = text.partition('twitter.com')[0] + 'vxtwitter.com' + text.partition('twitter.com')[2]
    

    bot.reply_to(
        message=message,
        text=vxed,
        disable_notification=True,
    )
    #bot.delete_message(chat_id=message.chat.id, message_id=message.id)