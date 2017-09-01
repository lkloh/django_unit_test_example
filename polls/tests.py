# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.test import Client, TestCase
from django.utils import timezone

from polls.models import Choice, Question

# Create your tests here.
class QuestionModelTests(TestCase):

	def test_was_published_recently_with_future_question(self):
		''' was_published_recently() returns False
			when pub_date is set to the future.
		'''
		future_question_pub_time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(pub_date=future_question_pub_time)
		self.assertFalse(future_question.was_published_recently())

	def test_was_published_recently_with_old_question(self):
		''' was_published_recently() returns False for questions
			whose pub_date is older than 1 day
		'''
		old_question_pub_time = timezone.now() - datetime.timedelta(days=1, seconds=1)
		old_question = Question(pub_date=old_question_pub_time)
		self.assertFalse(old_question.was_published_recently())

	def test_was_published_recently_with_new_question(self):
		''' was_published_recently() returns False for questions
			whose pub_date is less than 1 day
		'''
		new_question_pub_time = timezone.now() - datetime.timedelta(hours=1)
		new_question = Question(pub_date=new_question_pub_time)
		self.assertTrue(new_question.was_published_recently())


