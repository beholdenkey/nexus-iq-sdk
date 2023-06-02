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

class ApiFirewallReleaseQuarantineSummaryDTO(object):
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
        'auto_release_quarantine_count_mtd': 'int',
        'auto_release_quarantine_count_ytd': 'int'
    }

    attribute_map = {
        'auto_release_quarantine_count_mtd': 'autoReleaseQuarantineCountMTD',
        'auto_release_quarantine_count_ytd': 'autoReleaseQuarantineCountYTD'
    }

    def __init__(self, auto_release_quarantine_count_mtd=None, auto_release_quarantine_count_ytd=None):  # noqa: E501
        """ApiFirewallReleaseQuarantineSummaryDTO - a model defined in Swagger"""  # noqa: E501
        self._auto_release_quarantine_count_mtd = None
        self._auto_release_quarantine_count_ytd = None
        self.discriminator = None
        if auto_release_quarantine_count_mtd is not None:
            self.auto_release_quarantine_count_mtd = auto_release_quarantine_count_mtd
        if auto_release_quarantine_count_ytd is not None:
            self.auto_release_quarantine_count_ytd = auto_release_quarantine_count_ytd

    @property
    def auto_release_quarantine_count_mtd(self):
        """Gets the auto_release_quarantine_count_mtd of this ApiFirewallReleaseQuarantineSummaryDTO.  # noqa: E501


        :return: The auto_release_quarantine_count_mtd of this ApiFirewallReleaseQuarantineSummaryDTO.  # noqa: E501
        :rtype: int
        """
        return self._auto_release_quarantine_count_mtd

    @auto_release_quarantine_count_mtd.setter
    def auto_release_quarantine_count_mtd(self, auto_release_quarantine_count_mtd):
        """Sets the auto_release_quarantine_count_mtd of this ApiFirewallReleaseQuarantineSummaryDTO.


        :param auto_release_quarantine_count_mtd: The auto_release_quarantine_count_mtd of this ApiFirewallReleaseQuarantineSummaryDTO.  # noqa: E501
        :type: int
        """

        self._auto_release_quarantine_count_mtd = auto_release_quarantine_count_mtd

    @property
    def auto_release_quarantine_count_ytd(self):
        """Gets the auto_release_quarantine_count_ytd of this ApiFirewallReleaseQuarantineSummaryDTO.  # noqa: E501


        :return: The auto_release_quarantine_count_ytd of this ApiFirewallReleaseQuarantineSummaryDTO.  # noqa: E501
        :rtype: int
        """
        return self._auto_release_quarantine_count_ytd

    @auto_release_quarantine_count_ytd.setter
    def auto_release_quarantine_count_ytd(self, auto_release_quarantine_count_ytd):
        """Sets the auto_release_quarantine_count_ytd of this ApiFirewallReleaseQuarantineSummaryDTO.


        :param auto_release_quarantine_count_ytd: The auto_release_quarantine_count_ytd of this ApiFirewallReleaseQuarantineSummaryDTO.  # noqa: E501
        :type: int
        """

        self._auto_release_quarantine_count_ytd = auto_release_quarantine_count_ytd

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
        if issubclass(ApiFirewallReleaseQuarantineSummaryDTO, dict):
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
        if not isinstance(other, ApiFirewallReleaseQuarantineSummaryDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
