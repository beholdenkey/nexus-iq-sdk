"""
    Sonatype Nexus IQ Server

    This documents the available APIs into [Sonatype Nexus IQ Server](https://www.sonatype.com/products/open-source-security-dependency-management) (also knwon as Nexus Lifecycle).   # noqa: E501

    OpenAPI spec version: 156

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class ApiLicenseThreatDTOV2:
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
        'license_threat_group_name': 'str',
        'license_threat_group_level': 'int',
        'license_threat_group_category': 'str',
    }

    attribute_map = {
        'license_threat_group_name': 'licenseThreatGroupName',
        'license_threat_group_level': 'licenseThreatGroupLevel',
        'license_threat_group_category': 'licenseThreatGroupCategory',
    }

    def __init__(
        self,
        license_threat_group_name=None,
        license_threat_group_level=None,
        license_threat_group_category=None,
    ):  # noqa: E501
        """ApiLicenseThreatDTOV2 - a model defined in Swagger"""  # noqa: E501
        self._license_threat_group_name = None
        self._license_threat_group_level = None
        self._license_threat_group_category = None
        self.discriminator = None
        if license_threat_group_name is not None:
            self.license_threat_group_name = license_threat_group_name
        if license_threat_group_level is not None:
            self.license_threat_group_level = license_threat_group_level
        if license_threat_group_category is not None:
            self.license_threat_group_category = license_threat_group_category

    @property
    def license_threat_group_name(self):
        """Gets the license_threat_group_name of this ApiLicenseThreatDTOV2.  # noqa: E501


        :return: The license_threat_group_name of this ApiLicenseThreatDTOV2.  # noqa: E501
        :rtype: str
        """
        return self._license_threat_group_name

    @license_threat_group_name.setter
    def license_threat_group_name(self, license_threat_group_name):
        """Sets the license_threat_group_name of this ApiLicenseThreatDTOV2.


        :param license_threat_group_name: The license_threat_group_name of this ApiLicenseThreatDTOV2.  # noqa: E501
        :type: str
        """

        self._license_threat_group_name = license_threat_group_name

    @property
    def license_threat_group_level(self):
        """Gets the license_threat_group_level of this ApiLicenseThreatDTOV2.  # noqa: E501


        :return: The license_threat_group_level of this ApiLicenseThreatDTOV2.  # noqa: E501
        :rtype: int
        """
        return self._license_threat_group_level

    @license_threat_group_level.setter
    def license_threat_group_level(self, license_threat_group_level):
        """Sets the license_threat_group_level of this ApiLicenseThreatDTOV2.


        :param license_threat_group_level: The license_threat_group_level of this ApiLicenseThreatDTOV2.  # noqa: E501
        :type: int
        """

        self._license_threat_group_level = license_threat_group_level

    @property
    def license_threat_group_category(self):
        """Gets the license_threat_group_category of this ApiLicenseThreatDTOV2.  # noqa: E501


        :return: The license_threat_group_category of this ApiLicenseThreatDTOV2.  # noqa: E501
        :rtype: str
        """
        return self._license_threat_group_category

    @license_threat_group_category.setter
    def license_threat_group_category(self, license_threat_group_category):
        """Sets the license_threat_group_category of this ApiLicenseThreatDTOV2.


        :param license_threat_group_category: The license_threat_group_category of this ApiLicenseThreatDTOV2.  # noqa: E501
        :type: str
        """

        self._license_threat_group_category = license_threat_group_category

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
        if issubclass(ApiLicenseThreatDTOV2, dict):
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
        if not isinstance(other, ApiLicenseThreatDTOV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
