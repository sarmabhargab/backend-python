from django.test import TestCase, Client
from django.urls import reverse
from myapp.models import Users
import json


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.insert_url = reverse('insert')
        self.delete_url = reverse('delete',args=[2])

        self.user1 = Users.objects.create(
            name='name1',
            dob = '2010-01-01',
            address = 'address1',
            email = 'email@email.com'
        )


    def test_home_GET(self):
        response = self.client.get(self.home_url)

        # self.assertEquals(response.status_code,200)
        assert response.status_code == 200
        self.assertTemplateUsed(response,'home.html')


    def test_insert_GET(self):
        response = self.client.get(self.insert_url)

        # self.assertEquals(response.status_code,200)
        assert response.status_code == 200
        self.assertTemplateUsed(response,'insert.html')                
        self.assertTemplateUsed(response,'base.html')


    def test_delete_GET(self):
        response = self.client.get(self.delete_url)

        # self.assertEquals(response.status_code,302)
        assert response.status_code == 302


    def test_user_detail_POST(self):
        response = self.client.post(self.insert_url,{
            'name' : 'name1',
            'dob' : '2010-01-01',
            'address' : 'address1',
            'email' : 'email@email.com'
        })

        assert response.status_code == 302
        assert self.user1.name == 'name1'
        assert self.user1.dob == '2010-01-01'
        assert self.user1.address == 'address1'
        assert self.user1.email == 'email@email.com'

        # self.assertEquals(response.status_code,302)
        # self.assertEquals(self.user1.name,'name1')
        # self.assertEquals(self.user1.dob,'2010-01-01')
        # self.assertEquals(self.user1.address,'address1')
        # self.assertEquals(self.user1.email,'email@email.com')
