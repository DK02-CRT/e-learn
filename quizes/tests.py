from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from quizes.models import Quiz, Quiz_Task, Quiz_Answer
from coureses.models import Course

User = get_user_model()


class QuizTest(TestCase):

    def setUp(self):

        self.course = Course.objects.create(
            title="Chemia",
            desc="Wiedza o chemii",
            slug="chemia"
        )

        self.quiz = Quiz.objects.create(
            course=self.course,
            title="Quiz z chemii"
        )

        self.task = Quiz_Task.objects.create(
            task=self.quiz,
            context="Czym jest siarczan sodu?"
        )

        self.correct = Quiz_Answer.objects.create(
            answer=self.task,
            option="Substancja stosowana w medycynie",
            is_correct=True
        )

        self.wrong = Quiz_Answer.objects.create(
            answer=self.task,
            option="Substancja toksyczna",
            is_correct=False
        )

        self.user = User.objects.create_user(
            username="adam",
            password="haslo123",
            email="adam@test.pl",
        )

        self.client = Client()

        self.client.login(
            username="adam",
            password="haslo123"
        )

    def test_create_quiz(self):
        self.assertEqual(self.quiz.course, self.course)
        self.assertEqual(self.quiz.title, "Quiz z chemii")

    def test_create_task(self):
        self.assertEqual(self.task.task, self.quiz)
        self.assertEqual(self.task.context, "Czym jest siarczan sodu?")

    def test_quiz_scoring_correct_answer(self):
        url = reverse(
            "quiz_detail",
            args=[
                self.quiz.pk
            ]
        )

        response = self.client.post(url, {
            "answers": [self.correct.id],
            "time": "15"
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["score"], 1)

    def test_quiz_scoring_wrong_answer(self):
        url = reverse(
            "quiz_detail",
            args=[
                self.quiz.pk
            ]
        )

        response = self.client.post(url, {
            "answers": [self.wrong.id],
            "time": "15"
        })

        self.assertEqual(response.context["score"], 0)
