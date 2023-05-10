from otree.api import *


doc = """
Demographic application
"""


class C(BaseConstants):
    NAME_IN_URL = "demographics"
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    gender = models.StringField(label="¿Cuál es su género?",
                                choices=["Hombre",
                                         "Mujer",
                                         "Otro",
                                         "Prefiero no decir"])
    age = models.IntegerField(label="¿Cuál es su edad en años cumplidos?",
                              choices=list(range(18, 60)))
    ethnicity = models.StringField(label="¿Cuál es su etnicidad?",
                                   choices=["Asiático",
                                            "Indio",
                                            "Negro",
                                            "Blanco",
                                            "Oriente medio",
                                            "Latino-Hispánico"])


# PAGES
class Demographics(Page):
    form_model = "player"
    form_fields = ["gender", "age", "ethnicity"]


page_sequence = [Demographics]
