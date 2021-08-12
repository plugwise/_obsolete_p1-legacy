"""API for legacy Smile P1."""

import requests
from dateutil import tz
from dateutil.parser import parse
from lxml import etree


class SmileP1Api:
    """Plugwise P1 API class."""

    def __init__(self, host, user, password):
        self.session = requests.Session()
        self.host = host
        self.user = user
        self.password = password

    def get_base_url(self):
        return f"http://{self.user}:{self.password}@{self.host}/"

    def get_electricity_module(self):
        modules_response = self.session.get(self.get_base_url() + "core/modules")
        modules_xml = etree.fromstring(modules_response.content)
        module_id = modules_xml.xpath(
            "//modules/module[count(./services/electricity_interval_meter)>0]/@id"
        )[0]
        module_response = self.session.get(
            self.get_base_url() + f"core/modules;id={module_id}"
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
            self.get_base_url() + f"core/modules;id={module_id}"
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
        log_date = None
        log_date = electricity_module.xpath('//module/services/electricity_interval_meter/measurement')[0]
        log_date = parse(log_date.get('log_date'))
        log_date = log_date.astimezone(tz.gettz("UTC")).replace(tzinfo=None)
        return [float(value), log_date]

    def get_electricity_consumed_peak_interval(self, electricity_module):
        value = electricity_module.xpath(
            '//module/services/electricity_interval_meter/measurement[@directionality="consumed" and @tariff_indicator="nl_peak"]/text()'
        )[0]
        log_date = None
        log_date = electricity_module.xpath('//module/services/electricity_interval_meter/measurement')[0]
        log_date = parse(log_date.get('log_date'))
        log_date = log_date.astimezone(tz.gettz("UTC")).replace(tzinfo=None)
        return [float(value), log_date]

    def get_electricity_consumed_offpeak_cumulative(self, electricity_module):
        value = electricity_module.xpath(
            '//module/services/electricity_cumulative_meter/measurement[@directionality="consumed" and @tariff_indicator="nl_offpeak"]/text()'
        )[0]
        return float(value) / 1000

    def get_electricity_consumed_peak_cumulative(self, electricity_module):
        value = electricity_module.xpath(
            '//module/services/electricity_cumulative_meter/measurement[@directionality="consumed" and @tariff_indicator="nl_peak"]/text()'
        )[0]
        return float(value) / 1000

    def get_electricity_produced_point(self, electricity_module):
        value = electricity_module.xpath(
            '//module/services/electricity_point_meter/measurement[@directionality="produced"]/text()'
        )[0]
        return float(value)

    def get_electricity_produced_offpeak_interval(self, electricity_module):
        value = electricity_module.xpath(
            '//module/services/electricity_interval_meter/measurement[@directionality="produced" and @tariff_indicator="nl_offpeak"]/text()'
        )[0]
        log_date = None
        log_date = electricity_module.xpath('//module/services/electricity_interval_meter/measurement')[0]
        log_date = parse(log_date.get('log_date'))
        log_date = log_date.astimezone(tz.gettz("UTC")).replace(tzinfo=None)
        return [float(value), log_date]

    def get_electricity_produced_peak_interval(self, electricity_module):
        value = electricity_module.xpath(
            '//module/services/electricity_interval_meter/measurement[@directionality="produced" and @tariff_indicator="nl_peak"]/text()'
        )[0]
        log_date = None
        log_date = electricity_module.xpath('//module/services/electricity_interval_meter/measurement')[0]
        log_date = parse(log_date.get('log_date'))
        log_date = log_date.astimezone(tz.gettz("UTC")).replace(tzinfo=None)
        return [float(value), log_date]

    def get_electricity_produced_offpeak_cumulative(self, electricity_module):
        value = electricity_module.xpath(
            '//module/services/electricity_cumulative_meter/measurement[@directionality="produced" and @tariff_indicator="nl_offpeak"]/text()'
        )[0]
        return float(value) / 1000

    def get_electricity_produced_peak_cumulative(self, electricity_module):
        value = electricity_module.xpath(
            '//module/services/electricity_cumulative_meter/measurement[@directionality="produced" and @tariff_indicator="nl_peak"]/text()'
        )[0]
        return float(value) / 1000

    def get_gas_consumed_interval(self, gas_module):
        value = gas_module.xpath(
            '//module/services/gas_interval_meter/measurement[@directionality="consumed"]/text()'
        )[0]
        log_date = None
        log_date = electricity_module.xpath('//module/services/electricity_interval_meter/measurement')[0]
        log_date = parse(log_date.get('log_date'))
        log_date = log_date.astimezone(tz.gettz("UTC")).replace(tzinfo=None)
        return [float(value), log_date]

    def get_gas_consumed_cumulative(self, gas_module):
        value = gas_module.xpath(
            '//module/services/gas_cumulative_meter/measurement[@directionality="consumed"]/text()'
        )[0]
        return float(value)
