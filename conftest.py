pytest_plugins = [
    "fixtures.browser",
    "fixtures.site",
]

import pytest
import allure
from pathlib import Path

ARTIFACTS_DIR = Path("artifacts")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute test
    outcome = yield
    report = outcome.get_result()

    # only if test failed during call phase
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page", None)

        if page:
            test_name = item.name.replace("/", "_")

            # 📸 Screenshot
            screenshot_dir = ARTIFACTS_DIR / "screenshots"
            screenshot_dir.mkdir(parents=True, exist_ok=True)
            screenshot_path = screenshot_dir / f"{test_name}.png"
            page.screenshot(path=str(screenshot_path), full_page=True)

            allure.attach.file(
                str(screenshot_path),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

            # 🎥 Video attach
            if page.video:
                video_path = page.video.path()
                allure.attach.file(
                    video_path,
                    name="video",
                    attachment_type=allure.attachment_type.WEBM,
                )

            # 🧵 Trace attach
            trace_file = ARTIFACTS_DIR / "traces" / f"{test_name}.zip"
            if trace_file.exists():
                allure.attach.file(
                    str(trace_file),
                    name="trace",
                    attachment_type=allure.attachment_type.ZIP,
                )