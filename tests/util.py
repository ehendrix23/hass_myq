"""Tests for the myq integration."""
import json
import logging
from unittest.mock import patch

from homeassistant.const import CONF_PASSWORD, CONF_USERNAME
from homeassistant.core import HomeAssistant
from pymyq.const import ACCOUNTS_ENDPOINT, DEVICES_ENDPOINT
from pytest_homeassistant_custom_component.common import MockConfigEntry, load_fixture

from custom_components.myq.const import DOMAIN

_LOGGER = logging.getLogger(__name__)


async def async_config_entries_flow(hass, *args, **kwargs):
    with patch("homeassistant.loader.Integration.resolve_from_root", return_value=None):
        result = await hass.config_entries.flow.async_init(*args, **kwargs)
        # DOMAIN, context={"source": config_entries.SOURCE_USER}
        # )
    return result


async def async_init_integration(
    hass: HomeAssistant,
    skip_setup: bool = False,
) -> MockConfigEntry:
    """Set up the myq integration in Home Assistant."""

    devices_fixture = "devices.json"
    devices_json = load_fixture(devices_fixture)
    devices_dict = json.loads(devices_json)

    def _handle_mock_api_oauth_authenticate():
        return 1234, 1800

    def _handle_mock_api_request(method, returns, url, **kwargs):
        _LOGGER.debug("URL: %s", url)
        if url == ACCOUNTS_ENDPOINT:
            _LOGGER.debug("Accounts")
            return None, {"accounts": [{"id": 1, "name": "mock"}]}
        if url == DEVICES_ENDPOINT.format(account_id=1):
            _LOGGER.debug("Devices")
            return None, devices_dict
        _LOGGER.debug("Something else")
        return None, {}

    # Added patch to resolve from root as currently HASS picks up the myq core component and not
    # the custom component. This can be removed once myq is removed from the core.
    with patch(
        "pymyq.api.API._oauth_authenticate",
        side_effect=_handle_mock_api_oauth_authenticate,
    ), patch("pymyq.api.API.request", side_effect=_handle_mock_api_request), patch(
        "homeassistant.loader.Integration.resolve_from_root", return_value=None
    ):
        entry = MockConfigEntry(
            domain=DOMAIN, data={CONF_USERNAME: "mock", CONF_PASSWORD: "mock"}
        )
        entry.add_to_hass(hass)

        if not skip_setup:
            await hass.config_entries.async_setup(entry.entry_id)
            await hass.async_block_till_done()

    return entry
