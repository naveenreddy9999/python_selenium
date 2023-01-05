from seleniumpagefactory import PageFactory


class SignInPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {

        "txt": ("NAME", "q"),
        "btn": ("XPATH", "(//input[@type='submit'])[3]")

    }

    def sign(self):
        self.txt.set_text("naveen\n")
        print("pass")

    def enter(self):
        self.btn.click()
        print("pass 2")
