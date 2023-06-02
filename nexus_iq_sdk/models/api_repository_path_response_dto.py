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

class ApiRepositoryPathResponseDTO(object):
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
        'path_versions': 'list[ApiRepositoryPathVersions]'
    }

    attribute_map = {
        'path_versions': 'pathVersions'
    }

    def __init__(self, path_versions=None):  # noqa: E501
        """ApiRepositoryPathResponseDTO - a model defined in Swagger"""  # noqa: E501
        self._path_versions = None
        self.discriminator = None
        if path_versions is not None:
            self.path_versions = path_versions

    @property
    def path_versions(self):
        """Gets the path_versions of this ApiRepositoryPathResponseDTO.  # noqa: E501


        :return: The path_versions of this ApiRepositoryPathResponseDTO.  # noqa: E501
        :rtype: list[ApiRepositoryPathVersions]
        """
        return self._path_versions

    @path_versions.setter
    def path_versions(self, path_versions):
        """Sets the path_versions of this ApiRepositoryPathResponseDTO.


        :param path_versions: The path_versions of this ApiRepositoryPathResponseDTO.  # noqa: E501
        :type: list[ApiRepositoryPathVersions]
        """

        self._path_versions = path_versions

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
        if issubclass(ApiRepositoryPathResponseDTO, dict):
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
        if not isinstance(other, ApiRepositoryPathResponseDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
