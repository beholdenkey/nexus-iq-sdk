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


class ApiRepositoryPathVersions(object):
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
        "request_index": "int",
        "repository_component_paths": "list[ApiRepositoryComponentPath]",
    }

    attribute_map = {
        "request_index": "requestIndex",
        "repository_component_paths": "repositoryComponentPaths",
    }

    def __init__(
        self, request_index=None, repository_component_paths=None
    ):  # noqa: E501
        """ApiRepositoryPathVersions - a model defined in Swagger"""  # noqa: E501
        self._request_index = None
        self._repository_component_paths = None
        self.discriminator = None
        if request_index is not None:
            self.request_index = request_index
        if repository_component_paths is not None:
            self.repository_component_paths = repository_component_paths

    @property
    def request_index(self):
        """Gets the request_index of this ApiRepositoryPathVersions.  # noqa: E501


        :return: The request_index of this ApiRepositoryPathVersions.  # noqa: E501
        :rtype: int
        """
        return self._request_index

    @request_index.setter
    def request_index(self, request_index):
        """Sets the request_index of this ApiRepositoryPathVersions.


        :param request_index: The request_index of this ApiRepositoryPathVersions.  # noqa: E501
        :type: int
        """

        self._request_index = request_index

    @property
    def repository_component_paths(self):
        """Gets the repository_component_paths of this ApiRepositoryPathVersions.  # noqa: E501


        :return: The repository_component_paths of this ApiRepositoryPathVersions.  # noqa: E501
        :rtype: list[ApiRepositoryComponentPath]
        """
        return self._repository_component_paths

    @repository_component_paths.setter
    def repository_component_paths(self, repository_component_paths):
        """Sets the repository_component_paths of this ApiRepositoryPathVersions.


        :param repository_component_paths: The repository_component_paths of this ApiRepositoryPathVersions.  # noqa: E501
        :type: list[ApiRepositoryComponentPath]
        """

        self._repository_component_paths = repository_component_paths

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
        if issubclass(ApiRepositoryPathVersions, dict):
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
        if not isinstance(other, ApiRepositoryPathVersions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
