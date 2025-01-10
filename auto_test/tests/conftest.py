from typing import Generator

import pytest
from playwright.sync_api import Playwright, APIRequestContext

base_url_restful = "https://restful-booker.herokuapp.com/"


@pytest.fixture
def api_request_context(
    playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(
        base_url=base_url_restful
    )
    yield request_context
    request_context.dispose()
