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

class ApiVersionChangeOptionDTO(object):
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
    swagger_types = {
        'type': 'str',
        'data': 'ApiComponentChangeActionDTO'
    }

    attribute_map = {
        'type': 'type',
        'data': 'data'
    }

    def __init__(self, type=None, data=None):  # noqa: E501
        """ApiVersionChangeOptionDTO - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._data = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if data is not None:
            self.data = data

    @property
    def type(self):
        """Gets the type of this ApiVersionChangeOptionDTO.  # noqa: E501


        :return: The type of this ApiVersionChangeOptionDTO.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ApiVersionChangeOptionDTO.


        :param type: The type of this ApiVersionChangeOptionDTO.  # noqa: E501
        :type: str
        """
        allowed_values = ["next-no-violations", "next-non-failing", "next-no-violations-with-dependencies", "next-non-failing-with-dependencies"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def data(self):
        """Gets the data of this ApiVersionChangeOptionDTO.  # noqa: E501


        :return: The data of this ApiVersionChangeOptionDTO.  # noqa: E501
        :rtype: ApiComponentChangeActionDTO
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ApiVersionChangeOptionDTO.


        :param data: The data of this ApiVersionChangeOptionDTO.  # noqa: E501
        :type: ApiComponentChangeActionDTO
        """

        self._data = data

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ApiVersionChangeOptionDTO, dict):
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
        if not isinstance(other, ApiVersionChangeOptionDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
