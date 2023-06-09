"""
    Sonatype Nexus IQ Server

    This documents the available APIs into [Sonatype Nexus IQ Server](https://www.sonatype.com/products/open-source-security-dependency-management) (also knwon as Nexus Lifecycle).   # noqa: E501

    OpenAPI spec version: 156

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class ApiStaleWaiversResponseDTO:
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
    swagger_types = {'stale_waivers': 'list[ApiStaleWaiverDTO]'}

    attribute_map = {'stale_waivers': 'staleWaivers'}

    def __init__(self, stale_waivers=None):  # noqa: E501
        """ApiStaleWaiversResponseDTO - a model defined in Swagger"""  # noqa: E501
        self._stale_waivers = None
        self.discriminator = None
        if stale_waivers is not None:
            self.stale_waivers = stale_waivers

    @property
    def stale_waivers(self):
        """Gets the stale_waivers of this ApiStaleWaiversResponseDTO.  # noqa: E501


        :return: The stale_waivers of this ApiStaleWaiversResponseDTO.  # noqa: E501
        :rtype: list[ApiStaleWaiverDTO]
        """
        return self._stale_waivers

    @stale_waivers.setter
    def stale_waivers(self, stale_waivers):
        """Sets the stale_waivers of this ApiStaleWaiversResponseDTO.


        :param stale_waivers: The stale_waivers of this ApiStaleWaiversResponseDTO.  # noqa: E501
        :type: list[ApiStaleWaiverDTO]
        """

        self._stale_waivers = stale_waivers

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
        if issubclass(ApiStaleWaiversResponseDTO, dict):
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
        if not isinstance(other, ApiStaleWaiversResponseDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
