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

class ConfigurationValidationResult(object):
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
        'configuration_complete': 'ValidationResult',
        'repo_private': 'ValidationResult',
        'token_permissions': 'ValidationResult',
        'ssh_configuration': 'ValidationResult'
    }

    attribute_map = {
        'configuration_complete': 'configurationComplete',
        'repo_private': 'repoPrivate',
        'token_permissions': 'tokenPermissions',
        'ssh_configuration': 'sshConfiguration'
    }

    def __init__(self, configuration_complete=None, repo_private=None, token_permissions=None, ssh_configuration=None):  # noqa: E501
        """ConfigurationValidationResult - a model defined in Swagger"""  # noqa: E501
        self._configuration_complete = None
        self._repo_private = None
        self._token_permissions = None
        self._ssh_configuration = None
        self.discriminator = None
        if configuration_complete is not None:
            self.configuration_complete = configuration_complete
        if repo_private is not None:
            self.repo_private = repo_private
        if token_permissions is not None:
            self.token_permissions = token_permissions
        if ssh_configuration is not None:
            self.ssh_configuration = ssh_configuration

    @property
    def configuration_complete(self):
        """Gets the configuration_complete of this ConfigurationValidationResult.  # noqa: E501


        :return: The configuration_complete of this ConfigurationValidationResult.  # noqa: E501
        :rtype: ValidationResult
        """
        return self._configuration_complete

    @configuration_complete.setter
    def configuration_complete(self, configuration_complete):
        """Sets the configuration_complete of this ConfigurationValidationResult.


        :param configuration_complete: The configuration_complete of this ConfigurationValidationResult.  # noqa: E501
        :type: ValidationResult
        """

        self._configuration_complete = configuration_complete

    @property
    def repo_private(self):
        """Gets the repo_private of this ConfigurationValidationResult.  # noqa: E501


        :return: The repo_private of this ConfigurationValidationResult.  # noqa: E501
        :rtype: ValidationResult
        """
        return self._repo_private

    @repo_private.setter
    def repo_private(self, repo_private):
        """Sets the repo_private of this ConfigurationValidationResult.


        :param repo_private: The repo_private of this ConfigurationValidationResult.  # noqa: E501
        :type: ValidationResult
        """

        self._repo_private = repo_private

    @property
    def token_permissions(self):
        """Gets the token_permissions of this ConfigurationValidationResult.  # noqa: E501


        :return: The token_permissions of this ConfigurationValidationResult.  # noqa: E501
        :rtype: ValidationResult
        """
        return self._token_permissions

    @token_permissions.setter
    def token_permissions(self, token_permissions):
        """Sets the token_permissions of this ConfigurationValidationResult.


        :param token_permissions: The token_permissions of this ConfigurationValidationResult.  # noqa: E501
        :type: ValidationResult
        """

        self._token_permissions = token_permissions

    @property
    def ssh_configuration(self):
        """Gets the ssh_configuration of this ConfigurationValidationResult.  # noqa: E501


        :return: The ssh_configuration of this ConfigurationValidationResult.  # noqa: E501
        :rtype: ValidationResult
        """
        return self._ssh_configuration

    @ssh_configuration.setter
    def ssh_configuration(self, ssh_configuration):
        """Sets the ssh_configuration of this ConfigurationValidationResult.


        :param ssh_configuration: The ssh_configuration of this ConfigurationValidationResult.  # noqa: E501
        :type: ValidationResult
        """

        self._ssh_configuration = ssh_configuration

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
        if issubclass(ConfigurationValidationResult, dict):
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
        if not isinstance(other, ConfigurationValidationResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
