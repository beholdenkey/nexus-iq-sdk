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


class ApiDataRetentionPoliciesDTO(object):
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
        "application_reports": "ApiReportRetentionPoliciesDTO",
        "success_metrics": "ApiSuccessMetricsRetentionPolicyDTO",
    }

    attribute_map = {
        "application_reports": "applicationReports",
        "success_metrics": "successMetrics",
    }

    def __init__(self, application_reports=None, success_metrics=None):  # noqa: E501
        """ApiDataRetentionPoliciesDTO - a model defined in Swagger"""  # noqa: E501
        self._application_reports = None
        self._success_metrics = None
        self.discriminator = None
        if application_reports is not None:
            self.application_reports = application_reports
        if success_metrics is not None:
            self.success_metrics = success_metrics

    @property
    def application_reports(self):
        """Gets the application_reports of this ApiDataRetentionPoliciesDTO.  # noqa: E501


        :return: The application_reports of this ApiDataRetentionPoliciesDTO.  # noqa: E501
        :rtype: ApiReportRetentionPoliciesDTO
        """
        return self._application_reports

    @application_reports.setter
    def application_reports(self, application_reports):
        """Sets the application_reports of this ApiDataRetentionPoliciesDTO.


        :param application_reports: The application_reports of this ApiDataRetentionPoliciesDTO.  # noqa: E501
        :type: ApiReportRetentionPoliciesDTO
        """

        self._application_reports = application_reports

    @property
    def success_metrics(self):
        """Gets the success_metrics of this ApiDataRetentionPoliciesDTO.  # noqa: E501


        :return: The success_metrics of this ApiDataRetentionPoliciesDTO.  # noqa: E501
        :rtype: ApiSuccessMetricsRetentionPolicyDTO
        """
        return self._success_metrics

    @success_metrics.setter
    def success_metrics(self, success_metrics):
        """Sets the success_metrics of this ApiDataRetentionPoliciesDTO.


        :param success_metrics: The success_metrics of this ApiDataRetentionPoliciesDTO.  # noqa: E501
        :type: ApiSuccessMetricsRetentionPolicyDTO
        """

        self._success_metrics = success_metrics

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(ApiDataRetentionPoliciesDTO, dict):
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
        if not isinstance(other, ApiDataRetentionPoliciesDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
