import pytest
from utils.config_loader import load_sites_config

@pytest.fixture(params=load_sites_config(), ids=lambda site: site['name'])
def site_config(request):
    return request.param
