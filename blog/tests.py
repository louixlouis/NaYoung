from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Post

# Create your tests here.
# TDD - Test Driven Development 
'''
1. 포스트리스트
2. 상세페이지
3. 이미지 업로드
4. 파일 업로드...
'''

class TestView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_post_list(self):
        # 포스트 목록 페이지
        response = self.client.get('/blog/')
        # 정상적으로 로드
        self.assertEqual(response.status_code, 200)
        # 타이틀 확인
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(soup.title.text, 'LOUIS BLOG')
        navbar = soup.nav
        #self.assertIn(, second)