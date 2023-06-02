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

class ApiComponentProjectScmMetadataDTO(object):
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
        'stars': 'int',
        'forks': 'int'
    }

    attribute_map = {
        'stars': 'stars',
        'forks': 'forks'
    }

    def __init__(self, stars=None, forks=None):  # noqa: E501
        """ApiComponentProjectScmMetadataDTO - a model defined in Swagger"""  # noqa: E501
        self._stars = None
        self._forks = None
        self.discriminator = None
        if stars is not None:
            self.stars = stars
        if forks is not None:
            self.forks = forks

    @property
    def stars(self):
        """Gets the stars of this ApiComponentProjectScmMetadataDTO.  # noqa: E501


        :return: The stars of this ApiComponentProjectScmMetadataDTO.  # noqa: E501
        :rtype: int
        """
        return self._stars

    @stars.setter
    def stars(self, stars):
        """Sets the stars of this ApiComponentProjectScmMetadataDTO.


        :param stars: The stars of this ApiComponentProjectScmMetadataDTO.  # noqa: E501
        :type: int
        """

        self._stars = stars

    @property
    def forks(self):
        """Gets the forks of this ApiComponentProjectScmMetadataDTO.  # noqa: E501


        :return: The forks of this ApiComponentProjectScmMetadataDTO.  # noqa: E501
        :rtype: int
        """
        return self._forks

    @forks.setter
    def forks(self, forks):
        """Sets the forks of this ApiComponentProjectScmMetadataDTO.


        :param forks: The forks of this ApiComponentProjectScmMetadataDTO.  # noqa: E501
        :type: int
        """

        self._forks = forks

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
        if issubclass(ApiComponentProjectScmMetadataDTO, dict):
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
        if not isinstance(other, ApiComponentProjectScmMetadataDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
