from os import environ

SESSION_CONFIGS = [
    dict(
        name='Four_people_session',
        display_name='Эксперимент 3 донора + 1 получатель',
        app_sequence=['testapp', 'testapp_2', 'spasibo'],
        num_demo_participants = 8,
        info=False,
     ),


    dict(
        name='eight_people_session',
        display_name='Эксперимент 6 доноров + 2 получателя',
        app_sequence=['testapp_2', 'testapp', 'spasibo'],
        num_demo_participants = 8,
        info=False,
     ),


]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'ru'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '5908177708601'
