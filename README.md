![GitHub all releases](https://img.shields.io/github/downloads/ehendrix23/hass_myq/total)
![GitHub release (latest by SemVer)](https://img.shields.io/github/downloads/ehendrix23/hass_myq/latest/total)

[![GitHub Release][releases-shield]][releases]
[![License][license-shield]](LICENSE)

[![hacs][hacsbadge]][hacs]
[![Project Maintenance][maintenance-shield]][user_profile]

<img align="left" width="80" height="80" src="https://raw.githubusercontent.com/ehendrix23/hass_myq/master/icons/icon.png" alt="App icon">

# MyQ

_Component to add [myQ](https://www.myq.com) garage doors and gates to home assistant_

The myQ component lets you control myQ-Enabled garage doors and gates through Home Assistant. Device names in Home Assistant are generated based on the names defined in your myQ Device mobile app.

This is a custom component replacing the core myQ integration in [Homeassistant](https://home-assistant.io).

**This component will set up the following platforms.**

| Platform        | Description                                                                                         |
| --------------- | --------------------------------------------------------------------------------------------------- |
| `binary_sensor` | Represents myQ gateway.                                                                             |
| `cover`         | For each garage door or gate discovered from myQ. Shows current state and allows opening or closing |

## Installation with HACS

This component is available through [HACS](https://hacs.xyz/). This is the easiest method to install, stay informed of new releases, and update.

1. Within Home Assistant, open HACS (install HACS if not already installed, see [HACS Installation](https://hacs.xyz/docs/installation/prerequisites))
2. Go to the store and search for MyQ
3. Install myQ through HACS
4. Go to Configuration -> Integrations page
5. On the bottom right of the page click on the Orange + sign to add an integration
6. Search for myQ (if you don't see it, try refreshing your browser page to reload the cache)
7. Enter your myQ account credentials

## Manual Installation

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
2. If you do not have a `custom_components` directory (folder) there, you need to create it.
3. In the `custom_components` directory (folder) create a new folder called `myq`.
4. Download _all_ the files from the `custom_components/myq/` directory (folder) in this repository.
5. Place the files you downloaded in the new directory (folder) you created.
6. Restart Home Assistant
7. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "myQ"

Using your HA configuration directory (folder) as a starting point you should now also have this:

## Configuration is done in the UI

<!---->

## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)

## Credits

This project was generated from [@oncleben31](https://github.com/oncleben31)'s [Home Assistant Custom Component Cookiecutter](https://github.com/oncleben31/cookiecutter-homeassistant-custom-component) template.

Code template was mainly taken from [@Ludeeus](https://github.com/ludeeus)'s [integration_blueprint][integration_blueprint] template

---

[integration_blueprint]: https://github.com/custom-components/integration_blueprint
[black]: https://github.com/psf/black
[black-shield]: https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge
[buymecoffee]: https://www.buymeacoffee.com/ehendrix23
[buymecoffeebadge]: https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=for-the-badge
[commits-shield]: https://img.shields.io/github/commit-activity/y/ehendrix23/hass_myq.svg?style=for-the-badge
[commits]: https://github.com/ehendrix23/hass_myq/commits/main
[hacs]: https://hacs.xyz
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[discord]: https://discord.gg/Qa5fW2R
[discord-shield]: https://img.shields.io/discord/330944238910963714.svg?style=for-the-badge
[exampleimg]: example.png
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[forum]: https://community.home-assistant.io/
[license-shield]: https://img.shields.io/github/license/ehendrix23/hass_myq.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-%40ehendrix23-blue.svg?style=for-the-badge
[pre-commit]: https://github.com/pre-commit/pre-commit
[pre-commit-shield]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/ehendrix23/hass_myq.svg?style=for-the-badge
[releases]: https://github.com/ehendrix23/hass_myq/releases
[user_profile]: https://github.com/ehendrix23
