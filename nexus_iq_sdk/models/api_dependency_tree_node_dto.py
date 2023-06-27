"""
    Sonatype Nexus IQ Server

    This documents the available APIs into [Sonatype Nexus IQ Server](https://www.sonatype.com/products/open-source-security-dependency-management) (also knwon as Nexus Lifecycle).   # noqa: E501

    OpenAPI spec version: 156

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class ApiDependencyTreeNodeDTO:
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
        'package_url': 'str',
        'component_identifier': 'ApiComponentIdentifierDTOV2',
        'children': 'list[ApiDependencyTreeNodeDTO]',
        'direct': 'bool',
    }

    attribute_map = {
        'package_url': 'packageUrl',
        'component_identifier': 'componentIdentifier',
        'children': 'children',
        'direct': 'direct',
    }

    def __init__(
        self, package_url=None, component_identifier=None, children=None, direct=None
    ):  # noqa: E501
        """ApiDependencyTreeNodeDTO - a model defined in Swagger"""  # noqa: E501
        self._package_url = None
        self._component_identifier = None
        self._children = None
        self._direct = None
        self.discriminator = None
        if package_url is not None:
            self.package_url = package_url
        if component_identifier is not None:
            self.component_identifier = component_identifier
        if children is not None:
            self.children = children
        if direct is not None:
            self.direct = direct

    @property
    def package_url(self):
        """Gets the package_url of this ApiDependencyTreeNodeDTO.  # noqa: E501


        :return: The package_url of this ApiDependencyTreeNodeDTO.  # noqa: E501
        :rtype: str
        """
        return self._package_url

    @package_url.setter
    def package_url(self, package_url):
        """Sets the package_url of this ApiDependencyTreeNodeDTO.


        :param package_url: The package_url of this ApiDependencyTreeNodeDTO.  # noqa: E501
        :type: str
        """

        self._package_url = package_url

    @property
    def component_identifier(self):
        """Gets the component_identifier of this ApiDependencyTreeNodeDTO.  # noqa: E501


        :return: The component_identifier of this ApiDependencyTreeNodeDTO.  # noqa: E501
        :rtype: ApiComponentIdentifierDTOV2
        """
        return self._component_identifier

    @component_identifier.setter
    def component_identifier(self, component_identifier):
        """Sets the component_identifier of this ApiDependencyTreeNodeDTO.


        :param component_identifier: The component_identifier of this ApiDependencyTreeNodeDTO.  # noqa: E501
        :type: ApiComponentIdentifierDTOV2
        """

        self._component_identifier = component_identifier

    @property
    def children(self):
        """Gets the children of this ApiDependencyTreeNodeDTO.  # noqa: E501


        :return: The children of this ApiDependencyTreeNodeDTO.  # noqa: E501
        :rtype: list[ApiDependencyTreeNodeDTO]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this ApiDependencyTreeNodeDTO.


        :param children: The children of this ApiDependencyTreeNodeDTO.  # noqa: E501
        :type: list[ApiDependencyTreeNodeDTO]
        """

        self._children = children

    @property
    def direct(self):
        """Gets the direct of this ApiDependencyTreeNodeDTO.  # noqa: E501


        :return: The direct of this ApiDependencyTreeNodeDTO.  # noqa: E501
        :rtype: bool
        """
        return self._direct

    @direct.setter
    def direct(self, direct):
        """Sets the direct of this ApiDependencyTreeNodeDTO.


        :param direct: The direct of this ApiDependencyTreeNodeDTO.  # noqa: E501
        :type: bool
        """

        self._direct = direct

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
        if issubclass(ApiDependencyTreeNodeDTO, dict):
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
        if not isinstance(other, ApiDependencyTreeNodeDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
