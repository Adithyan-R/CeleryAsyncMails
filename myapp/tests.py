import unittest

from django.test import TestCase, RequestFactory
from unittest.mock import patch, MagicMock
from django.urls import reverse
from .views import send_email_view, check_email_task_view, heavy_task_view


class SendEmailViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    @patch('myapp.tasks.send_email_task.delay')
    def test_send_email_view(self, mock_send_email_task_delay):
        mock_task = MagicMock()
        mock_task.id = 'mock_task_id'
        mock_send_email_task_delay.return_value = mock_task

        # Make a mock GET request to the view
        url = reverse('send_email')
        request = self.factory.get(url,
                                   {'to_email': 'test@example.com', 'subject': 'Test', 'body': 'Testing email body'})
        response = send_email_view(request)

        # Print the response content for debugging
        response_content = response.content.decode('utf-8')
        print(f"Expected content: 'Your task ID is: mock_task_id'")
        print(f"Response content: {response_content}")

        # Check if the response contains the mock task ID
        self.assertIn('Your task ID is: mock_task_id', response_content)

    @patch('myapp.views.AsyncResult')
    def test_check_email_task_view(self, mock_AsyncResult):
        mock_task = MagicMock()
        mock_task.state = 'SUCCESS'
        mock_task.result = 'Email sent successfully'
        mock_task.id = 'mock_task_id'

        mock_AsyncResult.return_value = mock_task

        url = reverse('check_email_task', args=['mock_task_id'])
        request = self.factory.get(url)
        response = check_email_task_view(request, 'mock_task_id')

        # Print the response content for debugging
        response_content = response.content.decode('utf-8')
        print(f"Expected content: 'Result: Email sent successfully'")
        print(f"Response content: {response_content}")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Task ID: mock_task_id')
        self.assertContains(response, 'Result: Email sent successfully')


class HeavyTaskViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    @patch('myapp.tasks.some_heavy_task.delay')
    def test_heavy_task_view(self, mock_some_heavy_task_delay):
        mock_task = MagicMock()
        mock_task.id = 'mock_task_id'
        mock_some_heavy_task_delay.return_value = mock_task

        # Make a mock GET request to the view
        url = reverse('heavy_task')
        request = self.factory.get(url)
        response = heavy_task_view(request)

        # Print the response content for debugging
        response_content = response.content.decode('utf-8')
        print(f"Expected content: 'Your task ID is: mock_task_id'")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Your task ID is: mock_task_id')


if __name__ == '__main__':
    unittest.main()
