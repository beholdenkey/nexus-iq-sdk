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

class ApiComponentPolicyViolationDTO(object):
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
        'component': 'ApiComponentDTOV2',
        'waived_policy_violations': 'list[ApiWaivedPolicyViolationDTO]'
    }

    attribute_map = {
        'component': 'component',
        'waived_policy_violations': 'waivedPolicyViolations'
    }

    def __init__(self, component=None, waived_policy_violations=None):  # noqa: E501
        """ApiComponentPolicyViolationDTO - a model defined in Swagger"""  # noqa: E501
        self._component = None
        self._waived_policy_violations = None
        self.discriminator = None
        if component is not None:
            self.component = component
        if waived_policy_violations is not None:
            self.waived_policy_violations = waived_policy_violations

    @property
    def component(self):
        """Gets the component of this ApiComponentPolicyViolationDTO.  # noqa: E501


        :return: The component of this ApiComponentPolicyViolationDTO.  # noqa: E501
        :rtype: ApiComponentDTOV2
        """
        return self._component

    @component.setter
    def component(self, component):
        """Sets the component of this ApiComponentPolicyViolationDTO.


        :param component: The component of this ApiComponentPolicyViolationDTO.  # noqa: E501
        :type: ApiComponentDTOV2
        """

        self._component = component

    @property
    def waived_policy_violations(self):
        """Gets the waived_policy_violations of this ApiComponentPolicyViolationDTO.  # noqa: E501


        :return: The waived_policy_violations of this ApiComponentPolicyViolationDTO.  # noqa: E501
        :rtype: list[ApiWaivedPolicyViolationDTO]
        """
        return self._waived_policy_violations

    @waived_policy_violations.setter
    def waived_policy_violations(self, waived_policy_violations):
        """Sets the waived_policy_violations of this ApiComponentPolicyViolationDTO.


        :param waived_policy_violations: The waived_policy_violations of this ApiComponentPolicyViolationDTO.  # noqa: E501
        :type: list[ApiWaivedPolicyViolationDTO]
        """

        self._waived_policy_violations = waived_policy_violations

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
        if issubclass(ApiComponentPolicyViolationDTO, dict):
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
        if not isinstance(other, ApiComponentPolicyViolationDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
