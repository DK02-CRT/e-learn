from django.test import TestCase, Client
from results.models import ResultsQuiz, ResultsTopic
from quizes.models import Quiz
from coureses.models import Topic, Course, Module
from users.models import User
from django.utils import timezone
from datetime import timedelta
from django.urls import reverse


class QuizTest(TestCase):

    def setUp(self):
        self.course = Course.objects.create(
            title="Chemia",
            desc="Chemia - desc",
            slug="chemia"
        )
        self.module = Module.objects.create(
            course=self.course,
            title="Chemia organiczna",
            order=1,
            content="Chemia organiczna - desc"
        )
        self.topic = Topic.objects.create(
            module=self.module,
            title="Węglowodory"
        )

        self.quiz = Quiz.objects.create(
            course=self.course,
            title="Quiz z chemii"
        )

        self.user = User.objects.create_user(
            username="adam",
            password="haslo123",
            email="adam@test.pl",
        )
        score = 8
        max_score = 10

        self.resTopic = ResultsTopic.objects.create(
            users=self.user,
            topic=self.topic,
            score=score,
            max_score=max_score,
            started_at=timezone.now(),
            duration=timedelta(seconds=25),
            passed=(score/max_score >= 0.75)
        )

        self.resQuiz = ResultsQuiz.objects.create(
            users=self.user,
            quiz=self.quiz,
            score=score,
            max_score=max_score,
            started_at=timezone.now(),
            duration=timedelta(seconds=25),
            passed=(score/max_score >= 0.8)
        )

        self.client = Client()

        self.client.login(
            username="adam",
            password="haslo123"
        )

    def test_create_result_quiz(self):
        self.assertEqual(self.resQuiz.users, self.user)
        self.assertEqual(self.resQuiz.quiz, self.quiz)
        self.assertEqual(self.resQuiz.score, 8)
        self.assertEqual(self.resQuiz.max_score, 10)
        self.assertEqual(self.resQuiz.passed, True)

    def test_create_result_topic(self):
        self.assertEqual(self.resTopic.users, self.user)
        self.assertEqual(self.resTopic.topic, self.topic)
        self.assertEqual(self.resTopic.score, 8)
        self.assertEqual(self.resTopic.max_score, 10)

    def test_result_page_load(self):
        response = self.client.get(
            reverse("results")
        )
        self.assertEqual(response.status_code, 200)

    def test_results_template(self):
        response = self.client.get(reverse("results"))

        self.assertTemplateUsed(response, "results/results.html")

    def test_results_context(self):
        response = self.client.get(reverse("results"))

        self.assertIn("resultsQuiz", response.context)
        self.assertIn("resultsTopic", response.context)

    def test_best_users_quizes_exists(self):
        response = self.client.get(reverse("results"))

        self.assertIn("bestUsersQ", response.context)

    def test_best_users_topic_exists(self):
        response = self.client.get(reverse("results"))

        self.assertIn("bestUsersR", response.context)

    def test_best_time_quizes_exists(self):
        response = self.client.get(reverse("results"))

        self.assertIn("bestTimeQ", response.context)

    def test_best_time_topic_exists(self):
        response = self.client.get(reverse("results"))

        self.assertIn("bestTimeR", response.context)
