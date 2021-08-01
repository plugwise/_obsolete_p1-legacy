""" P1-legacy sensor module."""

import logging
from datetime import timedelta
import voluptuous as vol
import requests
from lxml import etree

from homeassistant.components.sensor import PLATFORM_SCHEMA
import homeassistant.helpers.config_validation as cv
from homeassistant.const import CONF_HOST, CONF_USERNAME, CONF_PASSWORD, CONF_RESOURCES
from homeassistant.util import Throttle
from homeassistant.helpers.entity import Entity

_LOGGER = logging.getLogger(__name__)

MIN_TIME_BETWEEN_UPDATES = timedelta(seconds=30)

SENSOR_PREFIX = "PSP1 "
SENSOR_TYPES = {
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

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_HOST): cv.string,
        vol.Required(CONF_USERNAME): cv.string,
        vol.Required(CONF_PASSWORD): cv.string,
        vol.Required(CONF_RESOURCES, default=[]): vol.All(
            cv.ensure_list, [vol.In(SENSOR_TYPES)]
        ),
    }
)


class PlugWiseP1Api:
    """ Plugwise P1 API class."""
    def __init__(self, host, user, password):
        self.session = requests.Session()
        self.host = host
        self.user = user
        self.password = password

    def get_base_url(self):
        return "http://{user}:{password}@{host}/".format(
            user=self.user, password=self.password, host=self.host
        )

    def get_electricity_module(self):
        modules_response = self.session.get(self.get_base_url() + "core/modules")
        modules_xml = etree.fromstring(modules_response.content)
        module_id = modules_xml.xpath(
            "//modules/module[count(./services/electricity_interval_meter)>0]/@id"
        )[0]
        module_response = self.session.get(
            self.get_base_url()
            + "core/modules;id={module_id}".format(module_id=module_id)
        )
        module_xml = etree.fromstring(module_response.content)
        return module_xml

    def get_gas_module(self):
        modules_response = self.session.get(self.get_base_url() + "core/modules")
        modules_xml = etree.fromstring(modules_response.content)
        module_id = modules_xml.xpath(
            "//modules/module[count(./services/gas_interval_meter)>0]/@id"
        )[0]
        module_response = self.session.get(
            self.get_base_url()
            + "core/modules;id={module_id}".format(module_id=module_id)
        )
        module_xml = etree.fromstring(module_response.content)
        return module_xml

    def get_electricity_consumed_point(self, electricity_module):
        value = electricity_module.xpath(
            '//module/services/electricity_point_meter/measurement[@directionality="consumed"]/text()'
        )[0]
        return float(value)

    def get_electricity_consumed_offpeak_interval(self, electricity_module):
        value = electricity_module.xpath(
            '//module/services/electricity_interval_meter/measurement[@directionality="consumed" and @tariff_indicator="nl_offpeak"]/text()'
        )[0]
        return float(value)

    def get_electricity_consumed_peak_interval(self, electricity_module):
        value = electricity_module.xpath(
            '//module/services/electricity_interval_meter/measurement[@directionality="consumed" and @tariff_indicator="nl_peak"]/text()'
        )[0]
        return float(value)

    def get_electricity_consumed_offpeak_cumulative(self, electricity_module):
        value = electricity_module.xpath(
            '//module/services/electricity_cumulative_meter/measurement[@directionality="consumed" and @tariff_indicator="nl_offpeak"]/text()'
        )[0]
        return float(value)

    def get_electricity_consumed_peak_cumulative(self, electricity_module):
        value = electricity_module.xpath(
            '//module/services/electricity_cumulative_meter/measurement[@directionality="consumed" and @tariff_indicator="nl_peak"]/text()'
        )[0]
        return float(value)

    def get_electricity_produced_point(self, electricity_module):
        value = electricity_module.xpath(
            '//module/services/electricity_point_meter/measurement[@directionality="produced"]/text()'
        )[0]
        return float(value)

    def get_electricity_produced_offpeak_interval(self, electricity_module):
        value = electricity_module.xpath(
            '//module/services/electricity_interval_meter/measurement[@directionality="produced" and @tariff_indicator="nl_offpeak"]/text()'
        )[0]
        return float(value)

    def get_electricity_produced_peak_interval(self, electricity_module):
        value = electricity_module.xpath(
            '//module/services/electricity_interval_meter/measurement[@directionality="produced" and @tariff_indicator="nl_peak"]/text()'
        )[0]
        return float(value)

    def get_electricity_produced_offpeak_cumulative(self, electricity_module):
        value = electricity_module.xpath(
            '//module/services/electricity_cumulative_meter/measurement[@directionality="produced" and @tariff_indicator="nl_offpeak"]/text()'
        )[0]
        return float(value)

    def get_electricity_produced_peak_cumulative(self, electricity_module):
        value = electricity_module.xpath(
            '//module/services/electricity_cumulative_meter/measurement[@directionality="produced" and @tariff_indicator="nl_peak"]/text()'
        )[0]
        return float(value)

    def get_gas_consumed_interval(self, gas_module):
        value = gas_module.xpath(
            '//module/services/gas_interval_meter/measurement[@directionality="consumed"]/text()'
        )[0]
        return float(value)

    def get_gas_consumed_cumulative(self, gas_module):
        value = gas_module.xpath(
            '//module/services/gas_cumulative_meter/measurement[@directionality="consumed"]/text()'
        )[0]
        return float(value)


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Setup the Plugwise Smile sensors."""
    host = config.get(CONF_HOST)
    username = config.get(CONF_USERNAME)
    password = config.get(CONF_PASSWORD)

    try:
        data = PlugwiseSmileData(host, username, password)
    except RunTimeError:
        _LOGGER.error("Unable to connect fetch data from Plugwise Smile %s", host)
        return False

    entities = []

    for resource in config[CONF_RESOURCES]:
        sensor_type = resource.lower()

        if sensor_type not in SENSOR_TYPES:
            SENSOR_TYPES[sensor_type] = [sensor_type.title(), "", "mdi:flash"]

        entities.append(PlugwiseSmileSensor(data, sensor_type))

    add_entities(entities)


# pylint: disable=abstract-method
class PlugwiseSmileData(object):
    """Representation of a Plugwise Wise."""

    def __init__(self, host, username, password):
        """Initialize the Plugwise Smile data."""
        self._host = host
        self._username = username
        self._password = password
        self._api = PlugWiseP1Api(self._host, self._username, self._password)

    @Throttle(MIN_TIME_BETWEEN_UPDATES)
    def update(self):
        """Update the data from the server."""
        self._electricity_module = self._api.get_electricity_module()
        self._gas_module = self._api.get_gas_module()

    def get_electricity_consumed_point(self):
        return self._api.get_electricity_consumed_point(self._electricity_module)

    def get_electricity_consumed_offpeak_interval(self):
        return self._api.get_electricity_consumed_offpeak_interval(
            self._electricity_module
        )

    def get_electricity_consumed_peak_interval(self):
        return self._api.get_electricity_consumed_peak_interval(
            self._electricity_module
        )

    def get_electricity_consumed_offpeak_cumulative(self):
        return self._api.get_electricity_consumed_offpeak_cumulative(
            self._electricity_module
        )

    def get_electricity_consumed_peak_cumulative(self):
        return self._api.get_electricity_consumed_peak_cumulative(
            self._electricity_module
        )

    def get_electricity_produced_point(self):
        return self._api.get_electricity_produced_point(self._electricity_module)

    def get_electricity_produced_offpeak_interval(self):
        return self._api.get_electricity_produced_offpeak_interval(
            self._electricity_module
        )

    def get_electricity_produced_peak_interval(self):
        return self._api.get_electricity_produced_peak_interval(
            self._electricity_module
        )

    def get_electricity_produced_offpeak_cumulative(self):
        return self._api.get_electricity_produced_offpeak_cumulative(
            self._electricity_module
        )

    def get_electricity_produced_peak_cumulative(self):
        return self._api.get_electricity_produced_peak_cumulative(
            self._electricity_module
        )

    def get_gas_consumed_interval(self):
        return self._api.get_gas_consumed_interval(self._gas_module)

    def get_gas_consumed_cumulative(self):
        return self._api.get_gas_consumed_cumulative(self._gas_module)


class PlugwiseSmileSensor(Entity):
    """Representation of a Plugwise Smile sensor."""

    def __init__(self, data, sensor_type):
        """Initialize the sensor."""
        self.data = data
        self.sr_type = sensor_type
        self._name = SENSOR_PREFIX + SENSOR_TYPES[self.sr_type][0]
        self._device_class = SENSOR_TYPES[self.sr_type][1]
        self._unit_of_measurement = SENSOR_TYPES[self.sr_type][2]
        self._icon = SENSOR_TYPES[self.sr_type][3]
        self._state = None

        self.update()

    @property
    def device_class(self):
        """Return the device_class of the sensor."""
        return self._device_class

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def icon(self):
        """Icon to use in the frontend, if any."""
        return self._icon

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement of this entity, if any."""
        return self._unit_of_measurement

    def get_power(self, power_value):
        pvSplit = power_value.split()
        value = float(pvSplit[0])
        if pvSplit[1] == "kW":
            return value * 1000
        else:
            return value

    def update(self):
        """Get the latest data and use it to update our sensor state."""
        self.data.update()

        if self.type == "electricity_consumed_offpeak_interval":
            self._state = self.data.get_electricity_consumed_offpeak_interval()
        elif self.type == "electricity_consumed_peak_interval":
            self._state = self.data.get_electricity_consumed_peak_interval()
        elif self.type == "electricity_consumed_offpeak_cumulative":
            self._state = self.data.get_electricity_consumed_offpeak_cumulative()
        elif self.type == "electricity_consumed_peak_cumulative":
            self._state = self.data.get_electricity_consumed_peak_cumulative()
        elif self.type == "electricity_produced_offpeak_interval":
            self._state = self.data.get_electricity_produced_offpeak_interval()
        elif self.type == "electricity_produced_peak_interval":
            self._state = self.data.get_electricity_produced_peak_interval()
        elif self.type == "electricity_produced_offpeak_cumulative":
            self._state = self.data.get_electricity_produced_offpeak_cumulative()
        elif self.type == "electricity_produced_peak_cumulative":
            self._state = self.data.get_electricity_produced_peak_cumulative()
        elif self.type == "gas_consumed_interval":
            self._state = self.data.get_gas_consumed_interval()
        elif self.type == "gas_consumed_cumulative":
            self._state = self.data.get_gas_consumed_cumulative()
        elif self.type == "net_electricity_point":
            self._state = (
                self.data.get_electricity_consumed_point()
                - self.data.get_electricity_produced_point()
            )
        elif self.type == "net_electricity_cumulative":
            self._state = (
                self.data.get_electricity_consumed_offpeak_cumulative()
                + self.data.get_electricity_consumed_peak_cumulative()
                - self.data.get_electricity_produced_offpeak_cumulative()
                - self.data.get_electricity_produced_peak_cumulative()
            )
