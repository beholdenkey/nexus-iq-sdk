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


class ApiCompositeValueDTOBoolean(object):
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
    swagger_types = {"value": "bool", "parent_value": "bool", "parent_name": "str"}

    attribute_map = {
        "value": "value",
        "parent_value": "parentValue",
        "parent_name": "parentName",
    }

    def __init__(self, value=None, parent_value=None, parent_name=None):  # noqa: E501
        """ApiCompositeValueDTOBoolean - a model defined in Swagger"""  # noqa: E501
        self._value = None
        self._parent_value = None
        self._parent_name = None
        self.discriminator = None
        if value is not None:
            self.value = value
        if parent_value is not None:
            self.parent_value = parent_value
        if parent_name is not None:
            self.parent_name = parent_name

    @property
    def value(self):
        """Gets the value of this ApiCompositeValueDTOBoolean.  # noqa: E501


        :return: The value of this ApiCompositeValueDTOBoolean.  # noqa: E501
        :rtype: bool
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ApiCompositeValueDTOBoolean.


        :param value: The value of this ApiCompositeValueDTOBoolean.  # noqa: E501
        :type: bool
        """

        self._value = value

    @property
    def parent_value(self):
        """Gets the parent_value of this ApiCompositeValueDTOBoolean.  # noqa: E501


        :return: The parent_value of this ApiCompositeValueDTOBoolean.  # noqa: E501
        :rtype: bool
        """
        return self._parent_value

    @parent_value.setter
    def parent_value(self, parent_value):
        """Sets the parent_value of this ApiCompositeValueDTOBoolean.


        :param parent_value: The parent_value of this ApiCompositeValueDTOBoolean.  # noqa: E501
        :type: bool
        """

        self._parent_value = parent_value

    @property
    def parent_name(self):
        """Gets the parent_name of this ApiCompositeValueDTOBoolean.  # noqa: E501


        :return: The parent_name of this ApiCompositeValueDTOBoolean.  # noqa: E501
        :rtype: str
        """
        return self._parent_name

    @parent_name.setter
    def parent_name(self, parent_name):
        """Sets the parent_name of this ApiCompositeValueDTOBoolean.


        :param parent_name: The parent_name of this ApiCompositeValueDTOBoolean.  # noqa: E501
        :type: str
        """

        self._parent_name = parent_name

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
        if issubclass(ApiCompositeValueDTOBoolean, dict):
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
        if not isinstance(other, ApiCompositeValueDTOBoolean):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
