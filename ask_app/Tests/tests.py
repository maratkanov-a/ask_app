from django.test import TestCase
from ask_app.models import Question
import unittest
# Create your tests here.


# def test_get_queryset(self):
#     """
#     Return the last five published questions (not including those set to be
#     published in the future).
#     """
#     assert isinstance(Question.objects.filter(text_author='sashok').order_by, object)
#     return Question.objects.filter(text_author='sashok').order_by('-create_date')

# class DefaultWidgetSizeTestCase(unittest.TestCase):
#     def runTest(self):
#         widget = Widget('The widget')
#         self.assertEqual(widget.size(), (50, 50), 'incorrect default size')