"""The scene tests for the myq platform."""
from homeassistant.const import STATE_OFF

from .util import async_init_integration


async def test_create_lights(hass):
    """Test creation of lights."""

    await async_init_integration(hass)

    state = hass.states.get("light.large_garage_light")
    assert state.state == STATE_OFF
    expected_attributes = {
        "friendly_name": "Large Garage Light",
        "supported_features": 0,
    }
    # Only test for a subset of attributes in case
    # HA changes the implementation and a new one appears
    assert all(
        state.attributes[key] == expected_attributes[key] for key in expected_attributes
    )

    state = hass.states.get("light.small_garage_light")
    assert state.state == STATE_OFF
    expected_attributes = {
        "friendly_name": "Small Garage Light",
        "supported_features": 0,
    }
    # Only test for a subset of attributes in case
    # HA changes the implementation and a new one appears
    assert all(
        state.attributes[key] == expected_attributes[key] for key in expected_attributes
    )
