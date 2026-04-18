from pages.home_page import HomePage

def test_home_page_title(page, site_config):
    home = HomePage(page, site_config['base_url'])
    home.open_home()
    title = home.get_home_title()
    assert title is not None and len(title) > 0, f"Home page title should not be empty for site {site_config['name']}"