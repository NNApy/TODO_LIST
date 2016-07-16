from django.test import TestCase
from models import Tasks

class MyTest(TestCase):

    def test_ok_save_my_task(self):
        data = {'task_name': 'my_test_task', 'done': '1'}
        response = self.client.post('/add_task/', data)
        q_my_task = Tasks.objects.filter()
        self.assertEquals(q_my_task.count(), 1)
        task = q_my_task.get()
        self.assertEquals(task.task_name, data['task_name'])
        self.assertEquals(task.done, data['done'])

    def test_ok_delete_my_task(self):
        data = {'task_name': 'my_test_task', 'done': '1'}
        response = self.client.post('/add_task/', data)
        q_my_task = Tasks.objects.filter()
        self.assertEquals(q_my_task.count(), 1)
        Tasks.objects.filter(id=1).delete()
        self.assertEquals(q_my_task.count(), 0)

    def test_ok_edit_my_task(self):
        data = {'task_name': 'my_test_task', 'done': '1'}
        response = self.client.post('/add_task/', data)
        q_my_task = Tasks.objects.filter()
        self.assertEquals(q_my_task.count(), 1)
        Tasks.objects.filter(id=1).update(task_name='NEW NAME FOR MY TASK')
        self.assertEquals(Tasks.objects.filter().get().task_name, 'NEW NAME FOR MY TASK')

