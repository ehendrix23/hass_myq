![Validate](https://github.com/ehendrix23/hass_myq/workflows/Validate/badge.svg)
[![hacs][hacsbadge]][hacs]
![GitHub all releases](https://img.shields.io/github/downloads/ehendrix23/hass_myq/total)
![GitHub release (latest by SemVer)](https://img.shields.io/github/downloads/ehendrix23/hass_myq/latest/total)

<img align="left" width="80" height="80" src="https://raw.githubusercontent.com/ehendrix23/hass_myq/master/icons/icon.png" alt="App icon">

# MyQ

_Component to add MyQ garage doors and gates to hime assistant_

The myq cover platform lets you control MyQ-Enabled garage doors through Home Assistant. Device names in Home Assistant are generated based on the names defined in your MyQ Device mobile app.

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

