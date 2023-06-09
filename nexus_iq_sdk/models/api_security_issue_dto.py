"""
    Sonatype Nexus IQ Server

    This documents the available APIs into [Sonatype Nexus IQ Server](https://www.sonatype.com/products/open-source-security-dependency-management) (also knwon as Nexus Lifecycle).   # noqa: E501

    OpenAPI spec version: 156

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class ApiSecurityIssueDTO:
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
        'source': 'str',
        'reference': 'str',
        'severity': 'float',
        'status': 'str',
        'url': 'str',
        'threat_category': 'str',
        'cwe': 'str',
        'cvss_vector': 'str',
        'cvss_vector_source': 'str',
    }

    attribute_map = {
        'source': 'source',
        'reference': 'reference',
        'severity': 'severity',
        'status': 'status',
        'url': 'url',
        'threat_category': 'threatCategory',
        'cwe': 'cwe',
        'cvss_vector': 'cvssVector',
        'cvss_vector_source': 'cvssVectorSource',
    }

    def __init__(
        self,
        source=None,
        reference=None,
        severity=None,
        status=None,
        url=None,
        threat_category=None,
        cwe=None,
        cvss_vector=None,
        cvss_vector_source=None,
    ):  # noqa: E501
        """ApiSecurityIssueDTO - a model defined in Swagger"""  # noqa: E501
        self._source = None
        self._reference = None
        self._severity = None
        self._status = None
        self._url = None
        self._threat_category = None
        self._cwe = None
        self._cvss_vector = None
        self._cvss_vector_source = None
        self.discriminator = None
        if source is not None:
            self.source = source
        if reference is not None:
            self.reference = reference
        if severity is not None:
            self.severity = severity
        if status is not None:
            self.status = status
        if url is not None:
            self.url = url
        if threat_category is not None:
            self.threat_category = threat_category
        if cwe is not None:
            self.cwe = cwe
        if cvss_vector is not None:
            self.cvss_vector = cvss_vector
        if cvss_vector_source is not None:
            self.cvss_vector_source = cvss_vector_source

    @property
    def source(self):
        """Gets the source of this ApiSecurityIssueDTO.  # noqa: E501


        :return: The source of this ApiSecurityIssueDTO.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this ApiSecurityIssueDTO.


        :param source: The source of this ApiSecurityIssueDTO.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def reference(self):
        """Gets the reference of this ApiSecurityIssueDTO.  # noqa: E501


        :return: The reference of this ApiSecurityIssueDTO.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this ApiSecurityIssueDTO.


        :param reference: The reference of this ApiSecurityIssueDTO.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def severity(self):
        """Gets the severity of this ApiSecurityIssueDTO.  # noqa: E501


        :return: The severity of this ApiSecurityIssueDTO.  # noqa: E501
        :rtype: float
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this ApiSecurityIssueDTO.


        :param severity: The severity of this ApiSecurityIssueDTO.  # noqa: E501
        :type: float
        """

        self._severity = severity

    @property
    def status(self):
        """Gets the status of this ApiSecurityIssueDTO.  # noqa: E501


        :return: The status of this ApiSecurityIssueDTO.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ApiSecurityIssueDTO.


        :param status: The status of this ApiSecurityIssueDTO.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def url(self):
        """Gets the url of this ApiSecurityIssueDTO.  # noqa: E501


        :return: The url of this ApiSecurityIssueDTO.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ApiSecurityIssueDTO.


        :param url: The url of this ApiSecurityIssueDTO.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def threat_category(self):
        """Gets the threat_category of this ApiSecurityIssueDTO.  # noqa: E501


        :return: The threat_category of this ApiSecurityIssueDTO.  # noqa: E501
        :rtype: str
        """
        return self._threat_category

    @threat_category.setter
    def threat_category(self, threat_category):
        """Sets the threat_category of this ApiSecurityIssueDTO.


        :param threat_category: The threat_category of this ApiSecurityIssueDTO.  # noqa: E501
        :type: str
        """

        self._threat_category = threat_category

    @property
    def cwe(self):
        """Gets the cwe of this ApiSecurityIssueDTO.  # noqa: E501


        :return: The cwe of this ApiSecurityIssueDTO.  # noqa: E501
        :rtype: str
        """
        return self._cwe

    @cwe.setter
    def cwe(self, cwe):
        """Sets the cwe of this ApiSecurityIssueDTO.


        :param cwe: The cwe of this ApiSecurityIssueDTO.  # noqa: E501
        :type: str
        """

        self._cwe = cwe

    @property
    def cvss_vector(self):
        """Gets the cvss_vector of this ApiSecurityIssueDTO.  # noqa: E501


        :return: The cvss_vector of this ApiSecurityIssueDTO.  # noqa: E501
        :rtype: str
        """
        return self._cvss_vector

    @cvss_vector.setter
    def cvss_vector(self, cvss_vector):
        """Sets the cvss_vector of this ApiSecurityIssueDTO.


        :param cvss_vector: The cvss_vector of this ApiSecurityIssueDTO.  # noqa: E501
        :type: str
        """

        self._cvss_vector = cvss_vector

    @property
    def cvss_vector_source(self):
        """Gets the cvss_vector_source of this ApiSecurityIssueDTO.  # noqa: E501


        :return: The cvss_vector_source of this ApiSecurityIssueDTO.  # noqa: E501
        :rtype: str
        """
        return self._cvss_vector_source

    @cvss_vector_source.setter
    def cvss_vector_source(self, cvss_vector_source):
        """Sets the cvss_vector_source of this ApiSecurityIssueDTO.


        :param cvss_vector_source: The cvss_vector_source of this ApiSecurityIssueDTO.  # noqa: E501
        :type: str
        """

        self._cvss_vector_source = cvss_vector_source

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
        if issubclass(ApiSecurityIssueDTO, dict):
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
        if not isinstance(other, ApiSecurityIssueDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
