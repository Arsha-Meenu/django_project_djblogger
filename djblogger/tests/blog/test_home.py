import  pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

pytestmark = pytest.mark.django_db


class TestHomePage:
    def test_homepag_url(self,client):
        url = reverse('homepage')
        response = client.get(url)
        assert response.status_code == 200

    def test_post_htmx_fragment(self, client):
        headers = {'HTTP_HX-Request': 'True'}
        url = reverse('homepage')
        response = client.get(url, **headers)
        assertTemplateUsed(response, 'blog/components/post-list-elements.html')
