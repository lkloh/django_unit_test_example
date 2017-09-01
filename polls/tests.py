# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.test import TestCase
from django.utils import timezone

from polls.models import Choice, Question

# Create your tests here.
class QuestionModelTests(TestCase):

	def test_was_published_recently_with_future_question(self):
		''' was_published_recently() returns False
			when pub_date is set to the future.
		'''
		future_time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(pub_date=future_time)
		self.assertFalse(future_question.was_published_recently())


