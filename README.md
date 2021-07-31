# P1_legacy

This code is a copy from https://bitbucket.org/jvdschoot/home-assistant-sensor-plugwise-smile-p1/src/master/

It is added to the plugwise repository so that all the working plugwise-related HA Core can be found in one place.

Usage:
```
  - platform: plugwise_p1_legacy
    name: Plugwise Smile
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
