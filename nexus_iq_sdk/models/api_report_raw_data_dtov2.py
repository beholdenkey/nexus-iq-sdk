"""
    Sonatype Nexus IQ Server

    This documents the available APIs into [Sonatype Nexus IQ Server](https://www.sonatype.com/products/open-source-security-dependency-management) (also knwon as Nexus Lifecycle).   # noqa: E501

    OpenAPI spec version: 156

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class ApiReportRawDataDTOV2:
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
        'components': 'list[ApiReportComponentDTOV2]',
        'match_summary': 'ApiMatchStateSummaryDTOV2',
    }

    attribute_map = {'components': 'components', 'match_summary': 'matchSummary'}

    def __init__(self, components=None, match_summary=None):  # noqa: E501
        """ApiReportRawDataDTOV2 - a model defined in Swagger"""  # noqa: E501
        self._components = None
        self._match_summary = None
        self.discriminator = None
        if components is not None:
            self.components = components
        if match_summary is not None:
            self.match_summary = match_summary

    @property
    def components(self):
        """Gets the components of this ApiReportRawDataDTOV2.  # noqa: E501


        :return: The components of this ApiReportRawDataDTOV2.  # noqa: E501
        :rtype: list[ApiReportComponentDTOV2]
        """
        return self._components

    @components.setter
    def components(self, components):
        """Sets the components of this ApiReportRawDataDTOV2.


        :param components: The components of this ApiReportRawDataDTOV2.  # noqa: E501
        :type: list[ApiReportComponentDTOV2]
        """

        self._components = components

    @property
    def match_summary(self):
        """Gets the match_summary of this ApiReportRawDataDTOV2.  # noqa: E501


        :return: The match_summary of this ApiReportRawDataDTOV2.  # noqa: E501
        :rtype: ApiMatchStateSummaryDTOV2
        """
        return self._match_summary

    @match_summary.setter
    def match_summary(self, match_summary):
        """Sets the match_summary of this ApiReportRawDataDTOV2.


        :param match_summary: The match_summary of this ApiReportRawDataDTOV2.  # noqa: E501
        :type: ApiMatchStateSummaryDTOV2
        """

        self._match_summary = match_summary

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
        if issubclass(ApiReportRawDataDTOV2, dict):
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
        if not isinstance(other, ApiReportRawDataDTOV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
