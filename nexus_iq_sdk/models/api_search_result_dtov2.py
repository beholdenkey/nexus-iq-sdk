"""
    Sonatype Nexus IQ Server

    This documents the available APIs into [Sonatype Nexus IQ Server](https://www.sonatype.com/products/open-source-security-dependency-management) (also knwon as Nexus Lifecycle).   # noqa: E501

    OpenAPI spec version: 156

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class ApiSearchResultDTOV2:
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
        'application_id': 'str',
        'application_name': 'str',
        'report_html_url': 'str',
        'report_url': 'str',
        'hash': 'str',
        'component_identifier': 'ApiComponentIdentifierDTOV2',
        'package_url': 'str',
        'threat_level': 'int',
        'dependency_data': 'ApiDependencyDataDTO',
    }

    attribute_map = {
        'application_id': 'applicationId',
        'application_name': 'applicationName',
        'report_html_url': 'reportHtmlUrl',
        'report_url': 'reportUrl',
        'hash': 'hash',
        'component_identifier': 'componentIdentifier',
        'package_url': 'packageUrl',
        'threat_level': 'threatLevel',
        'dependency_data': 'dependencyData',
    }

    def __init__(
        self,
        application_id=None,
        application_name=None,
        report_html_url=None,
        report_url=None,
        hash=None,
        component_identifier=None,
        package_url=None,
        threat_level=None,
        dependency_data=None,
    ):  # noqa: E501
        """ApiSearchResultDTOV2 - a model defined in Swagger"""  # noqa: E501
        self._application_id = None
        self._application_name = None
        self._report_html_url = None
        self._report_url = None
        self._hash = None
        self._component_identifier = None
        self._package_url = None
        self._threat_level = None
        self._dependency_data = None
        self.discriminator = None
        if application_id is not None:
            self.application_id = application_id
        if application_name is not None:
            self.application_name = application_name
        if report_html_url is not None:
            self.report_html_url = report_html_url
        if report_url is not None:
            self.report_url = report_url
        if hash is not None:
            self.hash = hash
        if component_identifier is not None:
            self.component_identifier = component_identifier
        if package_url is not None:
            self.package_url = package_url
        if threat_level is not None:
            self.threat_level = threat_level
        if dependency_data is not None:
            self.dependency_data = dependency_data

    @property
    def application_id(self):
        """Gets the application_id of this ApiSearchResultDTOV2.  # noqa: E501


        :return: The application_id of this ApiSearchResultDTOV2.  # noqa: E501
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this ApiSearchResultDTOV2.


        :param application_id: The application_id of this ApiSearchResultDTOV2.  # noqa: E501
        :type: str
        """

        self._application_id = application_id

    @property
    def application_name(self):
        """Gets the application_name of this ApiSearchResultDTOV2.  # noqa: E501


        :return: The application_name of this ApiSearchResultDTOV2.  # noqa: E501
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        """Sets the application_name of this ApiSearchResultDTOV2.


        :param application_name: The application_name of this ApiSearchResultDTOV2.  # noqa: E501
        :type: str
        """

        self._application_name = application_name

    @property
    def report_html_url(self):
        """Gets the report_html_url of this ApiSearchResultDTOV2.  # noqa: E501


        :return: The report_html_url of this ApiSearchResultDTOV2.  # noqa: E501
        :rtype: str
        """
        return self._report_html_url

    @report_html_url.setter
    def report_html_url(self, report_html_url):
        """Sets the report_html_url of this ApiSearchResultDTOV2.


        :param report_html_url: The report_html_url of this ApiSearchResultDTOV2.  # noqa: E501
        :type: str
        """

        self._report_html_url = report_html_url

    @property
    def report_url(self):
        """Gets the report_url of this ApiSearchResultDTOV2.  # noqa: E501


        :return: The report_url of this ApiSearchResultDTOV2.  # noqa: E501
        :rtype: str
        """
        return self._report_url

    @report_url.setter
    def report_url(self, report_url):
        """Sets the report_url of this ApiSearchResultDTOV2.


        :param report_url: The report_url of this ApiSearchResultDTOV2.  # noqa: E501
        :type: str
        """

        self._report_url = report_url

    @property
    def hash(self):
        """Gets the hash of this ApiSearchResultDTOV2.  # noqa: E501


        :return: The hash of this ApiSearchResultDTOV2.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this ApiSearchResultDTOV2.


        :param hash: The hash of this ApiSearchResultDTOV2.  # noqa: E501
        :type: str
        """

        self._hash = hash

    @property
    def component_identifier(self):
        """Gets the component_identifier of this ApiSearchResultDTOV2.  # noqa: E501


        :return: The component_identifier of this ApiSearchResultDTOV2.  # noqa: E501
        :rtype: ApiComponentIdentifierDTOV2
        """
        return self._component_identifier

    @component_identifier.setter
    def component_identifier(self, component_identifier):
        """Sets the component_identifier of this ApiSearchResultDTOV2.


        :param component_identifier: The component_identifier of this ApiSearchResultDTOV2.  # noqa: E501
        :type: ApiComponentIdentifierDTOV2
        """

        self._component_identifier = component_identifier

    @property
    def package_url(self):
        """Gets the package_url of this ApiSearchResultDTOV2.  # noqa: E501


        :return: The package_url of this ApiSearchResultDTOV2.  # noqa: E501
        :rtype: str
        """
        return self._package_url

    @package_url.setter
    def package_url(self, package_url):
        """Sets the package_url of this ApiSearchResultDTOV2.


        :param package_url: The package_url of this ApiSearchResultDTOV2.  # noqa: E501
        :type: str
        """

        self._package_url = package_url

    @property
    def threat_level(self):
        """Gets the threat_level of this ApiSearchResultDTOV2.  # noqa: E501


        :return: The threat_level of this ApiSearchResultDTOV2.  # noqa: E501
        :rtype: int
        """
        return self._threat_level

    @threat_level.setter
    def threat_level(self, threat_level):
        """Sets the threat_level of this ApiSearchResultDTOV2.


        :param threat_level: The threat_level of this ApiSearchResultDTOV2.  # noqa: E501
        :type: int
        """

        self._threat_level = threat_level

    @property
    def dependency_data(self):
        """Gets the dependency_data of this ApiSearchResultDTOV2.  # noqa: E501


        :return: The dependency_data of this ApiSearchResultDTOV2.  # noqa: E501
        :rtype: ApiDependencyDataDTO
        """
        return self._dependency_data

    @dependency_data.setter
    def dependency_data(self, dependency_data):
        """Sets the dependency_data of this ApiSearchResultDTOV2.


        :param dependency_data: The dependency_data of this ApiSearchResultDTOV2.  # noqa: E501
        :type: ApiDependencyDataDTO
        """

        self._dependency_data = dependency_data

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
        if issubclass(ApiSearchResultDTOV2, dict):
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
        if not isinstance(other, ApiSearchResultDTOV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
