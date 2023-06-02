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

class ApiComponentProjectMetadataDTO(object):
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
        'description': 'str',
        'organization': 'str'
    }

    attribute_map = {
        'description': 'description',
        'organization': 'organization'
    }

    def __init__(self, description=None, organization=None):  # noqa: E501
        """ApiComponentProjectMetadataDTO - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._organization = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if organization is not None:
            self.organization = organization

    @property
    def description(self):
        """Gets the description of this ApiComponentProjectMetadataDTO.  # noqa: E501


        :return: The description of this ApiComponentProjectMetadataDTO.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ApiComponentProjectMetadataDTO.


        :param description: The description of this ApiComponentProjectMetadataDTO.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def organization(self):
        """Gets the organization of this ApiComponentProjectMetadataDTO.  # noqa: E501


        :return: The organization of this ApiComponentProjectMetadataDTO.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this ApiComponentProjectMetadataDTO.


        :param organization: The organization of this ApiComponentProjectMetadataDTO.  # noqa: E501
        :type: str
        """

        self._organization = organization

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
        if issubclass(ApiComponentProjectMetadataDTO, dict):
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
        if not isinstance(other, ApiComponentProjectMetadataDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
