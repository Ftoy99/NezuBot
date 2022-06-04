import discord
from settings.settings import settingsManager


class Nezu(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return

        if self.user in message.mentions:
            self.handle_message(message)

    def handle_message(self, message):
        pass


def main():
    nezu = Nezu()
    nezu.run(settingsManager.getToken())


if __name__ == "__main__":
    main()
