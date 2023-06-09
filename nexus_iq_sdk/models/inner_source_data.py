"""
    Sonatype Nexus IQ Server

    This documents the available APIs into [Sonatype Nexus IQ Server](https://www.sonatype.com/products/open-source-security-dependency-management) (also knwon as Nexus Lifecycle).   # noqa: E501

    OpenAPI spec version: 156

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class InnerSourceData:
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
        'owner_application_name': 'str',
        'owner_application_id': 'str',
        'inner_source_component_purl': 'str',
    }

    attribute_map = {
        'owner_application_name': 'ownerApplicationName',
        'owner_application_id': 'ownerApplicationId',
        'inner_source_component_purl': 'innerSourceComponentPurl',
    }

    def __init__(
        self,
        owner_application_name=None,
        owner_application_id=None,
        inner_source_component_purl=None,
    ):  # noqa: E501
        """InnerSourceData - a model defined in Swagger"""  # noqa: E501
        self._owner_application_name = None
        self._owner_application_id = None
        self._inner_source_component_purl = None
        self.discriminator = None
        if owner_application_name is not None:
            self.owner_application_name = owner_application_name
        if owner_application_id is not None:
            self.owner_application_id = owner_application_id
        if inner_source_component_purl is not None:
            self.inner_source_component_purl = inner_source_component_purl

    @property
    def owner_application_name(self):
        """Gets the owner_application_name of this InnerSourceData.  # noqa: E501


        :return: The owner_application_name of this InnerSourceData.  # noqa: E501
        :rtype: str
        """
        return self._owner_application_name

    @owner_application_name.setter
    def owner_application_name(self, owner_application_name):
        """Sets the owner_application_name of this InnerSourceData.


        :param owner_application_name: The owner_application_name of this InnerSourceData.  # noqa: E501
        :type: str
        """

        self._owner_application_name = owner_application_name

    @property
    def owner_application_id(self):
        """Gets the owner_application_id of this InnerSourceData.  # noqa: E501


        :return: The owner_application_id of this InnerSourceData.  # noqa: E501
        :rtype: str
        """
        return self._owner_application_id

    @owner_application_id.setter
    def owner_application_id(self, owner_application_id):
        """Sets the owner_application_id of this InnerSourceData.


        :param owner_application_id: The owner_application_id of this InnerSourceData.  # noqa: E501
        :type: str
        """

        self._owner_application_id = owner_application_id

    @property
    def inner_source_component_purl(self):
        """Gets the inner_source_component_purl of this InnerSourceData.  # noqa: E501


        :return: The inner_source_component_purl of this InnerSourceData.  # noqa: E501
        :rtype: str
        """
        return self._inner_source_component_purl

    @inner_source_component_purl.setter
    def inner_source_component_purl(self, inner_source_component_purl):
        """Sets the inner_source_component_purl of this InnerSourceData.


        :param inner_source_component_purl: The inner_source_component_purl of this InnerSourceData.  # noqa: E501
        :type: str
        """

        self._inner_source_component_purl = inner_source_component_purl

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
        if issubclass(InnerSourceData, dict):
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
        if not isinstance(other, InnerSourceData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
