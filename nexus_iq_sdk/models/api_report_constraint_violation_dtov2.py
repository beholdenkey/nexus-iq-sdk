"""
    Sonatype Nexus IQ Server

    This documents the available APIs into [Sonatype Nexus IQ Server](https://www.sonatype.com/products/open-source-security-dependency-management) (also knwon as Nexus Lifecycle).   # noqa: E501

    OpenAPI spec version: 156

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class ApiReportConstraintViolationDTOV2:
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
        'constraint_id': 'str',
        'constraint_name': 'str',
        'conditions': 'list[ApiReportConstraintConditionDTOV2]',
    }

    attribute_map = {
        'constraint_id': 'constraintId',
        'constraint_name': 'constraintName',
        'conditions': 'conditions',
    }

    def __init__(
        self, constraint_id=None, constraint_name=None, conditions=None
    ):  # noqa: E501
        """ApiReportConstraintViolationDTOV2 - a model defined in Swagger"""  # noqa: E501
        self._constraint_id = None
        self._constraint_name = None
        self._conditions = None
        self.discriminator = None
        if constraint_id is not None:
            self.constraint_id = constraint_id
        if constraint_name is not None:
            self.constraint_name = constraint_name
        if conditions is not None:
            self.conditions = conditions

    @property
    def constraint_id(self):
        """Gets the constraint_id of this ApiReportConstraintViolationDTOV2.  # noqa: E501


        :return: The constraint_id of this ApiReportConstraintViolationDTOV2.  # noqa: E501
        :rtype: str
        """
        return self._constraint_id

    @constraint_id.setter
    def constraint_id(self, constraint_id):
        """Sets the constraint_id of this ApiReportConstraintViolationDTOV2.


        :param constraint_id: The constraint_id of this ApiReportConstraintViolationDTOV2.  # noqa: E501
        :type: str
        """

        self._constraint_id = constraint_id

    @property
    def constraint_name(self):
        """Gets the constraint_name of this ApiReportConstraintViolationDTOV2.  # noqa: E501


        :return: The constraint_name of this ApiReportConstraintViolationDTOV2.  # noqa: E501
        :rtype: str
        """
        return self._constraint_name

    @constraint_name.setter
    def constraint_name(self, constraint_name):
        """Sets the constraint_name of this ApiReportConstraintViolationDTOV2.


        :param constraint_name: The constraint_name of this ApiReportConstraintViolationDTOV2.  # noqa: E501
        :type: str
        """

        self._constraint_name = constraint_name

    @property
    def conditions(self):
        """Gets the conditions of this ApiReportConstraintViolationDTOV2.  # noqa: E501


        :return: The conditions of this ApiReportConstraintViolationDTOV2.  # noqa: E501
        :rtype: list[ApiReportConstraintConditionDTOV2]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this ApiReportConstraintViolationDTOV2.


        :param conditions: The conditions of this ApiReportConstraintViolationDTOV2.  # noqa: E501
        :type: list[ApiReportConstraintConditionDTOV2]
        """

        self._conditions = conditions

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
        if issubclass(ApiReportConstraintViolationDTOV2, dict):
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
        if not isinstance(other, ApiReportConstraintViolationDTOV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
