import json


class Settings:
    def __init__(self, token=""):
        self.token = token

    def toJSON(self):
        return json.dumps(self.__dict__)


class SettingsManager:
    def __init__(self):
        self.settings = None
        self.settingsFiles = "settings/settings.json"
        # Load or Create File
        try:
            with open(self.settingsFiles, 'r+') as file:
                data = json.loads(file.read())
                self.settings = Settings(data['token'])
        # Create a new Settings file.
        except FileNotFoundError as e:
            with open(self.settingsFiles, 'w+') as file:
                self.settings = Settings()
                self.save()

    def getToken(self):
        return self.settings.token

    def save(self):
        try:
            with open(self.settingsFiles, 'r+') as file:
                file.write(self.settings.toJSON())
        except Exception as e:
            print(e)


settingsManager = SettingsManager()
