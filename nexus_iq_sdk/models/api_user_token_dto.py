"""
    Sonatype Nexus IQ Server

    This documents the available APIs into [Sonatype Nexus IQ Server](https://www.sonatype.com/products/open-source-security-dependency-management) (also knwon as Nexus Lifecycle).   # noqa: E501

    OpenAPI spec version: 156

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class ApiUserTokenDTO:
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
        'user_code': 'str',
        'pass_code': 'str',
        'username': 'str',
        'realm': 'str',
    }

    attribute_map = {
        'user_code': 'userCode',
        'pass_code': 'passCode',
        'username': 'username',
        'realm': 'realm',
    }

    def __init__(
        self, user_code=None, pass_code=None, username=None, realm=None
    ):  # noqa: E501
        """ApiUserTokenDTO - a model defined in Swagger"""  # noqa: E501
        self._user_code = None
        self._pass_code = None
        self._username = None
        self._realm = None
        self.discriminator = None
        if user_code is not None:
            self.user_code = user_code
        if pass_code is not None:
            self.pass_code = pass_code
        if username is not None:
            self.username = username
        if realm is not None:
            self.realm = realm

    @property
    def user_code(self):
        """Gets the user_code of this ApiUserTokenDTO.  # noqa: E501


        :return: The user_code of this ApiUserTokenDTO.  # noqa: E501
        :rtype: str
        """
        return self._user_code

    @user_code.setter
    def user_code(self, user_code):
        """Sets the user_code of this ApiUserTokenDTO.


        :param user_code: The user_code of this ApiUserTokenDTO.  # noqa: E501
        :type: str
        """

        self._user_code = user_code

    @property
    def pass_code(self):
        """Gets the pass_code of this ApiUserTokenDTO.  # noqa: E501


        :return: The pass_code of this ApiUserTokenDTO.  # noqa: E501
        :rtype: str
        """
        return self._pass_code

    @pass_code.setter
    def pass_code(self, pass_code):
        """Sets the pass_code of this ApiUserTokenDTO.


        :param pass_code: The pass_code of this ApiUserTokenDTO.  # noqa: E501
        :type: str
        """

        self._pass_code = pass_code

    @property
    def username(self):
        """Gets the username of this ApiUserTokenDTO.  # noqa: E501


        :return: The username of this ApiUserTokenDTO.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this ApiUserTokenDTO.


        :param username: The username of this ApiUserTokenDTO.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def realm(self):
        """Gets the realm of this ApiUserTokenDTO.  # noqa: E501


        :return: The realm of this ApiUserTokenDTO.  # noqa: E501
        :rtype: str
        """
        return self._realm

    @realm.setter
    def realm(self, realm):
        """Sets the realm of this ApiUserTokenDTO.


        :param realm: The realm of this ApiUserTokenDTO.  # noqa: E501
        :type: str
        """

        self._realm = realm

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
        if issubclass(ApiUserTokenDTO, dict):
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
        if not isinstance(other, ApiUserTokenDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
