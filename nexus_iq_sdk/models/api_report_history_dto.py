"""
    Sonatype Nexus IQ Server

    This documents the available APIs into [Sonatype Nexus IQ Server](https://www.sonatype.com/products/open-source-security-dependency-management) (also knwon as Nexus Lifecycle).   # noqa: E501

    OpenAPI spec version: 156

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class ApiReportHistoryDTO:
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
    swagger_types = {'application_id': 'str', 'reports': 'list[ApiReportResultsDTO]'}

    attribute_map = {'application_id': 'applicationId', 'reports': 'reports'}

    def __init__(self, application_id=None, reports=None):  # noqa: E501
        """ApiReportHistoryDTO - a model defined in Swagger"""  # noqa: E501
        self._application_id = None
        self._reports = None
        self.discriminator = None
        if application_id is not None:
            self.application_id = application_id
        if reports is not None:
            self.reports = reports

    @property
    def application_id(self):
        """Gets the application_id of this ApiReportHistoryDTO.  # noqa: E501


        :return: The application_id of this ApiReportHistoryDTO.  # noqa: E501
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this ApiReportHistoryDTO.


        :param application_id: The application_id of this ApiReportHistoryDTO.  # noqa: E501
        :type: str
        """

        self._application_id = application_id

    @property
    def reports(self):
        """Gets the reports of this ApiReportHistoryDTO.  # noqa: E501


        :return: The reports of this ApiReportHistoryDTO.  # noqa: E501
        :rtype: list[ApiReportResultsDTO]
        """
        return self._reports

    @reports.setter
    def reports(self, reports):
        """Sets the reports of this ApiReportHistoryDTO.


        :param reports: The reports of this ApiReportHistoryDTO.  # noqa: E501
        :type: list[ApiReportResultsDTO]
        """

        self._reports = reports

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
        if issubclass(ApiReportHistoryDTO, dict):
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
        if not isinstance(other, ApiReportHistoryDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
