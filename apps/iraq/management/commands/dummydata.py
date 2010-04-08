#!/usr/bin/env python
# vim: et ts=4 sw=4

import random
from optparse import make_option
from django.core.management.base import BaseCommand
from apps.reporters.models import PersistantBackend, PersistantConnection
from apps.poll.models import Question, User, UserResponse
from apps.charts.models import District


class Command(BaseCommand):
    help = "Generates some dummy data to populate the website."
    args = "[optional number of votes]"

    option_list = BaseCommand.option_list + (
        make_option('--choice-entropy',   dest='choice_entropy',   default='20'),
        make_option('--district-entropy', dest='district_entropy', default='5'),
        make_option('--age-entropy',      dest='age_entropy',      default='5'))

    def handle(self, num_votes='1000', **options):
        num_votes = int(num_votes)

        self.choice_entropy   = int(options['choice_entropy'])
        self.district_entropy = int(options['district_entropy'])
        self.age_entropy      = int(options['age_entropy'])

        print "Generating %d votes with entropy: %d/%d/%d" %\
            (num_votes, self.choice_entropy, self.district_entropy, self.age_entropy)

        self.districts = self._zipped_ratios(
            District.objects.all(),
            self.district_entropy)

        self.ages = self._zipped_ratios(
            range(2, 18),
            self.age_entropy)

        for n in xrange(num_votes):
            self.random_answer()

        print "Done."

    @property
    def _backend(self):
        return PersistantBackend.objects.get_or_create(
            defaults={"title": "Dummy Data"},
            slug="dummy")[0]

    @property
    def _connection(self):
        return PersistantConnection.objects.get_or_create(
            identity="Dummy Data Spawner",
            backend=self._backend,
            is_bot=False)[0]

    def random_answer(self):
        district = self._random_choice(self.districts)
        question, choices = random.choice(self._questions(district))

        user = User.objects.create(
            connection = self._connection,
            gender = random.choice('mf'),
            age = self._random_choice(self.ages),
            governorate = district.governorate.code,
            district = district.code)

        response = UserResponse.objects.create(
            choice=self._random_choice(choices),
            question=question,
            user=user)

        #print "Voted %s to Q#%d in %s district." %\
        #    (response.choice.code, question.pk, district.name)

    @staticmethod
    def _random_choice(pairs):
        x = random.uniform(0, 1)

        for element, weight in pairs:
            if x <= weight: return element
            x -= weight

        raise ValueError

    def _choices(self, question):
        return self._zipped_ratios(
            question.choice_set.all(),
            self.choice_entropy)

    def _questions(self, district):
        if not hasattr(district, "_questions"):
            district._questions = [
                (q, self._choices(q))
                for q in Question.objects.all()]

        return district._questions

    @classmethod
    def _zipped_ratios(cls, objects, entropy):
        weights = cls._weights(len(objects), entropy)
        ratios = cls._ratios(weights)
        return zip(objects, ratios)

    @staticmethod
    def _ratios(weights):
        total = float(sum(weights))
        return [w/total for w in weights]

    @staticmethod
    def _weights(number, entropy):
        return [
            (random.uniform(1, entropy)**entropy)
            for _ in range(number)]
