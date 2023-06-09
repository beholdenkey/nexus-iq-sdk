"""
    Sonatype Nexus IQ Server

    This documents the available APIs into [Sonatype Nexus IQ Server](https://www.sonatype.com/products/open-source-security-dependency-management) (also knwon as Nexus Lifecycle).   # noqa: E501

    OpenAPI spec version: 156

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class ApiMoveApplicationResponseDTOV2:
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
    swagger_types = {'warnings': 'list[str]', 'errors': 'list[str]'}

    attribute_map = {'warnings': 'warnings', 'errors': 'errors'}

    def __init__(self, warnings=None, errors=None):  # noqa: E501
        """ApiMoveApplicationResponseDTOV2 - a model defined in Swagger"""  # noqa: E501
        self._warnings = None
        self._errors = None
        self.discriminator = None
        if warnings is not None:
            self.warnings = warnings
        if errors is not None:
            self.errors = errors

    @property
    def warnings(self):
        """Gets the warnings of this ApiMoveApplicationResponseDTOV2.  # noqa: E501


        :return: The warnings of this ApiMoveApplicationResponseDTOV2.  # noqa: E501
        :rtype: list[str]
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this ApiMoveApplicationResponseDTOV2.


        :param warnings: The warnings of this ApiMoveApplicationResponseDTOV2.  # noqa: E501
        :type: list[str]
        """

        self._warnings = warnings

    @property
    def errors(self):
        """Gets the errors of this ApiMoveApplicationResponseDTOV2.  # noqa: E501


        :return: The errors of this ApiMoveApplicationResponseDTOV2.  # noqa: E501
        :rtype: list[str]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this ApiMoveApplicationResponseDTOV2.


        :param errors: The errors of this ApiMoveApplicationResponseDTOV2.  # noqa: E501
        :type: list[str]
        """

        self._errors = errors

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
        if issubclass(ApiMoveApplicationResponseDTOV2, dict):
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
        if not isinstance(other, ApiMoveApplicationResponseDTOV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
