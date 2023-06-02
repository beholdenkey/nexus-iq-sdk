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

class ApiLicenseDataDTOV2(object):
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
        'declared_licenses': 'list[ApiLicenseDTO]',
        'observed_licenses': 'list[ApiLicenseDTO]',
        'effective_licenses': 'list[ApiLicenseDTO]',
        'overridden_licenses': 'list[ApiLicenseDTO]',
        'status': 'str',
        'effective_license_threats': 'list[ApiLicenseThreatDTOV2]'
    }

    attribute_map = {
        'declared_licenses': 'declaredLicenses',
        'observed_licenses': 'observedLicenses',
        'effective_licenses': 'effectiveLicenses',
        'overridden_licenses': 'overriddenLicenses',
        'status': 'status',
        'effective_license_threats': 'effectiveLicenseThreats'
    }

    def __init__(self, declared_licenses=None, observed_licenses=None, effective_licenses=None, overridden_licenses=None, status=None, effective_license_threats=None):  # noqa: E501
        """ApiLicenseDataDTOV2 - a model defined in Swagger"""  # noqa: E501
        self._declared_licenses = None
        self._observed_licenses = None
        self._effective_licenses = None
        self._overridden_licenses = None
        self._status = None
        self._effective_license_threats = None
        self.discriminator = None
        if declared_licenses is not None:
            self.declared_licenses = declared_licenses
        if observed_licenses is not None:
            self.observed_licenses = observed_licenses
        if effective_licenses is not None:
            self.effective_licenses = effective_licenses
        if overridden_licenses is not None:
            self.overridden_licenses = overridden_licenses
        if status is not None:
            self.status = status
        if effective_license_threats is not None:
            self.effective_license_threats = effective_license_threats

    @property
    def declared_licenses(self):
        """Gets the declared_licenses of this ApiLicenseDataDTOV2.  # noqa: E501


        :return: The declared_licenses of this ApiLicenseDataDTOV2.  # noqa: E501
        :rtype: list[ApiLicenseDTO]
        """
        return self._declared_licenses

    @declared_licenses.setter
    def declared_licenses(self, declared_licenses):
        """Sets the declared_licenses of this ApiLicenseDataDTOV2.


        :param declared_licenses: The declared_licenses of this ApiLicenseDataDTOV2.  # noqa: E501
        :type: list[ApiLicenseDTO]
        """

        self._declared_licenses = declared_licenses

    @property
    def observed_licenses(self):
        """Gets the observed_licenses of this ApiLicenseDataDTOV2.  # noqa: E501


        :return: The observed_licenses of this ApiLicenseDataDTOV2.  # noqa: E501
        :rtype: list[ApiLicenseDTO]
        """
        return self._observed_licenses

    @observed_licenses.setter
    def observed_licenses(self, observed_licenses):
        """Sets the observed_licenses of this ApiLicenseDataDTOV2.


        :param observed_licenses: The observed_licenses of this ApiLicenseDataDTOV2.  # noqa: E501
        :type: list[ApiLicenseDTO]
        """

        self._observed_licenses = observed_licenses

    @property
    def effective_licenses(self):
        """Gets the effective_licenses of this ApiLicenseDataDTOV2.  # noqa: E501


        :return: The effective_licenses of this ApiLicenseDataDTOV2.  # noqa: E501
        :rtype: list[ApiLicenseDTO]
        """
        return self._effective_licenses

    @effective_licenses.setter
    def effective_licenses(self, effective_licenses):
        """Sets the effective_licenses of this ApiLicenseDataDTOV2.


        :param effective_licenses: The effective_licenses of this ApiLicenseDataDTOV2.  # noqa: E501
        :type: list[ApiLicenseDTO]
        """

        self._effective_licenses = effective_licenses

    @property
    def overridden_licenses(self):
        """Gets the overridden_licenses of this ApiLicenseDataDTOV2.  # noqa: E501


        :return: The overridden_licenses of this ApiLicenseDataDTOV2.  # noqa: E501
        :rtype: list[ApiLicenseDTO]
        """
        return self._overridden_licenses

    @overridden_licenses.setter
    def overridden_licenses(self, overridden_licenses):
        """Sets the overridden_licenses of this ApiLicenseDataDTOV2.


        :param overridden_licenses: The overridden_licenses of this ApiLicenseDataDTOV2.  # noqa: E501
        :type: list[ApiLicenseDTO]
        """

        self._overridden_licenses = overridden_licenses

    @property
    def status(self):
        """Gets the status of this ApiLicenseDataDTOV2.  # noqa: E501


        :return: The status of this ApiLicenseDataDTOV2.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ApiLicenseDataDTOV2.


        :param status: The status of this ApiLicenseDataDTOV2.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def effective_license_threats(self):
        """Gets the effective_license_threats of this ApiLicenseDataDTOV2.  # noqa: E501


        :return: The effective_license_threats of this ApiLicenseDataDTOV2.  # noqa: E501
        :rtype: list[ApiLicenseThreatDTOV2]
        """
        return self._effective_license_threats

    @effective_license_threats.setter
    def effective_license_threats(self, effective_license_threats):
        """Sets the effective_license_threats of this ApiLicenseDataDTOV2.


        :param effective_license_threats: The effective_license_threats of this ApiLicenseDataDTOV2.  # noqa: E501
        :type: list[ApiLicenseThreatDTOV2]
        """

        self._effective_license_threats = effective_license_threats

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
        if issubclass(ApiLicenseDataDTOV2, dict):
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
        if not isinstance(other, ApiLicenseDataDTOV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
