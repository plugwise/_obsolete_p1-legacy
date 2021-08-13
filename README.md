# P1-legacy

This code is based on https://bitbucket.org/jvdschoot/home-assistant-sensor-plugwise-smile-p1/src/master/.
It is added to the plugwise repository so that all the plugwise-related HA Core custom_components can be found in one place.

This code is meant for a Smile P1 with firmware 2.1.x. For P1's with newer firmware please use `plugwise-beta`.

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
    host: 10.10.10.1 #example
    username: smile
    password: abcdefgh #the 8-letter Smile ID
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
      - net_electricity_point
      - net_electricity_cumulative
      - gas_consumed_interval
      - gas_consumed_cumulative
    scan_interval: 10 ### optional, see below ###
```

# How to change the update interval?

The default update interval is 30 seconds.
You can change this by editing line 23 in `__init_.py`; change the number at the end of the line. 
Don't go below 10 seconds, as on most smartmeters the update interval is 10 seconds.
Also, add the optional scan_interval_line, see above.
