"""Test the MyQ config flow."""
from unittest.mock import patch

from homeassistant import config_entries, setup
from homeassistant.const import CONF_PASSWORD, CONF_USERNAME
from pymyq.errors import InvalidCredentialsError, MyQError
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.myq.const import DOMAIN

from .util import async_config_entries_flow


async def test_form_user(hass):
    """Test we get the user form."""

    await setup.async_setup_component(hass, "persistent_notification", {})
    result = await async_config_entries_flow(
        hass, DOMAIN, context={"source": config_entries.SOURCE_USER}
    )
    assert result["type"] == "form"
    assert result["errors"] == {}

    with patch(
        "custom_components.myq.config_flow.pymyq.login",
        return_value=True,
    ), patch(
        "custom_components.myq.async_setup", return_value=True
    ) as mock_setup, patch(
        "custom_components.myq.async_setup_entry",
        return_value=True,
    ) as mock_setup_entry:
        result2 = await hass.config_entries.flow.async_configure(
            result["flow_id"],
            {"username": "test-username", "password": "test-password"},
        )
        await hass.async_block_till_done()

    assert result2["type"] == "create_entry"
    assert result2["title"] == "test-username"
    assert result2["data"] == {
        "username": "test-username",
        "password": "test-password",
    }
    assert len(mock_setup.mock_calls) == 1
    assert len(mock_setup_entry.mock_calls) == 1


async def test_form_invalid_auth(hass):
    """Test we handle invalid auth."""
    result = await async_config_entries_flow(
        hass, DOMAIN, context={"source": config_entries.SOURCE_USER}
    )

    with patch(
        "custom_components.myq.config_flow.pymyq.login",
        side_effect=InvalidCredentialsError,
    ):
        result2 = await hass.config_entries.flow.async_configure(
            result["flow_id"],
            {"username": "test-username", "password": "test-password"},
        )

    assert result2["type"] == "form"
    assert result2["errors"] == {"base": "invalid_auth"}


async def test_form_cannot_connect(hass):
    """Test we handle cannot connect error."""
    result = await async_config_entries_flow(
        hass, DOMAIN, context={"source": config_entries.SOURCE_USER}
    )

    with patch(
        "custom_components.myq.config_flow.pymyq.login",
        side_effect=MyQError,
    ):
        result2 = await hass.config_entries.flow.async_configure(
            result["flow_id"],
            {"username": "test-username", "password": "test-password"},
        )

    assert result2["type"] == "form"
    assert result2["errors"] == {"base": "cannot_connect"}


async def test_form_homekit(hass):
    """Test that we abort from homekit if myq is already setup."""
    await setup.async_setup_component(hass, "persistent_notification", {})

    result = await async_config_entries_flow(
        hass,
        DOMAIN,
        context={"source": "homekit"},
        data={"properties": {"id": "AA:BB:CC:DD:EE:FF"}},
    )

    assert result["type"] == "form"
    assert result["errors"] == {}
    flow = next(
        flow
        for flow in hass.config_entries.flow.async_progress()
        if flow["flow_id"] == result["flow_id"]
    )
    assert flow["context"]["unique_id"] == "AA:BB:CC:DD:EE:FF"

    entry = MockConfigEntry(
        domain=DOMAIN, data={CONF_USERNAME: "mock", CONF_PASSWORD: "mock"}
    )
    entry.add_to_hass(hass)

    result = await async_config_entries_flow(
        hass,
        DOMAIN,
        context={"source": "homekit"},
        data={"properties": {"id": "AA:BB:CC:DD:EE:FF"}},
    )

    assert result["type"] == "abort"
