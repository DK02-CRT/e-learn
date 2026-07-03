from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from coureses.models import Module, Course, Topic, Quest, Question, Answer

User = get_user_model()


class CoursesTest(TestCase):

    def setUp(self):
        # Course
        self.course = Course.objects.create(
            title="Chemia",
            desc="Chemia - desc",
            slug="chemia"
        )

        # Module
        self.module = Module.objects.create(
            course=self.course,
            title="Chemia organiczna",
            order=1,
            content="Chemia organiczna - desc"
        )

        # Topic
        self.topic = Topic.objects.create(
            module=self.module,
            title="Węglowodory"
        )

        # Question
        self.quest = Quest.objects.create(
            quest=self.topic,
            content="zestaw zadań dla węglowodorów"
        )

        # Question
        self.question = Question.objects.create(
            question=self.quest,
            content="Na co dzielą się węglowodory ?"
        )

        # Answers
        self.correct = Answer.objects.create(
            question=self.question,
            content="Alkany",
            is_correct=True
        )

        self.wrong = Answer.objects.create(
            question=self.question,
            content="Aminokwasy",
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

    def test_create_course(self):
        self.assertEqual(self.course.title, "Chemia")
        self.assertEqual(self.course.desc, "Chemia - desc")
        self.assertEqual(self.course.slug, "chemia")

    def test_create_module(self):
        self.assertEqual(self.module.course, self.course)
        self.assertEqual(self.module.title, "Chemia organiczna")
        self.assertEqual(self.module.content, "Chemia organiczna - desc")

    def test_create_topic(self):
        self.assertEqual(self.topic.module, self.module)
        self.assertEqual(self.topic.title, "Węglowodory")
        self.assertEqual(self.course.desc, "Chemia - desc")
        self.assertEqual(self.course.slug, "chemia")

    def test_module_page_loads(self):
        url = reverse(
            "module_detail",
            kwargs={
                "pk": self.module.pk
            }
        )

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_topic_page_loads(self):
        url = reverse(
            "topic_detail",
            kwargs={
                "module_pk": self.module.pk,
                "topic_pk": self.topic.pk
            }
        )

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Alkany")

    def test_quiz_scoring_correct_answer(self):
        url = reverse(
            "topic_detail",
            kwargs={
                "module_pk": self.module.pk,
                "topic_pk": self.topic.pk
            }
        )

        response = self.client.post(url, {
            "answers": [self.correct.id],
            "time": "15"
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["score"], 1)

    def test_quiz_scoring_wrong_answer(self):
        url = reverse(
            "topic_detail",
            kwargs={
                "module_pk": self.module.pk,
                "topic_pk": self.topic.pk
            }
        )

        response = self.client.post(url, {
            "answers": [self.wrong.id],
            "time": "15"
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["score"], 0)
