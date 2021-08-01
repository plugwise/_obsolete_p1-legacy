""" P1-legacy constants."""

from datetime import timedelta

MIN_TIME_BETWEEN_UPDATES = timedelta(seconds=30)

SENSOR_PREFIX = "P1 "
SENSOR_TYPES = {
    "electricity_consumed_point": [
        "Electricity Consumed Point",
        "power",
        "W",
        "mdi:flash",
    ],
    "electricity_produced_point": [
        "Electricity Produced Point",
        "power",
        "W",
        "mdi:flash",
    ],
    "electricity_consumed_offpeak_interval": [
        "Electricity Consumed Off Peak Interval",
        "energy",
        "Wh",
        "mdi:flash",
    ],
    "electricity_consumed_peak_interval": [
        "Electricity Consumed Peak Interval",
        "energy",
        "Wh",
        "mdi:flash",
    ],
    "electricity_consumed_offpeak_cumulative": [
        "Electricity Consumed Off Peak Cumulative",
        "energy",
        "Wh",
        "mdi:flash",
    ],
    "electricity_consumed_peak_cumulative": [
        "Electricity Consumed Peak Cumulative",
        "energy",
        "Wh",
        "mdi:flash",
    ],
    "electricity_produced_offpeak_interval": [
        "Electricity Produced Off Peak Interval",
        "energy",
        "Wh",
        "mdi:white-balance-sunny",
    ],
    "electricity_produced_peak_interval": [
        "Electricity Produced Peak Interval",
        "energy",
        "Wh",
        "mdi:white-balance-sunny",
    ],
    "electricity_produced_offpeak_cumulative": [
        "Electricity Produced Off Peak Cumulative",
        "energy",
        "Wh",
        "mdi:white-balance-sunny",
    ],
    "electricity_produced_peak_cumulative": [
        "Electricity Produced Peak Cumulative",
        "energy",
        "Wh",
        "mdi:white-balance-sunny",
    ],
    "net_electricity_cumulative": [
        "Net Electricity Cumulative",
        "power",
        "W",
        "mdi:flash",
    ],
    "net_electricity_point": ["Net Electricity Point", "power", "W", "mdi:flash"],
    "gas_consumed_interval": ["Gas Consumed Interval", None, "m3", "mdi:gas-cylinder"],
    "gas_consumed_cumulative": [
        "Gas Consumed Cumulative",
        None,
        "m3",
        "mdi:gas-cylinder",
    ],
}
