import random
import vk_api
import vk_api.bot_longpoll
# TODO Импорт токена лучше сделать с обработкой ошибки
#  try:
#     from settings import tok
#  except ImportError:
#     settings = None  # Для того, чтобы убрать замечание среду разработки.
#     print('Для работы бота...')
#     exit()
from _key import sicret_tocen

group_id = 199623812


class Bot:

    def __init__(self, group_id, token):
        self.group_id = group_id
        self.token = token

        self.vk = vk_api.VkApi(token=token)
        self.long_poller = vk_api.bot_longpoll.VkBotLongPoll(self.vk, self.group_id)
        self.api = self.vk.get_api()

    def run(self):
        for event in self.long_poller.listen():
            try:
                print(event)
                self.on_event(event)
            except Exception as exc:
                print(exc)

    def on_event(self, event):
        if event.type == vk_api.bot_longpoll.VkBotEventType.MESSAGE_NEW:
            # TODO При отправке сообщения вы сами генерируете random_id. В библиотеке для генерации идентификатора
            #  есть специальная функция vk_api.utils.get_random_id.
            #  Подробнее можете посмотреть в примерах библиотеки:
            #  https://github.com/python273/vk_api/blob/master/examples/messages_bot/user_messages_bot.py#L55
            self.api.messages.send(
                message=event.object.message['text'],
                random_id=random.randint(0, 2**10),
                peer_id=event.object.message['peer_id'],
            )
        else:
            print('Мы пока не умеем обрабатывать такие события.', event.type)


if __name__ == '__main__':
    bot = Bot(group_id, sicret_tocen)
    bot.run()
