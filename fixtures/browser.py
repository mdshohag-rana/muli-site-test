import pytest
from pathlib import Path
from playwright.sync_api import sync_playwright

ARTIFACTS_DIR = Path("artifacts")

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture
def context(browser, request):
    test_name = request.node.name.replace("/", "_")

    context = browser.new_context(
        record_video_dir=str(ARTIFACTS_DIR / "videos"),
        record_video_size={"width": 1280, "height": 720},
    )

    # start tracing
    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    yield context

    # stop tracing and save
    trace_path = ARTIFACTS_DIR / "traces" / f"{test_name}.zip"
    trace_path.parent.mkdir(parents=True, exist_ok=True)
    context.tracing.stop(path=str(trace_path))

    context.close()

@pytest.fixture
def page(context):
    page = context.new_page()
    yield page