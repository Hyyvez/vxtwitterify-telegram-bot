"""if res.fetchone() != 1:
  #channel forward parser
  src_chat_id= "@artwilike"
  target_chat_id= "@artwilike"
  @bot.channel_post_handler(chat_id = src_chat_id,func=if_hasvx)
  def channel_forward_vxtwitterify(message):
    link = message.text
    vxed = link.partition('twitter.com')[0] + 'vxtwitter.com' + link.partition(
        'twitter.com')[2]
    #bot.send_message(message.chat.id, vxed)
    bot.send_message(target_chat_id, vxed)
    #如果是从当前频道获取的消息，则删除没有vx前缀的twitter链接
    if target_chat_id == "@" + message.chat.username:
        bot.delete_message(chat_id = message.chat.id, message_id = message.id)
else:
  print("database is empty")
"""
