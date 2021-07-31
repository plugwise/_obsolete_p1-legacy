# P1-legacy

This code is a copy from https://bitbucket.org/jvdschoot/home-assistant-sensor-plugwise-smile-p1/src/master/

It is added to the plugwise repository so that all the plugwise-related HA Core custom_components can be found in one place.

# How to install?

- Use [HACS](https://hacs.xyz)
- Navigate to the `Integrations` page and use the three-dots icon on the top right to add a custom repository.
- Use the link to this page as the URL and select 'Integrations' as the category.
- Look for `Plugwise P1-legacy custom component` in `Integrations` and install it!

## How to add the integration to HA Core

Add this to your configuration.yaml file, under `sensor`:
```
sensor #remove this line when already present, always remove this comment
  - platform: plugwise_p1_legacy
    name: Plugwise P1-legacy
    host: x.x.x.x
    username: smile
    password: password
    resources:
      - electricity_consumed_point
      - electricity_consumed_offpeak_interval
      - electricity_consumed_peak_interval
      - electricity_consumed_offpeak_cumulative
      - electricity_consumed_peak_cumulative
      - electricity_produced_point
      - electricity_produced_offpeak_interval
      - electricity_produced_peak_interval
      - electricity_produced_offpeak_cumulative
      - electricity_produced_peak_cumulative
      - gas_consumed_interval
      - gas_consumed_cumulative
```

# How to change the update interval?

The default update interval is 30 seconds.
You can change this by editing line 23 in `__init_.py`; change the number at the end of the line. Don't go lower than 10.
