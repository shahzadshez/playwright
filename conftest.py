import pytest

from ui.config.settings import settings
from ui.pages.landing_page import LandingPage


@pytest.fixture
async def landing_page(page):
    landing = LandingPage(page, settings.base_url)
    await landing.open()
    yield page
