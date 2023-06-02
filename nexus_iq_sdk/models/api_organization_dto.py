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


class ApiOrganizationDTO(object):
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
        "id": "str",
        "name": "str",
        "parent_organization_id": "str",
        "tags": "list[ApiTagDTO]",
    }

    attribute_map = {
        "id": "id",
        "name": "name",
        "parent_organization_id": "parentOrganizationId",
        "tags": "tags",
    }

    def __init__(
        self, id=None, name=None, parent_organization_id=None, tags=None
    ):  # noqa: E501
        """ApiOrganizationDTO - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._parent_organization_id = None
        self._tags = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if parent_organization_id is not None:
            self.parent_organization_id = parent_organization_id
        if tags is not None:
            self.tags = tags

    @property
    def id(self):
        """Gets the id of this ApiOrganizationDTO.  # noqa: E501


        :return: The id of this ApiOrganizationDTO.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiOrganizationDTO.


        :param id: The id of this ApiOrganizationDTO.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ApiOrganizationDTO.  # noqa: E501


        :return: The name of this ApiOrganizationDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiOrganizationDTO.


        :param name: The name of this ApiOrganizationDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def parent_organization_id(self):
        """Gets the parent_organization_id of this ApiOrganizationDTO.  # noqa: E501


        :return: The parent_organization_id of this ApiOrganizationDTO.  # noqa: E501
        :rtype: str
        """
        return self._parent_organization_id

    @parent_organization_id.setter
    def parent_organization_id(self, parent_organization_id):
        """Sets the parent_organization_id of this ApiOrganizationDTO.


        :param parent_organization_id: The parent_organization_id of this ApiOrganizationDTO.  # noqa: E501
        :type: str
        """

        self._parent_organization_id = parent_organization_id

    @property
    def tags(self):
        """Gets the tags of this ApiOrganizationDTO.  # noqa: E501


        :return: The tags of this ApiOrganizationDTO.  # noqa: E501
        :rtype: list[ApiTagDTO]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ApiOrganizationDTO.


        :param tags: The tags of this ApiOrganizationDTO.  # noqa: E501
        :type: list[ApiTagDTO]
        """

        self._tags = tags

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
        if issubclass(ApiOrganizationDTO, dict):
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
        if not isinstance(other, ApiOrganizationDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
