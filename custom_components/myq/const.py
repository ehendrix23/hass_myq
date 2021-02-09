"""The MyQ integration."""
from homeassistant.const import STATE_CLOSED, STATE_CLOSING, STATE_OPEN, STATE_OPENING
from pymyq.garagedoor import (
    STATE_CLOSED as MYQ_COVER_STATE_CLOSED,
    STATE_CLOSING as MYQ_COVER_STATE_CLOSING,
    STATE_OPEN as MYQ_COVER_STATE_OPEN,
    STATE_OPENING as MYQ_COVER_STATE_OPENING,
)

__version__ = "0.0.1"
PROJECT_URL = "https://github.com/ehendrix23/hass_myq"
ISSUE_URL = "{}issues".format(PROJECT_URL)

DOMAIN = "myq"
PLATFORMS = ["cover", "binary_sensor"]

MYQ_TO_HASS = {
    MYQ_COVER_STATE_CLOSED: STATE_CLOSED,
    MYQ_COVER_STATE_CLOSING: STATE_CLOSING,
    MYQ_COVER_STATE_OPEN: STATE_OPEN,
    MYQ_COVER_STATE_OPENING: STATE_OPENING,
}

MYQ_GATEWAY = "myq_gateway"
MYQ_COORDINATOR = "coordinator"

# myq has some ratelimits in place
# and 61 seemed to be work every time
UPDATE_INTERVAL = 15
