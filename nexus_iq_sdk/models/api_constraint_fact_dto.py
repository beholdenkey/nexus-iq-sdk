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


class ApiConstraintFactDTO(object):
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
        "constraint_name": "str",
        "constraint_id": "str",
        "reasons": "list[ApiConditionFactReasonDTO]",
    }

    attribute_map = {
        "constraint_name": "constraintName",
        "constraint_id": "constraintId",
        "reasons": "reasons",
    }

    def __init__(
        self, constraint_name=None, constraint_id=None, reasons=None
    ):  # noqa: E501
        """ApiConstraintFactDTO - a model defined in Swagger"""  # noqa: E501
        self._constraint_name = None
        self._constraint_id = None
        self._reasons = None
        self.discriminator = None
        if constraint_name is not None:
            self.constraint_name = constraint_name
        if constraint_id is not None:
            self.constraint_id = constraint_id
        if reasons is not None:
            self.reasons = reasons

    @property
    def constraint_name(self):
        """Gets the constraint_name of this ApiConstraintFactDTO.  # noqa: E501


        :return: The constraint_name of this ApiConstraintFactDTO.  # noqa: E501
        :rtype: str
        """
        return self._constraint_name

    @constraint_name.setter
    def constraint_name(self, constraint_name):
        """Sets the constraint_name of this ApiConstraintFactDTO.


        :param constraint_name: The constraint_name of this ApiConstraintFactDTO.  # noqa: E501
        :type: str
        """

        self._constraint_name = constraint_name

    @property
    def constraint_id(self):
        """Gets the constraint_id of this ApiConstraintFactDTO.  # noqa: E501


        :return: The constraint_id of this ApiConstraintFactDTO.  # noqa: E501
        :rtype: str
        """
        return self._constraint_id

    @constraint_id.setter
    def constraint_id(self, constraint_id):
        """Sets the constraint_id of this ApiConstraintFactDTO.


        :param constraint_id: The constraint_id of this ApiConstraintFactDTO.  # noqa: E501
        :type: str
        """

        self._constraint_id = constraint_id

    @property
    def reasons(self):
        """Gets the reasons of this ApiConstraintFactDTO.  # noqa: E501


        :return: The reasons of this ApiConstraintFactDTO.  # noqa: E501
        :rtype: list[ApiConditionFactReasonDTO]
        """
        return self._reasons

    @reasons.setter
    def reasons(self, reasons):
        """Sets the reasons of this ApiConstraintFactDTO.


        :param reasons: The reasons of this ApiConstraintFactDTO.  # noqa: E501
        :type: list[ApiConditionFactReasonDTO]
        """

        self._reasons = reasons

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
        if issubclass(ApiConstraintFactDTO, dict):
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
        if not isinstance(other, ApiConstraintFactDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
