from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'testapp'
    PLAYERS_PER_GROUP = 4
    NUM_ROUNDS = 2



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):

    def sum_offer(group):
        return (group.get_player_by_id(1).offer
                + group.get_player_by_id(2).offer
                + group.get_player_by_id(3).offer)

    def ost(group):
        if (group.sum_offer()) > 450:
            return (f'Оставшиеся средства будут получены случайным игроком. Остаток: {group.sum_offer() - 450}₽')
        else:
            return (" ")

    def results(group):
        if group.sum_offer() > 450:
            return ('Вам удалось набрать минимально необходимую сумму. '
                    'Пострадавшему будут возвращены все потерянные средства!')
        else:
            return ('К сожалению, необходимую сумму набрать не удалось. Все вложенные средства сгорели.')


    def results_recip(group):
        if group.sum_offer() > 450:
            return ('Донорам удалось набрать минимально необходимую сумму. '
                    'Вам будут возвращены потерянные средства!')
        else:
            return ('К сожалению, необходимую сумму набрать не удалось. Вам не будут возвращены потерянные средства.')


class Player(BasePlayer):

    balance = models.IntegerField(initial=1000)
    porog_small = models.IntegerField(initial=450)
    offer = models.IntegerField(label='Размер пожертвования:', min=0, max=1000)



    def role(self):
        if self.id_in_group == 1:
            return 'Донор'
        elif self.id_in_group == 2:
            return 'Донор'
        elif self.id_in_group == 3:
            return 'Донор'
        else:
            return 'Пострадавший'



    def sum_offer(self):
        return (self.get_others_in_group()[0].offer
                    + self.get_others_in_group()[1].offer
                + self.get_others_in_group()[2].offer)




    def set_payoff(self):
        if self.id_in_group != 4:
            return self.balance - self.offer
        elif self.sum_offer() > self.porog_small:
            return self.balance
        else:
            return 0


class MyPage(Page):
    def is_displayed(self):
        return self.round_number == 1
    form_model = 'player'



class ResultsWaitPage(WaitPage):
    pass


class MyPageResults(Page):
    def is_displayed(self):
        return self.id_in_group != 4
    form_model = 'player'
    form_fields = ['offer']


class MyPageResultsrecip(Page):
    def is_displayed(self):
        return self.id_in_group == 4


class PageDonor(Page):
    form_model = 'player'
    form_fields = ['offer']

    def is_displayed(self):
        return self.id_in_group != 4


class PageRecipient(Page):

    def is_displayed(self):
        return self.id_in_group == 4




class ChoiseWaitPage(WaitPage):
    def is_displayed(self):
        return self.id_in_group == 4


class RecipientResult(Page):
    def is_displayed(self):
        return self.id_in_group == 4


class DonorResult(Page):
    def is_displayed(self):
        return self.id_in_group != 4


class FinalPage(Page):
    form_model = 'group'
    form_model = 'player'
    def is_displayed(self):
        return self.id_in_group != 4


class FinalPagerecip(Page):
    form_model = 'group'
    form_model = 'player'
    def is_displayed(self):
        return self.id_in_group == 4


page_sequence = [
    MyPage,
    ResultsWaitPage,
    MyPageResults, MyPageResultsrecip,
    ChoiseWaitPage,
    DonorResult,
    ResultsWaitPage,
    FinalPage, FinalPagerecip]
