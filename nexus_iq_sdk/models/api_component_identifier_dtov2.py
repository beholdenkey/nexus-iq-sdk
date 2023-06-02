# coding: utf-8

"""
    Sonatype Nexus IQ Server

    This documents the available APIs into [Sonatype Nexus IQ Server](https://www.sonatype.com/products/open-source-security-dependency-management) (also knwon as Nexus Lifecycle).   # noqa: E501

    OpenAPI spec version: 156
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class ApiComponentIdentifierDTOV2(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {"format": "str", "coordinates": "dict(str, str)"}

    attribute_map = {"format": "format", "coordinates": "coordinates"}

    def __init__(self, format=None, coordinates=None):  # noqa: E501
        """ApiComponentIdentifierDTOV2 - a model defined in Swagger"""  # noqa: E501
        self._format = None
        self._coordinates = None
        self.discriminator = None
        if format is not None:
            self.format = format
        if coordinates is not None:
            self.coordinates = coordinates

    @property
    def format(self):
        """Gets the format of this ApiComponentIdentifierDTOV2.  # noqa: E501


        :return: The format of this ApiComponentIdentifierDTOV2.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this ApiComponentIdentifierDTOV2.


        :param format: The format of this ApiComponentIdentifierDTOV2.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def coordinates(self):
        """Gets the coordinates of this ApiComponentIdentifierDTOV2.  # noqa: E501


        :return: The coordinates of this ApiComponentIdentifierDTOV2.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """Sets the coordinates of this ApiComponentIdentifierDTOV2.


        :param coordinates: The coordinates of this ApiComponentIdentifierDTOV2.  # noqa: E501
        :type: dict(str, str)
        """

        self._coordinates = coordinates

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(ApiComponentIdentifierDTOV2, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ApiComponentIdentifierDTOV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
