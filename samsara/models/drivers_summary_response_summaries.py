# coding: utf-8

"""
    Samsara API

    # Introduction The Samsara REST API lets you interact with the Samsara Cloud from anything that can send an HTTP request. With the Samsara API you can build powerful applications and custom solutions with sensor data.  Samsara has endpoints available to track and analyze sensors, vehicles, and entire fleets. If you’re familiar with what you can build with a REST API, the following API reference guide will be your go-to resource.  API access to the Samsara cloud is available to all Samsara administrators. If you’d like to try the API, [contact us](https://www.samsara.com/free-trial). The API is currently in beta and may be subject to frequent changes.  # Connecting to the API There are two ways to connect to the API. If you prefer to use the API in Javascript or Python, we supply SDKs which you can download here: [Javascript SDK](https://github.com/samsarahq/samsara-js), [Python SDK](https://github.com/samsarahq/samsara-python).  If you’d rather use another language to interact with the Samsara API, the endpoints and examples are in the reference guide below.  

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DriversSummaryResponseSummaries(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, driver_id=None, driver_name=None, driver_username=None, group_id=None, active_hours=None, distance_miles=None):
        """
        DriversSummaryResponseSummaries - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'driver_id': 'int',
            'driver_name': 'str',
            'driver_username': 'str',
            'group_id': 'int',
            'active_hours': 'float',
            'distance_miles': 'float'
        }

        self.attribute_map = {
            'driver_id': 'driverId',
            'driver_name': 'driverName',
            'driver_username': 'driverUsername',
            'group_id': 'groupId',
            'active_hours': 'activeHours',
            'distance_miles': 'distanceMiles'
        }

        self._driver_id = driver_id
        self._driver_name = driver_name
        self._driver_username = driver_username
        self._group_id = group_id
        self._active_hours = active_hours
        self._distance_miles = distance_miles

    @property
    def driver_id(self):
        """
        Gets the driver_id of this DriversSummaryResponseSummaries.
        ID of the driver.

        :return: The driver_id of this DriversSummaryResponseSummaries.
        :rtype: int
        """
        return self._driver_id

    @driver_id.setter
    def driver_id(self, driver_id):
        """
        Sets the driver_id of this DriversSummaryResponseSummaries.
        ID of the driver.

        :param driver_id: The driver_id of this DriversSummaryResponseSummaries.
        :type: int
        """

        self._driver_id = driver_id

    @property
    def driver_name(self):
        """
        Gets the driver_name of this DriversSummaryResponseSummaries.
        Name of the driver.

        :return: The driver_name of this DriversSummaryResponseSummaries.
        :rtype: str
        """
        return self._driver_name

    @driver_name.setter
    def driver_name(self, driver_name):
        """
        Sets the driver_name of this DriversSummaryResponseSummaries.
        Name of the driver.

        :param driver_name: The driver_name of this DriversSummaryResponseSummaries.
        :type: str
        """

        self._driver_name = driver_name

    @property
    def driver_username(self):
        """
        Gets the driver_username of this DriversSummaryResponseSummaries.
        Username of the driver.

        :return: The driver_username of this DriversSummaryResponseSummaries.
        :rtype: str
        """
        return self._driver_username

    @driver_username.setter
    def driver_username(self, driver_username):
        """
        Sets the driver_username of this DriversSummaryResponseSummaries.
        Username of the driver.

        :param driver_username: The driver_username of this DriversSummaryResponseSummaries.
        :type: str
        """

        self._driver_username = driver_username

    @property
    def group_id(self):
        """
        Gets the group_id of this DriversSummaryResponseSummaries.
        Group of the driver.

        :return: The group_id of this DriversSummaryResponseSummaries.
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this DriversSummaryResponseSummaries.
        Group of the driver.

        :param group_id: The group_id of this DriversSummaryResponseSummaries.
        :type: int
        """

        self._group_id = group_id

    @property
    def active_hours(self):
        """
        Gets the active_hours of this DriversSummaryResponseSummaries.
        Hours spent on duty or driving, rounded to two decimal places.

        :return: The active_hours of this DriversSummaryResponseSummaries.
        :rtype: float
        """
        return self._active_hours

    @active_hours.setter
    def active_hours(self, active_hours):
        """
        Sets the active_hours of this DriversSummaryResponseSummaries.
        Hours spent on duty or driving, rounded to two decimal places.

        :param active_hours: The active_hours of this DriversSummaryResponseSummaries.
        :type: float
        """

        self._active_hours = active_hours

    @property
    def distance_miles(self):
        """
        Gets the distance_miles of this DriversSummaryResponseSummaries.
        Distance driven in miles, rounded to two decimal places.

        :return: The distance_miles of this DriversSummaryResponseSummaries.
        :rtype: float
        """
        return self._distance_miles

    @distance_miles.setter
    def distance_miles(self, distance_miles):
        """
        Sets the distance_miles of this DriversSummaryResponseSummaries.
        Distance driven in miles, rounded to two decimal places.

        :param distance_miles: The distance_miles of this DriversSummaryResponseSummaries.
        :type: float
        """

        self._distance_miles = distance_miles

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, DriversSummaryResponseSummaries):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
