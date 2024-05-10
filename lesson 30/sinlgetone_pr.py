class AppSettings:
    __instance = None

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = super(AppSettings, cls).__new__(cls)
        return cls.__instance

    def __init__(self):
        self.app_name = 'My Amazing Application'
        self.debug_mode = False
        self.log_level = 'INFO'

    @staticmethod
    def get_app_setting():
        if not AppSettings.__instance:
            AppSettings.__new__(AppSettings)
        return AppSettings.__instance
    

app1 = AppSettings.get_app_setting()
app2 = AppSettings()


print(app1.app_name)
print(app2.debug_mode)
app2.debug_mode = True
print(app1.debug_mode)

print(id(app1))
print(id(app2))