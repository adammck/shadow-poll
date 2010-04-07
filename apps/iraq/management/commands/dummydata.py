#!/usr/bin/env python
# vim: et ts=4 sw=4

import random
from django.core.management.base import NoArgsCommand
from apps.reporters.models import PersistantBackend, PersistantConnection
from apps.poll.models import Question, User, UserResponse
from apps.charts.models import District


class Command(NoArgsCommand):
    CHOICE_ENTROPY   = 20
    DISTRICT_ENTROPY = 5
    RESPONSES        = 100

    def handle_noargs(self, **options):
        self.districts = self._districts()

        for n in xrange(self.RESPONSES):
            self.random_answer()

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
            age = random.randint(2, 18),
            governorate = district.governorate.code,
            district = district.code)

        response = UserResponse.objects.create(
            choice=self._random_choice(choices),
            question=question,
            user=user)

        #print "Responded %s to Q#%d in %s district." %\
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
            self.CHOICE_ENTROPY)

    def _districts(self):
        return self._zipped_ratios(
            District.objects.all(),
            self.DISTRICT_ENTROPY)

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
