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

class ApiSourceControlDTO(object):
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
        'owner_id': 'str',
        'repository_url': 'str',
        'username': 'str',
        'token': 'str',
        'provider': 'str',
        'base_branch': 'str',
        'enable_pull_requests': 'bool',
        'remediation_pull_requests_enabled': 'bool',
        'enable_status_checks': 'bool',
        'status_checks_enabled': 'bool',
        'pull_request_commenting_enabled': 'bool',
        'source_control_evaluations_enabled': 'bool',
        'source_control_scan_target': 'str',
        'ssh_enabled': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'owner_id': 'ownerId',
        'repository_url': 'repositoryUrl',
        'username': 'username',
        'token': 'token',
        'provider': 'provider',
        'base_branch': 'baseBranch',
        'enable_pull_requests': 'enablePullRequests',
        'remediation_pull_requests_enabled': 'remediationPullRequestsEnabled',
        'enable_status_checks': 'enableStatusChecks',
        'status_checks_enabled': 'statusChecksEnabled',
        'pull_request_commenting_enabled': 'pullRequestCommentingEnabled',
        'source_control_evaluations_enabled': 'sourceControlEvaluationsEnabled',
        'source_control_scan_target': 'sourceControlScanTarget',
        'ssh_enabled': 'sshEnabled'
    }

    def __init__(self, id=None, owner_id=None, repository_url=None, username=None, token=None, provider=None, base_branch=None, enable_pull_requests=None, remediation_pull_requests_enabled=None, enable_status_checks=None, status_checks_enabled=None, pull_request_commenting_enabled=None, source_control_evaluations_enabled=None, source_control_scan_target=None, ssh_enabled=None):  # noqa: E501
        """ApiSourceControlDTO - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._owner_id = None
        self._repository_url = None
        self._username = None
        self._token = None
        self._provider = None
        self._base_branch = None
        self._enable_pull_requests = None
        self._remediation_pull_requests_enabled = None
        self._enable_status_checks = None
        self._status_checks_enabled = None
        self._pull_request_commenting_enabled = None
        self._source_control_evaluations_enabled = None
        self._source_control_scan_target = None
        self._ssh_enabled = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if owner_id is not None:
            self.owner_id = owner_id
        if repository_url is not None:
            self.repository_url = repository_url
        if username is not None:
            self.username = username
        if token is not None:
            self.token = token
        if provider is not None:
            self.provider = provider
        if base_branch is not None:
            self.base_branch = base_branch
        if enable_pull_requests is not None:
            self.enable_pull_requests = enable_pull_requests
        if remediation_pull_requests_enabled is not None:
            self.remediation_pull_requests_enabled = remediation_pull_requests_enabled
        if enable_status_checks is not None:
            self.enable_status_checks = enable_status_checks
        if status_checks_enabled is not None:
            self.status_checks_enabled = status_checks_enabled
        if pull_request_commenting_enabled is not None:
            self.pull_request_commenting_enabled = pull_request_commenting_enabled
        if source_control_evaluations_enabled is not None:
            self.source_control_evaluations_enabled = source_control_evaluations_enabled
        if source_control_scan_target is not None:
            self.source_control_scan_target = source_control_scan_target
        if ssh_enabled is not None:
            self.ssh_enabled = ssh_enabled

    @property
    def id(self):
        """Gets the id of this ApiSourceControlDTO.  # noqa: E501


        :return: The id of this ApiSourceControlDTO.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiSourceControlDTO.


        :param id: The id of this ApiSourceControlDTO.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def owner_id(self):
        """Gets the owner_id of this ApiSourceControlDTO.  # noqa: E501


        :return: The owner_id of this ApiSourceControlDTO.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this ApiSourceControlDTO.


        :param owner_id: The owner_id of this ApiSourceControlDTO.  # noqa: E501
        :type: str
        """

        self._owner_id = owner_id

    @property
    def repository_url(self):
        """Gets the repository_url of this ApiSourceControlDTO.  # noqa: E501


        :return: The repository_url of this ApiSourceControlDTO.  # noqa: E501
        :rtype: str
        """
        return self._repository_url

    @repository_url.setter
    def repository_url(self, repository_url):
        """Sets the repository_url of this ApiSourceControlDTO.


        :param repository_url: The repository_url of this ApiSourceControlDTO.  # noqa: E501
        :type: str
        """

        self._repository_url = repository_url

    @property
    def username(self):
        """Gets the username of this ApiSourceControlDTO.  # noqa: E501


        :return: The username of this ApiSourceControlDTO.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this ApiSourceControlDTO.


        :param username: The username of this ApiSourceControlDTO.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def token(self):
        """Gets the token of this ApiSourceControlDTO.  # noqa: E501


        :return: The token of this ApiSourceControlDTO.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this ApiSourceControlDTO.


        :param token: The token of this ApiSourceControlDTO.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def provider(self):
        """Gets the provider of this ApiSourceControlDTO.  # noqa: E501


        :return: The provider of this ApiSourceControlDTO.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this ApiSourceControlDTO.


        :param provider: The provider of this ApiSourceControlDTO.  # noqa: E501
        :type: str
        """

        self._provider = provider

    @property
    def base_branch(self):
        """Gets the base_branch of this ApiSourceControlDTO.  # noqa: E501


        :return: The base_branch of this ApiSourceControlDTO.  # noqa: E501
        :rtype: str
        """
        return self._base_branch

    @base_branch.setter
    def base_branch(self, base_branch):
        """Sets the base_branch of this ApiSourceControlDTO.


        :param base_branch: The base_branch of this ApiSourceControlDTO.  # noqa: E501
        :type: str
        """

        self._base_branch = base_branch

    @property
    def enable_pull_requests(self):
        """Gets the enable_pull_requests of this ApiSourceControlDTO.  # noqa: E501


        :return: The enable_pull_requests of this ApiSourceControlDTO.  # noqa: E501
        :rtype: bool
        """
        return self._enable_pull_requests

    @enable_pull_requests.setter
    def enable_pull_requests(self, enable_pull_requests):
        """Sets the enable_pull_requests of this ApiSourceControlDTO.


        :param enable_pull_requests: The enable_pull_requests of this ApiSourceControlDTO.  # noqa: E501
        :type: bool
        """

        self._enable_pull_requests = enable_pull_requests

    @property
    def remediation_pull_requests_enabled(self):
        """Gets the remediation_pull_requests_enabled of this ApiSourceControlDTO.  # noqa: E501


        :return: The remediation_pull_requests_enabled of this ApiSourceControlDTO.  # noqa: E501
        :rtype: bool
        """
        return self._remediation_pull_requests_enabled

    @remediation_pull_requests_enabled.setter
    def remediation_pull_requests_enabled(self, remediation_pull_requests_enabled):
        """Sets the remediation_pull_requests_enabled of this ApiSourceControlDTO.


        :param remediation_pull_requests_enabled: The remediation_pull_requests_enabled of this ApiSourceControlDTO.  # noqa: E501
        :type: bool
        """

        self._remediation_pull_requests_enabled = remediation_pull_requests_enabled

    @property
    def enable_status_checks(self):
        """Gets the enable_status_checks of this ApiSourceControlDTO.  # noqa: E501


        :return: The enable_status_checks of this ApiSourceControlDTO.  # noqa: E501
        :rtype: bool
        """
        return self._enable_status_checks

    @enable_status_checks.setter
    def enable_status_checks(self, enable_status_checks):
        """Sets the enable_status_checks of this ApiSourceControlDTO.


        :param enable_status_checks: The enable_status_checks of this ApiSourceControlDTO.  # noqa: E501
        :type: bool
        """

        self._enable_status_checks = enable_status_checks

    @property
    def status_checks_enabled(self):
        """Gets the status_checks_enabled of this ApiSourceControlDTO.  # noqa: E501


        :return: The status_checks_enabled of this ApiSourceControlDTO.  # noqa: E501
        :rtype: bool
        """
        return self._status_checks_enabled

    @status_checks_enabled.setter
    def status_checks_enabled(self, status_checks_enabled):
        """Sets the status_checks_enabled of this ApiSourceControlDTO.


        :param status_checks_enabled: The status_checks_enabled of this ApiSourceControlDTO.  # noqa: E501
        :type: bool
        """

        self._status_checks_enabled = status_checks_enabled

    @property
    def pull_request_commenting_enabled(self):
        """Gets the pull_request_commenting_enabled of this ApiSourceControlDTO.  # noqa: E501


        :return: The pull_request_commenting_enabled of this ApiSourceControlDTO.  # noqa: E501
        :rtype: bool
        """
        return self._pull_request_commenting_enabled

    @pull_request_commenting_enabled.setter
    def pull_request_commenting_enabled(self, pull_request_commenting_enabled):
        """Sets the pull_request_commenting_enabled of this ApiSourceControlDTO.


        :param pull_request_commenting_enabled: The pull_request_commenting_enabled of this ApiSourceControlDTO.  # noqa: E501
        :type: bool
        """

        self._pull_request_commenting_enabled = pull_request_commenting_enabled

    @property
    def source_control_evaluations_enabled(self):
        """Gets the source_control_evaluations_enabled of this ApiSourceControlDTO.  # noqa: E501


        :return: The source_control_evaluations_enabled of this ApiSourceControlDTO.  # noqa: E501
        :rtype: bool
        """
        return self._source_control_evaluations_enabled

    @source_control_evaluations_enabled.setter
    def source_control_evaluations_enabled(self, source_control_evaluations_enabled):
        """Sets the source_control_evaluations_enabled of this ApiSourceControlDTO.


        :param source_control_evaluations_enabled: The source_control_evaluations_enabled of this ApiSourceControlDTO.  # noqa: E501
        :type: bool
        """

        self._source_control_evaluations_enabled = source_control_evaluations_enabled

    @property
    def source_control_scan_target(self):
        """Gets the source_control_scan_target of this ApiSourceControlDTO.  # noqa: E501


        :return: The source_control_scan_target of this ApiSourceControlDTO.  # noqa: E501
        :rtype: str
        """
        return self._source_control_scan_target

    @source_control_scan_target.setter
    def source_control_scan_target(self, source_control_scan_target):
        """Sets the source_control_scan_target of this ApiSourceControlDTO.


        :param source_control_scan_target: The source_control_scan_target of this ApiSourceControlDTO.  # noqa: E501
        :type: str
        """

        self._source_control_scan_target = source_control_scan_target

    @property
    def ssh_enabled(self):
        """Gets the ssh_enabled of this ApiSourceControlDTO.  # noqa: E501


        :return: The ssh_enabled of this ApiSourceControlDTO.  # noqa: E501
        :rtype: bool
        """
        return self._ssh_enabled

    @ssh_enabled.setter
    def ssh_enabled(self, ssh_enabled):
        """Sets the ssh_enabled of this ApiSourceControlDTO.


        :param ssh_enabled: The ssh_enabled of this ApiSourceControlDTO.  # noqa: E501
        :type: bool
        """

        self._ssh_enabled = ssh_enabled

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
        if issubclass(ApiSourceControlDTO, dict):
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
        if not isinstance(other, ApiSourceControlDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
