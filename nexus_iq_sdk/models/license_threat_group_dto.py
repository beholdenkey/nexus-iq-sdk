"""
    Sonatype Nexus IQ Server

    This documents the available APIs into [Sonatype Nexus IQ Server](https://www.sonatype.com/products/open-source-security-dependency-management) (also knwon as Nexus Lifecycle).   # noqa: E501

    OpenAPI spec version: 156

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class LicenseThreatGroupDTO:
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
    swagger_types = {'name': 'str', 'threat_level': 'int'}

    attribute_map = {'name': 'name', 'threat_level': 'threatLevel'}

    def __init__(self, name=None, threat_level=None):  # noqa: E501
        """LicenseThreatGroupDTO - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._threat_level = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if threat_level is not None:
            self.threat_level = threat_level

    @property
    def name(self):
        """Gets the name of this LicenseThreatGroupDTO.  # noqa: E501


        :return: The name of this LicenseThreatGroupDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LicenseThreatGroupDTO.


        :param name: The name of this LicenseThreatGroupDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def threat_level(self):
        """Gets the threat_level of this LicenseThreatGroupDTO.  # noqa: E501


        :return: The threat_level of this LicenseThreatGroupDTO.  # noqa: E501
        :rtype: int
        """
        return self._threat_level

    @threat_level.setter
    def threat_level(self, threat_level):
        """Sets the threat_level of this LicenseThreatGroupDTO.


        :param threat_level: The threat_level of this LicenseThreatGroupDTO.  # noqa: E501
        :type: int
        """

        self._threat_level = threat_level

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in self.swagger_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, 'to_dict') else x, value)
                )
            elif hasattr(value, 'to_dict'):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], 'to_dict')
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(LicenseThreatGroupDTO, dict):
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
        if not isinstance(other, LicenseThreatGroupDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
