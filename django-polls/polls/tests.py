from django.test import TestCase
from django.utils import timezone
import datetime
from django.urls import reverse
from .models import Question

def create_question(question_text, days, hours=0, minutes=0, seconds=0):
    time = timezone.now()+ datetime.timedelta(days=days, hours= hours ,minutes=minutes,seconds= seconds)
    return  Question.objects.create(question_text= question_text, pub_date= time)

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        '''was_published_recently() should return False With future question'''
        now=timezone.now()
        future_question=Question( pub_date=now + datetime.timedelta(days=30))
        self.assertIs(future_question.was_published_recently(), False)
       
    def test_was_published_recently_with_old_question(self):
        '''was_published_recently() return False with question publishe before 1 day'''
        old_question= Question(pub_date = timezone.now() - datetime.timedelta(days=1, seconds=1))
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_new_question(self):
        new_question = Question(pub_date= timezone.now() - datetime.timedelta( minutes=1) )
        self.assertIs(new_question.was_published_recently(), True)

class IndexViewTestCase(TestCase):
    def test_no_questions(self):
        ''' If no question present , n appropriate ,message is displayed'''
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
    def test_future_question(self):
        ''' Question with pub_date in future is not displayed'''
        create_question('future_question?', days=30 )
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,"No polls are available.")

    def test_one_past_question(self):
        '''Past question will be displayed'''
        create_question("Past Question?",days= -2)
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['latest_question_list'],['<Question: Past Question?>'])
    def test_one_past_one_future(self):
        ''' Only past questions are displayed ''' 
        create_question("Past Question?", days=-10)
        create_question("Future Question?", days=10)
        response= self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['latest_question_list'],['<Question: Past Question?>'])
       
        
class DetailViewTestCase(TestCase):
    def test_future_question(self):
        ''' future question is not displayed'''
        future_question= create_question("Future question?", days= 10)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
    def test_past_question(self):
        ''' only past question is displayed '''
        past_question= create_question("Past Question?", days= -10)
        url = reverse('polls:detail',args=(past_question.id,))
        response= self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, past_question.question_text)
        
# Create your tests here.
