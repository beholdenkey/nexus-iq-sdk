"""
    Sonatype Nexus IQ Server

    This documents the available APIs into [Sonatype Nexus IQ Server](https://www.sonatype.com/products/open-source-security-dependency-management) (also knwon as Nexus Lifecycle).   # noqa: E501

    OpenAPI spec version: 156

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class ApiMemberDTO:
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
        'owner_id': 'str',
        'owner_type': 'str',
        'type': 'str',
        'user_or_group_name': 'str',
    }

    attribute_map = {
        'owner_id': 'ownerId',
        'owner_type': 'ownerType',
        'type': 'type',
        'user_or_group_name': 'userOrGroupName',
    }

    def __init__(
        self, owner_id=None, owner_type=None, type=None, user_or_group_name=None
    ):  # noqa: E501
        """ApiMemberDTO - a model defined in Swagger"""  # noqa: E501
        self._owner_id = None
        self._owner_type = None
        self._type = None
        self._user_or_group_name = None
        self.discriminator = None
        if owner_id is not None:
            self.owner_id = owner_id
        if owner_type is not None:
            self.owner_type = owner_type
        if type is not None:
            self.type = type
        if user_or_group_name is not None:
            self.user_or_group_name = user_or_group_name

    @property
    def owner_id(self):
        """Gets the owner_id of this ApiMemberDTO.  # noqa: E501


        :return: The owner_id of this ApiMemberDTO.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this ApiMemberDTO.


        :param owner_id: The owner_id of this ApiMemberDTO.  # noqa: E501
        :type: str
        """

        self._owner_id = owner_id

    @property
    def owner_type(self):
        """Gets the owner_type of this ApiMemberDTO.  # noqa: E501


        :return: The owner_type of this ApiMemberDTO.  # noqa: E501
        :rtype: str
        """
        return self._owner_type

    @owner_type.setter
    def owner_type(self, owner_type):
        """Sets the owner_type of this ApiMemberDTO.


        :param owner_type: The owner_type of this ApiMemberDTO.  # noqa: E501
        :type: str
        """

        self._owner_type = owner_type

    @property
    def type(self):
        """Gets the type of this ApiMemberDTO.  # noqa: E501


        :return: The type of this ApiMemberDTO.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ApiMemberDTO.


        :param type: The type of this ApiMemberDTO.  # noqa: E501
        :type: str
        """
        allowed_values = ['USER', 'GROUP']  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                'Invalid value for `type` ({}), must be one of {}'.format(  # noqa: E501
                    type, allowed_values
                )
            )

        self._type = type

    @property
    def user_or_group_name(self):
        """Gets the user_or_group_name of this ApiMemberDTO.  # noqa: E501


        :return: The user_or_group_name of this ApiMemberDTO.  # noqa: E501
        :rtype: str
        """
        return self._user_or_group_name

    @user_or_group_name.setter
    def user_or_group_name(self, user_or_group_name):
        """Sets the user_or_group_name of this ApiMemberDTO.


        :param user_or_group_name: The user_or_group_name of this ApiMemberDTO.  # noqa: E501
        :type: str
        """

        self._user_or_group_name = user_or_group_name

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
        if issubclass(ApiMemberDTO, dict):
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
        if not isinstance(other, ApiMemberDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
