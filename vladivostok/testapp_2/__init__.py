from otree.api import *

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'testapp_2'
    PLAYERS_PER_GROUP = 8
    NUM_ROUNDS = 2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):

    def sum_offer(group):
        return (group.get_player_by_id(1).offer
                + group.get_player_by_id(2).offer
                + group.get_player_by_id(3).offer
                + group.get_player_by_id(5).offer
                + group.get_player_by_id(6).offer
                + group.get_player_by_id(7).offer)

    def ost(group):
        if (group.sum_offer()) > 900:
            return (f'Оставшиеся средства будут получены случайным игроком. Остаток: ${group.sum_offer() - 900}')
        else:
            return (" ")

    def results(group):
        if group.sum_offer() > 900:
            return ('Отлично! Вам удалось набрать минимально необходимую сумму. '
                    'Пострадавшим удалось вернуть все потерянные средства.')
        else:
            return ('К сожалению, необходимую сумму набрать не удалось. Все вложенные средства сгорели.')

    def results_recip(group):
        if group.sum_offer() > 900:
            return ('Донорам удалось набрать минимально необходимую сумму. '
                    'Вам будут возвращены потерянные средства!')
        else:
            return ('К сожалению, необходимую сумму набрать не удалось. Вам не будут возвращены потерянные средства.')

    def set_payoff_recip(group):
        if group.sum_offer() > 900:
            return 1000
        else:
            return 0



class Player(BasePlayer):
    balance = models.IntegerField(initial=1000)
    porog_small = models.IntegerField(initial=450)
    porog_large = models.IntegerField(initial=900)

    offer = models.IntegerField(label='Размер пожертвования:', min=0, max=1000)

    def role(self):
        if self.id_in_group == 1:
            return 'Донор'
        elif self.id_in_group == 2:
            return 'Донор'
        elif self.id_in_group == 3:
            return 'Донор'
        elif self.id_in_group == 5:
            return 'Донор'
        elif self.id_in_group == 6:
            return 'Донор'
        elif self.id_in_group == 7:
            return 'Донор'
        else:
            return 'Пострадавший'

    def set_payoff(self):
        if self.id_in_group != 4 and self.id_in_group != 8:
            return self.balance - self.offer

    def sum_offer(self):
        sum_offers = 0
        for i in range(0, 7):
            if self.get_others_in_group()[i].offer is not None:
                sum_offers += self.get_others_in_group()[i].offer
        # return #(self.get_others_in_group()[0].offer
        #        + self.get_others_in_group()[1].offer
        #        + self.get_others_in_group()[2].offer
        #        + self.get_others_in_group()[4].offer
        #        + self.get_others_in_group()[5].offer
        #        + self.get_others_in_group()[6].offer)
        return sum_offers


class MyPage(Page):
    def is_displayed(self):
        return self.round_number == 1

    form_model = 'player'


class ResultsWaitPage(WaitPage):
    pass


class MyPageResults(Page):
    def is_displayed(self):
        return self.id_in_group != 4 and self.id_in_group != 8

    form_model = 'player'
    form_fields = ['offer']


class MyPageResultsrecip(Page):
    def is_displayed(self):
        return self.id_in_group == 4 or self.id_in_group == 8


class PageDonor(Page):
    form_model = 'player'
    form_fields = ['offer']

    def is_displayed(self):
        return self.id_in_group != 4 and self.id_in_group != 8


class PageRecipient(Page):

    def is_displayed(self):
        return self.id_in_group == 4 or self.id_in_group == 8


class ChoiseWaitPage(WaitPage):
    def is_displayed(self):
        return self.id_in_group == 4 or self.id_in_group == 8


class RecipientResult(Page):
    def is_displayed(self):
        return self.id_in_group == 4 or self.id_in_group == 8


class DonorResult(Page):
    def is_displayed(self):
        return self.id_in_group != 4 and self.id_in_group != 8


class FinalPage(Page):
    form_model = 'group'
    form_model = 'player'

    def is_displayed(self):
        return self.id_in_group != 4 and self.id_in_group != 8


class FinalPagerecip(Page):
    form_model = 'group'
    form_model = 'player'

    def is_displayed(self):
        return self.id_in_group == 4 or self.id_in_group == 8



page_sequence = [MyPage,
                 ResultsWaitPage,
                 MyPageResults, MyPageResultsrecip,
                 ChoiseWaitPage,
                 DonorResult,
                 ResultsWaitPage,
                 FinalPage, FinalPagerecip]
