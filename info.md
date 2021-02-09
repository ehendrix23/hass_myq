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

## Changes as compared to your installed version:

### Breaking Changes

### Changes

### Features

{% if version_installed.replace("v", "").replace(".","") | int < 001  %}

- Initial release
  {% endif %}
  {% if version_installed.replace("v", "").replace(".","") | int < 002  %}
- Added change history
  {% endif %}

### Bugfixes

{% if version_installed.replace("v", "").replace(".","") | int < 002  %}

- Fixed repository information shown in HACS
  {% endif %}

---

{% endif %}
