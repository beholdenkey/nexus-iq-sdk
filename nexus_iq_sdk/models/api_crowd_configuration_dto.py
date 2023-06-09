"""
    Sonatype Nexus IQ Server

    This documents the available APIs into [Sonatype Nexus IQ Server](https://www.sonatype.com/products/open-source-security-dependency-management) (also knwon as Nexus Lifecycle).   # noqa: E501

    OpenAPI spec version: 156

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class ApiCrowdConfigurationDTO:
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
        'server_url': 'str',
        'application_name': 'str',
        'application_password': 'list[str]',
    }

    attribute_map = {
        'server_url': 'serverUrl',
        'application_name': 'applicationName',
        'application_password': 'applicationPassword',
    }

    def __init__(
        self, server_url=None, application_name=None, application_password=None
    ):  # noqa: E501
        """ApiCrowdConfigurationDTO - a model defined in Swagger"""  # noqa: E501
        self._server_url = None
        self._application_name = None
        self._application_password = None
        self.discriminator = None
        if server_url is not None:
            self.server_url = server_url
        if application_name is not None:
            self.application_name = application_name
        if application_password is not None:
            self.application_password = application_password

    @property
    def server_url(self):
        """Gets the server_url of this ApiCrowdConfigurationDTO.  # noqa: E501


        :return: The server_url of this ApiCrowdConfigurationDTO.  # noqa: E501
        :rtype: str
        """
        return self._server_url

    @server_url.setter
    def server_url(self, server_url):
        """Sets the server_url of this ApiCrowdConfigurationDTO.


        :param server_url: The server_url of this ApiCrowdConfigurationDTO.  # noqa: E501
        :type: str
        """

        self._server_url = server_url

    @property
    def application_name(self):
        """Gets the application_name of this ApiCrowdConfigurationDTO.  # noqa: E501


        :return: The application_name of this ApiCrowdConfigurationDTO.  # noqa: E501
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        """Sets the application_name of this ApiCrowdConfigurationDTO.


        :param application_name: The application_name of this ApiCrowdConfigurationDTO.  # noqa: E501
        :type: str
        """

        self._application_name = application_name

    @property
    def application_password(self):
        """Gets the application_password of this ApiCrowdConfigurationDTO.  # noqa: E501


        :return: The application_password of this ApiCrowdConfigurationDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._application_password

    @application_password.setter
    def application_password(self, application_password):
        """Sets the application_password of this ApiCrowdConfigurationDTO.


        :param application_password: The application_password of this ApiCrowdConfigurationDTO.  # noqa: E501
        :type: list[str]
        """

        self._application_password = application_password

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
        if issubclass(ApiCrowdConfigurationDTO, dict):
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
        if not isinstance(other, ApiCrowdConfigurationDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
