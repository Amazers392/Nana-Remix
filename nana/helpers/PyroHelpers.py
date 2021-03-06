from pyrogram import Message, User
from inspect import getfullargspec


def ReplyCheck(message: Message):
    reply_id = None

    if message.reply_to_message:
        reply_id = message.reply_to_message.message_id

    elif not message.from_user.is_self:
        reply_id = message.message_id

    return reply_id
  

def GetUserMentionable(user: User):
    "Get mentionable text of a user."
    if user.username:
        username = "@{}".format(user.username)
    else:
        if user.last_name:
            name_string = "{} {}".format(user.first_name, user.last_name)
        else:
            name_string = "{}".format(user.first_name)

        username = "<a href='tg://user?id={}'>{}</a>".format(user.id, name_string)

    return username


async def msg(message: Message, **kwargs):
    func = message.edit if message.from_user.is_self else message.reply
    spec = getfullargspec(func).args
    await func(**{k: v for k, v in kwargs.items() if k in spec})