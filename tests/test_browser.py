from seleniumbase import BaseCase

class Google(BaseCase):

    def test_home(self):
        self.open('https://google.com')

        self.assert_title('Google')



