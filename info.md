[myQ Custom Component](https://github.com/ehendrix23/hass_myq) for homeassistant

<img align="left" width="80" height="80" src="https://raw.githubusercontent.com/ehendrix23/hass_myq/master/icons/icon.png" alt="App icon">

# MyQ

_Component to add [myQ](https://www.myq.com) garage doors and gates to home assistant_

The myQ component lets you control myQ-Enabled garage doors and gates through Home Assistant. Device names in Home Assistant are generated based on the names defined in your myQ Device mobile app.

{% if prerelease %}

### NB!: This is a Beta version!

{% endif %}

**This component will set up the following platforms.**

### Binary Sensor

Your `MyQ` gateway will appear as a binary sensor that shows if the device is connected.

### Cover

Garage doors and gates linked to your `MyQ` account will appear as covers.

{% if installed and version_installed != selected_tag %}

## Changes as compared to your installed version:

### Breaking Changes

### Changes

{% if version_installed.replace("v", "").replace(".","") | int < 003  %}

- Bumped pymyq up from 3.0.1 to 3.0.2
- Changed minimum HASS release to 2021.2.0 from 2021.3.0
  {% endif %}

### Features

{% if version_installed.replace("v", "").replace(".","") | int < 001  %}

- Initial release
  {% endif %}
  {% if version_installed.replace("v", "").replace(".","") | int < 002  %}
- Added change history
  {% endif %}
  {% if version_installed.replace("v", "").replace(".","") | int < 003  %}
- Added CHANGELOG.md
  {% endif %}

### Bugfixes

{% if version_installed.replace("v", "").replace(".","") | int < 003  %}

- Fixed repository information shown in HACS
  {% endif %}

---

{% endif %}
