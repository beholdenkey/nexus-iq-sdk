"""
    Sonatype Nexus IQ Server

    This documents the available APIs into [Sonatype Nexus IQ Server](https://www.sonatype.com/products/open-source-security-dependency-management) (also knwon as Nexus Lifecycle).   # noqa: E501

    OpenAPI spec version: 156

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class ApiRepositoryComponentPath:
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
    swagger_types = {'pathname': 'str', 'quarantine': 'bool'}

    attribute_map = {'pathname': 'pathname', 'quarantine': 'quarantine'}

    def __init__(self, pathname=None, quarantine=None):  # noqa: E501
        """ApiRepositoryComponentPath - a model defined in Swagger"""  # noqa: E501
        self._pathname = None
        self._quarantine = None
        self.discriminator = None
        if pathname is not None:
            self.pathname = pathname
        if quarantine is not None:
            self.quarantine = quarantine

    @property
    def pathname(self):
        """Gets the pathname of this ApiRepositoryComponentPath.  # noqa: E501


        :return: The pathname of this ApiRepositoryComponentPath.  # noqa: E501
        :rtype: str
        """
        return self._pathname

    @pathname.setter
    def pathname(self, pathname):
        """Sets the pathname of this ApiRepositoryComponentPath.


        :param pathname: The pathname of this ApiRepositoryComponentPath.  # noqa: E501
        :type: str
        """

        self._pathname = pathname

    @property
    def quarantine(self):
        """Gets the quarantine of this ApiRepositoryComponentPath.  # noqa: E501


        :return: The quarantine of this ApiRepositoryComponentPath.  # noqa: E501
        :rtype: bool
        """
        return self._quarantine

    @quarantine.setter
    def quarantine(self, quarantine):
        """Sets the quarantine of this ApiRepositoryComponentPath.


        :param quarantine: The quarantine of this ApiRepositoryComponentPath.  # noqa: E501
        :type: bool
        """

        self._quarantine = quarantine

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
        if issubclass(ApiRepositoryComponentPath, dict):
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
        if not isinstance(other, ApiRepositoryComponentPath):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
