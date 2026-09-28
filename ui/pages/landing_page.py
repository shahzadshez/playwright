

class LandingPage:
    def __init__(self, page, url):
        self.page = page
        self.url = url
        self.navigation = page.get_by_role("navigation")
        self.discovery_call_link = self.navigation.get_by_role("link", name="Book a Discovery Call")
        self.email_button = page.get_by_role("button", name="msmohdshahzad1@gmail.com")
        self.linkedin_link = self.navigation.get_by_role("link", name="LinkedIn")
        self.github_link = self.navigation.get_by_role("link", name="GitHub")
        self.theme_toggle = page.get_by_role("button", name="Toggle light/dark theme")
    
    async def open(self):
        await self.page.goto(self.url)
