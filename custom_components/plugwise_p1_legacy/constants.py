"""P1-legacy constants."""

import datetime as dt

UTC = dt.timezone.utc
LR_TIME_0 = dt.datetime.utcfromtimestamp(0).replace(tzinfo=UTC)

MIN_TIME_BETWEEN_UPDATES = dt.timedelta(seconds=30)

SENSOR_PREFIX = "P1 "
SENSOR_TYPES = {
    "electricity_consumed_point": [
        "Electricity Consumed Point",
        "power",
        "measurement",
        None,
        "W",
        "mdi:flash",
    ],
    "electricity_produced_point": [
        "Electricity Produced Point",
        "power",
        "measurement",
        None,
        "W",
        "mdi:flash",
    ],
    "electricity_consumed_offpeak_interval": [
        "Electricity Consumed Off Peak Interval",
        "energy",
        "measurement",
        None,
        "Wh",
        "mdi:flash",
    ],
    "electricity_consumed_peak_interval": [
        "Electricity Consumed Peak Interval",
        "energy",
        "measurement",
        None,
        "Wh",
        "mdi:flash",
    ],
    "electricity_consumed_offpeak_cumulative": [
        "Electricity Consumed Off Peak Cumulative",
        "energy",
        "measurement",
        LR_TIME_0,
        "kWh",
        "mdi:flash",
    ],
    "electricity_consumed_peak_cumulative": [
        "Electricity Consumed Peak Cumulative",
        "energy",
        "measurement",
        LR_TIME_0,
        "kWh",
        "mdi:flash",
    ],
    "electricity_produced_offpeak_interval": [
        "Electricity Produced Off Peak Interval",
        "energy",
        "measurement",
        None,
        "Wh",
        "mdi:white-balance-sunny",
    ],
    "electricity_produced_peak_interval": [
        "Electricity Produced Peak Interval",
        "energy",
        "measurement",
        None,
        "Wh",
        "mdi:white-balance-sunny",
    ],
    "electricity_produced_offpeak_cumulative": [
        "Electricity Produced Off Peak Cumulative",
        "energy",
        "measurement",
        LR_TIME_0,
        "kWh",
        "mdi:white-balance-sunny",
    ],
    "electricity_produced_peak_cumulative": [
        "Electricity Produced Peak Cumulative",
        "energy",
        "measurement",
        LR_TIME_0,
        "kWh",
        "mdi:white-balance-sunny",
    ],
    "net_electricity_cumulative": [
        "Net Electricity Cumulative",
        "energy",
        "measurement",
        LR_TIME_0,
        "kWh",
        "mdi:flash",
    ],
    "net_electricity_point": [
        "Net Electricity Point",
        "power",
        "measurement",
        None,
        "W",
        "mdi:flash",
    ],
    "gas_consumed_interval": [
        "Gas Consumed Interval",
        None,
        "measurement",
        None,
        "m3",
        "mdi:gas-cylinder",
    ],
    "gas_consumed_cumulative": [
        "Gas Consumed Cumulative",
        None,
        "measurement",
        LR_TIME_0,
        "m3",
        "mdi:gas-cylinder",
    ],
}
