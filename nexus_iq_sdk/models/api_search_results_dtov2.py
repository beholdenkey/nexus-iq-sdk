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


class ApiSearchResultsDTOV2(object):
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
        "criteria": "ApiSearchCriteriaDTOV2",
        "results": "list[ApiSearchResultDTOV2]",
    }

    attribute_map = {"criteria": "criteria", "results": "results"}

    def __init__(self, criteria=None, results=None):  # noqa: E501
        """ApiSearchResultsDTOV2 - a model defined in Swagger"""  # noqa: E501
        self._criteria = None
        self._results = None
        self.discriminator = None
        if criteria is not None:
            self.criteria = criteria
        if results is not None:
            self.results = results

    @property
    def criteria(self):
        """Gets the criteria of this ApiSearchResultsDTOV2.  # noqa: E501


        :return: The criteria of this ApiSearchResultsDTOV2.  # noqa: E501
        :rtype: ApiSearchCriteriaDTOV2
        """
        return self._criteria

    @criteria.setter
    def criteria(self, criteria):
        """Sets the criteria of this ApiSearchResultsDTOV2.


        :param criteria: The criteria of this ApiSearchResultsDTOV2.  # noqa: E501
        :type: ApiSearchCriteriaDTOV2
        """

        self._criteria = criteria

    @property
    def results(self):
        """Gets the results of this ApiSearchResultsDTOV2.  # noqa: E501


        :return: The results of this ApiSearchResultsDTOV2.  # noqa: E501
        :rtype: list[ApiSearchResultDTOV2]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this ApiSearchResultsDTOV2.


        :param results: The results of this ApiSearchResultsDTOV2.  # noqa: E501
        :type: list[ApiSearchResultDTOV2]
        """

        self._results = results

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
        if issubclass(ApiSearchResultsDTOV2, dict):
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
        if not isinstance(other, ApiSearchResultsDTOV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
