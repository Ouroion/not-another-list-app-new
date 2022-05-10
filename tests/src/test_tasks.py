import unittest

import helper


class TaskTestCase(unittest.TestCase):
    def setUp(self):
        # Create 3 Users
        helper.create_user(username='unittest1', password='unittest1')
        helper.create_user(username='unittest2', password='unittest2')
        helper.create_user(username='unittest3', password='unittest3')

        
        # Create a list for said Users
        self.list_id = helper.lists_create(username='unittest1', password='unittest1',
                                           name='test_list_with_task',
                                           description='test').json()['id']

        self.empty_list_id = helper.lists_create(username='unittest1', password='unittest1',
                                                 name='test_list_no_task',
                                                 description='test').json()['id']

        # Create Task for List
        self.task_id = helper.task_create(username='unittest1',
                                          password='unittest1',
                                          list_id=self.list_id,
                                          name='test_task',
                                          description='test_desc').json()['id']

    def test_get_task_by_list_id(self):
        tasks = helper.task_get(username='unittest1',
                                password='unittest1',
                                list_id=self.list_id)
        assert len(tasks.json()) > 0
        assert tasks.json()[0]['list_id'] == self.list_id

    def test_get_task_by_list_id_no_tasks(self):
        tasks = helper.task_get(username='unittest1',
                                password='unittest1',
                                list_id=self.empty_list_id)
        assert tasks.json() == []

    def test_task_create(self):
        task = helper.task_create(username='unittest1',
                                  password='unittest1',
                                  list_id=self.list_id,
                                  name='test_task_create',
                                  description='test_task_create')

        assert task.json()['name'] == 'test_task_create'
        assert task.json()['list_id'] == self.list_id

        # delete new task
        helper.task_delete(username='unittest1',
                           password='unittest1',
                           id=task.json()['id'])

    def test_task_create_no_list_id(self):
        pass

    def test_task_delete(self):
        helper.task_delete(username='unittest1',
                           password='unittest1',
                           id=self.task_id)

        tasks = helper.task_get(username='unittest1',
                                password='unittest1',
                                list_id=self.list_id)
        assert tasks.json() == []

    def tearDown(self):
                # Delete Task
        helper.task_delete(username='unittest1',
                           password='unittest1',
                           id=self.task_id)

        # Delete List
        helper.lists_delete(username='unittest1', password='unittest1',
                            name='test_list_with_task')
        helper.lists_delete(username='unittest1', password='unittest1',
                            name='test_list_no_task')


        # Delete Users
        helper.delete_user(username='unittest1', password='unittest1')
        helper.delete_user(username='unittest2', password='unittest2')


if __name__ == '__main__':
    ttc = TaskTestCase()

    try:
        ttc.setUp()
        ttc.test_task_delete()
    except Exception as e:
        print(repr(e))
    ttc.tearDown()
