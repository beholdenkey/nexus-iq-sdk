"""
    Sonatype Nexus IQ Server

    This documents the available APIs into [Sonatype Nexus IQ Server](https://www.sonatype.com/products/open-source-security-dependency-management) (also knwon as Nexus Lifecycle).   # noqa: E501

    OpenAPI spec version: 156

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class ApiPolicyWaiversApplicableToViolationDTO:
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
        'active_waivers': 'list[ApiPolicyWaiverDTO]',
        'expired_waivers': 'list[ApiPolicyWaiverDTO]',
    }

    attribute_map = {
        'active_waivers': 'activeWaivers',
        'expired_waivers': 'expiredWaivers',
    }

    def __init__(self, active_waivers=None, expired_waivers=None):  # noqa: E501
        """ApiPolicyWaiversApplicableToViolationDTO - a model defined in Swagger"""  # noqa: E501
        self._active_waivers = None
        self._expired_waivers = None
        self.discriminator = None
        if active_waivers is not None:
            self.active_waivers = active_waivers
        if expired_waivers is not None:
            self.expired_waivers = expired_waivers

    @property
    def active_waivers(self):
        """Gets the active_waivers of this ApiPolicyWaiversApplicableToViolationDTO.  # noqa: E501


        :return: The active_waivers of this ApiPolicyWaiversApplicableToViolationDTO.  # noqa: E501
        :rtype: list[ApiPolicyWaiverDTO]
        """
        return self._active_waivers

    @active_waivers.setter
    def active_waivers(self, active_waivers):
        """Sets the active_waivers of this ApiPolicyWaiversApplicableToViolationDTO.


        :param active_waivers: The active_waivers of this ApiPolicyWaiversApplicableToViolationDTO.  # noqa: E501
        :type: list[ApiPolicyWaiverDTO]
        """

        self._active_waivers = active_waivers

    @property
    def expired_waivers(self):
        """Gets the expired_waivers of this ApiPolicyWaiversApplicableToViolationDTO.  # noqa: E501


        :return: The expired_waivers of this ApiPolicyWaiversApplicableToViolationDTO.  # noqa: E501
        :rtype: list[ApiPolicyWaiverDTO]
        """
        return self._expired_waivers

    @expired_waivers.setter
    def expired_waivers(self, expired_waivers):
        """Sets the expired_waivers of this ApiPolicyWaiversApplicableToViolationDTO.


        :param expired_waivers: The expired_waivers of this ApiPolicyWaiversApplicableToViolationDTO.  # noqa: E501
        :type: list[ApiPolicyWaiverDTO]
        """

        self._expired_waivers = expired_waivers

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
        if issubclass(ApiPolicyWaiversApplicableToViolationDTO, dict):
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
        if not isinstance(other, ApiPolicyWaiversApplicableToViolationDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
