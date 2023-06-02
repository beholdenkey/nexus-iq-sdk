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

class ApiReportComponentPolicyViolationsDTOV2(object):
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
        'hash': 'str',
        'sha256': 'str',
        'component_identifier': 'ApiComponentIdentifierDTOV2',
        'display_name': 'str',
        'proprietary': 'bool',
        'third_party': 'bool',
        'match_state': 'str',
        'pathnames': 'list[str]',
        'dependency_data': 'ApiDependencyDataDTO',
        'violations': 'list[ApiReportPolicyViolationDTOV2]'
    }

    attribute_map = {
        'package_url': 'packageUrl',
        'hash': 'hash',
        'sha256': 'sha256',
        'component_identifier': 'componentIdentifier',
        'display_name': 'displayName',
        'proprietary': 'proprietary',
        'third_party': 'thirdParty',
        'match_state': 'matchState',
        'pathnames': 'pathnames',
        'dependency_data': 'dependencyData',
        'violations': 'violations'
    }

    def __init__(self, package_url=None, hash=None, sha256=None, component_identifier=None, display_name=None, proprietary=None, third_party=None, match_state=None, pathnames=None, dependency_data=None, violations=None):  # noqa: E501
        """ApiReportComponentPolicyViolationsDTOV2 - a model defined in Swagger"""  # noqa: E501
        self._package_url = None
        self._hash = None
        self._sha256 = None
        self._component_identifier = None
        self._display_name = None
        self._proprietary = None
        self._third_party = None
        self._match_state = None
        self._pathnames = None
        self._dependency_data = None
        self._violations = None
        self.discriminator = None
        if package_url is not None:
            self.package_url = package_url
        if hash is not None:
            self.hash = hash
        if sha256 is not None:
            self.sha256 = sha256
        if component_identifier is not None:
            self.component_identifier = component_identifier
        if display_name is not None:
            self.display_name = display_name
        if proprietary is not None:
            self.proprietary = proprietary
        if third_party is not None:
            self.third_party = third_party
        if match_state is not None:
            self.match_state = match_state
        if pathnames is not None:
            self.pathnames = pathnames
        if dependency_data is not None:
            self.dependency_data = dependency_data
        if violations is not None:
            self.violations = violations

    @property
    def package_url(self):
        """Gets the package_url of this ApiReportComponentPolicyViolationsDTOV2.  # noqa: E501


        :return: The package_url of this ApiReportComponentPolicyViolationsDTOV2.  # noqa: E501
        :rtype: str
        """
        return self._package_url

    @package_url.setter
    def package_url(self, package_url):
        """Sets the package_url of this ApiReportComponentPolicyViolationsDTOV2.


        :param package_url: The package_url of this ApiReportComponentPolicyViolationsDTOV2.  # noqa: E501
        :type: str
        """

        self._package_url = package_url

    @property
    def hash(self):
        """Gets the hash of this ApiReportComponentPolicyViolationsDTOV2.  # noqa: E501


        :return: The hash of this ApiReportComponentPolicyViolationsDTOV2.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this ApiReportComponentPolicyViolationsDTOV2.


        :param hash: The hash of this ApiReportComponentPolicyViolationsDTOV2.  # noqa: E501
        :type: str
        """

        self._hash = hash

    @property
    def sha256(self):
        """Gets the sha256 of this ApiReportComponentPolicyViolationsDTOV2.  # noqa: E501


        :return: The sha256 of this ApiReportComponentPolicyViolationsDTOV2.  # noqa: E501
        :rtype: str
        """
        return self._sha256

    @sha256.setter
    def sha256(self, sha256):
        """Sets the sha256 of this ApiReportComponentPolicyViolationsDTOV2.


        :param sha256: The sha256 of this ApiReportComponentPolicyViolationsDTOV2.  # noqa: E501
        :type: str
        """

        self._sha256 = sha256

    @property
    def component_identifier(self):
        """Gets the component_identifier of this ApiReportComponentPolicyViolationsDTOV2.  # noqa: E501


        :return: The component_identifier of this ApiReportComponentPolicyViolationsDTOV2.  # noqa: E501
        :rtype: ApiComponentIdentifierDTOV2
        """
        return self._component_identifier

    @component_identifier.setter
    def component_identifier(self, component_identifier):
        """Sets the component_identifier of this ApiReportComponentPolicyViolationsDTOV2.


        :param component_identifier: The component_identifier of this ApiReportComponentPolicyViolationsDTOV2.  # noqa: E501
        :type: ApiComponentIdentifierDTOV2
        """

        self._component_identifier = component_identifier

    @property
    def display_name(self):
        """Gets the display_name of this ApiReportComponentPolicyViolationsDTOV2.  # noqa: E501


        :return: The display_name of this ApiReportComponentPolicyViolationsDTOV2.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ApiReportComponentPolicyViolationsDTOV2.


        :param display_name: The display_name of this ApiReportComponentPolicyViolationsDTOV2.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def proprietary(self):
        """Gets the proprietary of this ApiReportComponentPolicyViolationsDTOV2.  # noqa: E501


        :return: The proprietary of this ApiReportComponentPolicyViolationsDTOV2.  # noqa: E501
        :rtype: bool
        """
        return self._proprietary

    @proprietary.setter
    def proprietary(self, proprietary):
        """Sets the proprietary of this ApiReportComponentPolicyViolationsDTOV2.


        :param proprietary: The proprietary of this ApiReportComponentPolicyViolationsDTOV2.  # noqa: E501
        :type: bool
        """

        self._proprietary = proprietary

    @property
    def third_party(self):
        """Gets the third_party of this ApiReportComponentPolicyViolationsDTOV2.  # noqa: E501


        :return: The third_party of this ApiReportComponentPolicyViolationsDTOV2.  # noqa: E501
        :rtype: bool
        """
        return self._third_party

    @third_party.setter
    def third_party(self, third_party):
        """Sets the third_party of this ApiReportComponentPolicyViolationsDTOV2.


        :param third_party: The third_party of this ApiReportComponentPolicyViolationsDTOV2.  # noqa: E501
        :type: bool
        """

        self._third_party = third_party

    @property
    def match_state(self):
        """Gets the match_state of this ApiReportComponentPolicyViolationsDTOV2.  # noqa: E501


        :return: The match_state of this ApiReportComponentPolicyViolationsDTOV2.  # noqa: E501
        :rtype: str
        """
        return self._match_state

    @match_state.setter
    def match_state(self, match_state):
        """Sets the match_state of this ApiReportComponentPolicyViolationsDTOV2.


        :param match_state: The match_state of this ApiReportComponentPolicyViolationsDTOV2.  # noqa: E501
        :type: str
        """

        self._match_state = match_state

    @property
    def pathnames(self):
        """Gets the pathnames of this ApiReportComponentPolicyViolationsDTOV2.  # noqa: E501


        :return: The pathnames of this ApiReportComponentPolicyViolationsDTOV2.  # noqa: E501
        :rtype: list[str]
        """
        return self._pathnames

    @pathnames.setter
    def pathnames(self, pathnames):
        """Sets the pathnames of this ApiReportComponentPolicyViolationsDTOV2.


        :param pathnames: The pathnames of this ApiReportComponentPolicyViolationsDTOV2.  # noqa: E501
        :type: list[str]
        """

        self._pathnames = pathnames

    @property
    def dependency_data(self):
        """Gets the dependency_data of this ApiReportComponentPolicyViolationsDTOV2.  # noqa: E501


        :return: The dependency_data of this ApiReportComponentPolicyViolationsDTOV2.  # noqa: E501
        :rtype: ApiDependencyDataDTO
        """
        return self._dependency_data

    @dependency_data.setter
    def dependency_data(self, dependency_data):
        """Sets the dependency_data of this ApiReportComponentPolicyViolationsDTOV2.


        :param dependency_data: The dependency_data of this ApiReportComponentPolicyViolationsDTOV2.  # noqa: E501
        :type: ApiDependencyDataDTO
        """

        self._dependency_data = dependency_data

    @property
    def violations(self):
        """Gets the violations of this ApiReportComponentPolicyViolationsDTOV2.  # noqa: E501


        :return: The violations of this ApiReportComponentPolicyViolationsDTOV2.  # noqa: E501
        :rtype: list[ApiReportPolicyViolationDTOV2]
        """
        return self._violations

    @violations.setter
    def violations(self, violations):
        """Sets the violations of this ApiReportComponentPolicyViolationsDTOV2.


        :param violations: The violations of this ApiReportComponentPolicyViolationsDTOV2.  # noqa: E501
        :type: list[ApiReportPolicyViolationDTOV2]
        """

        self._violations = violations

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
        if issubclass(ApiReportComponentPolicyViolationsDTOV2, dict):
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
        if not isinstance(other, ApiReportComponentPolicyViolationsDTOV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
