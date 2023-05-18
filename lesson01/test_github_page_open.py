from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestGitHubPageOpen:
    def setup(self):
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)

    def test_github_page_open(self):
        self.driver.get("https://github.com/podchasova11/pythonProject01")
        assert self.driver.current_url == "https://github.com/podchasova11/pythonProject01"

    def test_orange_page_open(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        assert self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    def teardown(self):
        self.driver.close()