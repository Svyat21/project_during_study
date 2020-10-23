import vk_api
import vk_api.bot_longpoll
import vk_api.utils

try:
    from _key import sicret_tocen
except ImportError:
    settings = None
    print('Для работы бота импортируйте свой токен.')
    exit()


group_id = 199623812


class Bot:

    def __init__(self, id_group, token):
        self.group_id = id_group
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
            self.api.messages.send(
                message=event.object.message['text'],
                random_id=vk_api.utils.get_random_id(),
                peer_id=event.object.message['peer_id'],
            )
        else:
            print('Мы пока не умеем обрабатывать такие события.', event.type)


if __name__ == '__main__':
    bot = Bot(group_id, sicret_tocen)
    bot.run()
