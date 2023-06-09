"""
    Sonatype Nexus IQ Server

    This documents the available APIs into [Sonatype Nexus IQ Server](https://www.sonatype.com/products/open-source-security-dependency-management) (also knwon as Nexus Lifecycle).   # noqa: E501

    OpenAPI spec version: 156

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class ComponentObligationAttributionDTO:
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
        'id': 'str',
        'component_identifier': 'ApiComponentIdentifierDTOV2',
        'package_url': 'str',
        'owner_id': 'str',
        'obligation_name': 'str',
        'content': 'str',
        'last_updated_at': 'datetime',
        'last_updated_by_username': 'str',
    }

    attribute_map = {
        'id': 'id',
        'component_identifier': 'componentIdentifier',
        'package_url': 'packageUrl',
        'owner_id': 'ownerId',
        'obligation_name': 'obligationName',
        'content': 'content',
        'last_updated_at': 'lastUpdatedAt',
        'last_updated_by_username': 'lastUpdatedByUsername',
    }

    def __init__(
        self,
        id=None,
        component_identifier=None,
        package_url=None,
        owner_id=None,
        obligation_name=None,
        content=None,
        last_updated_at=None,
        last_updated_by_username=None,
    ):  # noqa: E501
        """ComponentObligationAttributionDTO - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._component_identifier = None
        self._package_url = None
        self._owner_id = None
        self._obligation_name = None
        self._content = None
        self._last_updated_at = None
        self._last_updated_by_username = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if component_identifier is not None:
            self.component_identifier = component_identifier
        if package_url is not None:
            self.package_url = package_url
        if owner_id is not None:
            self.owner_id = owner_id
        if obligation_name is not None:
            self.obligation_name = obligation_name
        if content is not None:
            self.content = content
        if last_updated_at is not None:
            self.last_updated_at = last_updated_at
        if last_updated_by_username is not None:
            self.last_updated_by_username = last_updated_by_username

    @property
    def id(self):
        """Gets the id of this ComponentObligationAttributionDTO.  # noqa: E501


        :return: The id of this ComponentObligationAttributionDTO.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ComponentObligationAttributionDTO.


        :param id: The id of this ComponentObligationAttributionDTO.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def component_identifier(self):
        """Gets the component_identifier of this ComponentObligationAttributionDTO.  # noqa: E501


        :return: The component_identifier of this ComponentObligationAttributionDTO.  # noqa: E501
        :rtype: ApiComponentIdentifierDTOV2
        """
        return self._component_identifier

    @component_identifier.setter
    def component_identifier(self, component_identifier):
        """Sets the component_identifier of this ComponentObligationAttributionDTO.


        :param component_identifier: The component_identifier of this ComponentObligationAttributionDTO.  # noqa: E501
        :type: ApiComponentIdentifierDTOV2
        """

        self._component_identifier = component_identifier

    @property
    def package_url(self):
        """Gets the package_url of this ComponentObligationAttributionDTO.  # noqa: E501


        :return: The package_url of this ComponentObligationAttributionDTO.  # noqa: E501
        :rtype: str
        """
        return self._package_url

    @package_url.setter
    def package_url(self, package_url):
        """Sets the package_url of this ComponentObligationAttributionDTO.


        :param package_url: The package_url of this ComponentObligationAttributionDTO.  # noqa: E501
        :type: str
        """

        self._package_url = package_url

    @property
    def owner_id(self):
        """Gets the owner_id of this ComponentObligationAttributionDTO.  # noqa: E501


        :return: The owner_id of this ComponentObligationAttributionDTO.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this ComponentObligationAttributionDTO.


        :param owner_id: The owner_id of this ComponentObligationAttributionDTO.  # noqa: E501
        :type: str
        """

        self._owner_id = owner_id

    @property
    def obligation_name(self):
        """Gets the obligation_name of this ComponentObligationAttributionDTO.  # noqa: E501


        :return: The obligation_name of this ComponentObligationAttributionDTO.  # noqa: E501
        :rtype: str
        """
        return self._obligation_name

    @obligation_name.setter
    def obligation_name(self, obligation_name):
        """Sets the obligation_name of this ComponentObligationAttributionDTO.


        :param obligation_name: The obligation_name of this ComponentObligationAttributionDTO.  # noqa: E501
        :type: str
        """

        self._obligation_name = obligation_name

    @property
    def content(self):
        """Gets the content of this ComponentObligationAttributionDTO.  # noqa: E501


        :return: The content of this ComponentObligationAttributionDTO.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ComponentObligationAttributionDTO.


        :param content: The content of this ComponentObligationAttributionDTO.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def last_updated_at(self):
        """Gets the last_updated_at of this ComponentObligationAttributionDTO.  # noqa: E501


        :return: The last_updated_at of this ComponentObligationAttributionDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated_at

    @last_updated_at.setter
    def last_updated_at(self, last_updated_at):
        """Sets the last_updated_at of this ComponentObligationAttributionDTO.


        :param last_updated_at: The last_updated_at of this ComponentObligationAttributionDTO.  # noqa: E501
        :type: datetime
        """

        self._last_updated_at = last_updated_at

    @property
    def last_updated_by_username(self):
        """Gets the last_updated_by_username of this ComponentObligationAttributionDTO.  # noqa: E501


        :return: The last_updated_by_username of this ComponentObligationAttributionDTO.  # noqa: E501
        :rtype: str
        """
        return self._last_updated_by_username

    @last_updated_by_username.setter
    def last_updated_by_username(self, last_updated_by_username):
        """Sets the last_updated_by_username of this ComponentObligationAttributionDTO.


        :param last_updated_by_username: The last_updated_by_username of this ComponentObligationAttributionDTO.  # noqa: E501
        :type: str
        """

        self._last_updated_by_username = last_updated_by_username

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
        if issubclass(ComponentObligationAttributionDTO, dict):
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
        if not isinstance(other, ComponentObligationAttributionDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
