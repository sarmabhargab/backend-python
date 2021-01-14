from django.urls import reverse,resolve
from myapp.views import home,insert,delete

class TestUrls:
    
    def test_home_urls_is_resolves(self):
        url = reverse('home')
        print(resolve(url))
        assert resolve(url).view_name == 'home'


    def test_insert_urls_is_resolves(self):
        url = reverse('insert')
        print(resolve(url))
        assert resolve(url).view_name == 'insert'

    def test_delete_urls_is_resolves(self):
        url = reverse('delete',args=[5])
        print(resolve(url))
        assert resolve(url).view_name == 'delete'

    # def test_home_urls_is_resolves(self):
    #     url = reverse('home')
    #     print(resolve(url))
    #     self.assertEquals(resolve(url).func, home)
    


    # def test_insert_urls_is_resolves(self):
    #     url = reverse('insert')
    #     print(resolve(url))
    #     self.assertEquals(resolve(url).func, insert)

    # def test_delete_urls_is_resolves(self):
    #     url = reverse('delete',args=[5])
    #     print(resolve(url))
    #     self.assertEquals(resolve(url).func, delete)
