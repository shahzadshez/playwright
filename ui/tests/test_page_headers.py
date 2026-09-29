from playwright.async_api import expect


async def test_landing_page_metadata(landing_page):
    await expect(landing_page).to_have_title("Mohammad Shahzad \u2014 QA Automation Consultant")


async def test_landing_page_top_header_left(landing_page):
    await expect(landing_page.get_by_role("navigation").get_by_role("link", name="Book a Discovery Call")).to_be_visible()
    await expect(landing_page.get_by_role("button", name="msmohdshahzad1@gmail.com")).to_be_visible()


async def test_landing_page_top_header_right(landing_page):
    await expect(landing_page.get_by_role("navigation").get_by_role("link", name="GitHub")).to_be_visible()
    await expect(landing_page.get_by_role("navigation")).to_contain_text("GitHub")
    await expect(landing_page.get_by_role("button", name="Toggle light/dark theme")).to_contain_text("Light")
    await expect(landing_page.locator("#copy-email-nav")).to_contain_text("msmohdshahzad1@gmail.com")
    await expect(landing_page.get_by_role("navigation").get_by_role("link", name="LinkedIn")).to_be_visible()
    await expect(landing_page.get_by_role("navigation")).to_contain_text("LinkedIn")


async def test_landing_page_heading(landing_page):
    await expect(landing_page.locator("div").filter(has_text="Mohammad Shahzad QA").nth(1)).to_be_visible()
    await landing_page.get_by_text("Mohammad Shahzad", exact=True).click()
    await expect(landing_page.get_by_text("QA Automation Consultant", exact=True)).to_be_visible()
    await expect(landing_page.get_by_role("heading", name="Strategic QA Automation Built")).to_be_visible()
    await expect(landing_page.locator("h1")).to_contain_text("Strategic QA Automation Built for Scalable Deployment Pipelines.")
    await landing_page.get_by_text("QA Automation Consultant", exact=True).click()
    await expect(landing_page.get_by_text("I architect your complete")).to_be_visible()
    await expect(landing_page.get_by_role("banner")).to_contain_text("I architect your complete test automation suite as a one-time engagement, then hand it off fully documented — no retainers, no QA headcount. You get enterprise-grade Playwright coverage and self-healing test pipelines wired into your CI/CD, giving your team the power to deploy daily with total confidence.")

