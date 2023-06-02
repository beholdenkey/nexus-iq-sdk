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


class StageData(object):
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
        "most_recent_evaluation_time": "datetime",
        "most_recent_scan_id": "str",
        "action_type_id": "str",
    }

    attribute_map = {
        "most_recent_evaluation_time": "mostRecentEvaluationTime",
        "most_recent_scan_id": "mostRecentScanId",
        "action_type_id": "actionTypeId",
    }

    def __init__(
        self,
        most_recent_evaluation_time=None,
        most_recent_scan_id=None,
        action_type_id=None,
    ):  # noqa: E501
        """StageData - a model defined in Swagger"""  # noqa: E501
        self._most_recent_evaluation_time = None
        self._most_recent_scan_id = None
        self._action_type_id = None
        self.discriminator = None
        if most_recent_evaluation_time is not None:
            self.most_recent_evaluation_time = most_recent_evaluation_time
        if most_recent_scan_id is not None:
            self.most_recent_scan_id = most_recent_scan_id
        if action_type_id is not None:
            self.action_type_id = action_type_id

    @property
    def most_recent_evaluation_time(self):
        """Gets the most_recent_evaluation_time of this StageData.  # noqa: E501


        :return: The most_recent_evaluation_time of this StageData.  # noqa: E501
        :rtype: datetime
        """
        return self._most_recent_evaluation_time

    @most_recent_evaluation_time.setter
    def most_recent_evaluation_time(self, most_recent_evaluation_time):
        """Sets the most_recent_evaluation_time of this StageData.


        :param most_recent_evaluation_time: The most_recent_evaluation_time of this StageData.  # noqa: E501
        :type: datetime
        """

        self._most_recent_evaluation_time = most_recent_evaluation_time

    @property
    def most_recent_scan_id(self):
        """Gets the most_recent_scan_id of this StageData.  # noqa: E501


        :return: The most_recent_scan_id of this StageData.  # noqa: E501
        :rtype: str
        """
        return self._most_recent_scan_id

    @most_recent_scan_id.setter
    def most_recent_scan_id(self, most_recent_scan_id):
        """Sets the most_recent_scan_id of this StageData.


        :param most_recent_scan_id: The most_recent_scan_id of this StageData.  # noqa: E501
        :type: str
        """

        self._most_recent_scan_id = most_recent_scan_id

    @property
    def action_type_id(self):
        """Gets the action_type_id of this StageData.  # noqa: E501


        :return: The action_type_id of this StageData.  # noqa: E501
        :rtype: str
        """
        return self._action_type_id

    @action_type_id.setter
    def action_type_id(self, action_type_id):
        """Sets the action_type_id of this StageData.


        :param action_type_id: The action_type_id of this StageData.  # noqa: E501
        :type: str
        """

        self._action_type_id = action_type_id

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
        if issubclass(StageData, dict):
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
        if not isinstance(other, StageData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
