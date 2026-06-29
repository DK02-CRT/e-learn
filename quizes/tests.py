from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from quizes.models import Quiz, Quiz_Task, Quiz_Answer
from coureses.models import Course
from users.models import User
from django.core.files.uploadedfile import SimpleUploadedFile

User = get_user_model()

avatar = SimpleUploadedFile(
    "avatar.jpg",
    b"file_content",
    content_type="image/jpeg"
)

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
            avatar=avatar,
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

    # def test_create_topic(self):
    #     self.assertEqual(self.topic.module, self.module)
    #     self.assertEqual(self.topic.title, "Węglowodory")
    #     self.assertEqual(self.course.desc, "Chemia - desc")
    #     self.assertEqual(self.course.slug, "chemia")

    # def test_module_page_loads(self):
    #     url = reverse(
    #         "module_detail",
    #         kwargs={
    #             "slug": self.course.slug,
    #             "pk": self.module.pk
    #         }
    #     )

    #     response = self.client.get(url)

    #     self.assertEqual(response.status_code, 200)

    # def test_topic_page_loads(self):
    #     url = reverse(
    #         "topic_detail",
    #         kwargs={
    #             "slug": self.course.slug,
    #             "module_pk": self.module.pk,
    #             "topic_pk": self.topic.pk
    #         }
    #     )

    #     response = self.client.get(url)

    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, "Alkany")

    def test_quiz_scoring_correct_answer(self):
        url = reverse(
            "quiz_detail",
            args=[
                self.quiz.pk
            ]
        )

        response = self.client.post(url, {
            "answers": [self.correct.id]
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
            "answers": [self.wrong.id]
        })

        self.assertEqual(response.context["score"], 0)