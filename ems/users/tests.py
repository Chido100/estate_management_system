from django.test import TestCase
from .models import User




class UsersTest(TestCase):

    def setUp(self):
        new_user = User(
            username='tester1',
            email='tester1@email.com',
            first_name='tester one',
            house_number=3,
            street_name='bury street',

            is_resident=True
        )
        self.assertEqual(new_user.username, 'tester1')

    def test_user_list(self):
        all_user = User.objects.all()
        self.assertEqual(all_users.count(), 1)
    


