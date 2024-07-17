
class SettingsRepository:
    def __init__(self, settings):
        self.settings = settings

    def get(self, key):
        return self.settings.get(key)

    def set(self, key, value):
        self.settings.set(key, value)

    def save(self):
        self.settings.save()