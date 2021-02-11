"""The MyQ integration."""
from homeassistant.const import (
    STATE_CLOSED,
    STATE_CLOSING,
    STATE_OFF,
    STATE_ON,
    STATE_OPEN,
    STATE_OPENING,
)
from pymyq.garagedoor import (
    STATE_CLOSED as MYQ_COVER_STATE_CLOSED,
    STATE_CLOSING as MYQ_COVER_STATE_CLOSING,
    STATE_OPEN as MYQ_COVER_STATE_OPEN,
    STATE_OPENING as MYQ_COVER_STATE_OPENING,
)
from pymyq.lamp import STATE_OFF as MYQ_LIGHT_STATE_OFF, STATE_ON as MYQ_LIGHT_STATE_ON

__version__ = "0.1.0"
PROJECT_URL = "https://github.com/ehendrix23/hass_myq"
ISSUE_URL = "{}issues".format(PROJECT_URL)

DOMAIN = "myq"
PLATFORMS = ["binary_sensor", "cover", "light"]

MYQ_TO_HASS = {
    MYQ_COVER_STATE_CLOSED: STATE_CLOSED,
    MYQ_COVER_STATE_CLOSING: STATE_CLOSING,
    MYQ_COVER_STATE_OPEN: STATE_OPEN,
    MYQ_COVER_STATE_OPENING: STATE_OPENING,
    MYQ_LIGHT_STATE_ON: STATE_ON,
    MYQ_LIGHT_STATE_OFF: STATE_OFF,
}

MYQ_GATEWAY = "myq_gateway"
MYQ_COORDINATOR = "coordinator"

# myq has some ratelimits in place
# and 15 seemed to be work every time
UPDATE_INTERVAL = 15
