from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

    def open(self, path: str = ""):
        url = f"{self.base_url}{path}"
        self.page.goto(url, wait_until="domcontentloaded")

        # wait network শেষ হওয়া পর্যন্ত (SPA ready)
        self.page.wait_for_load_state("networkidle")

        # wait body visible (UI rendered)
        expect(self.page.locator("body")).to_be_visible()

        # wait title not empty (JS hydration finished)
        self.page.wait_for_function(
            "() => document.title && document.title.length > 0"
        )

    def get_title(self) -> str:
        return self.page.title()