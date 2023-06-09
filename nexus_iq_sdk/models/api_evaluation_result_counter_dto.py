"""
    Sonatype Nexus IQ Server

    This documents the available APIs into [Sonatype Nexus IQ Server](https://www.sonatype.com/products/open-source-security-dependency-management) (also knwon as Nexus Lifecycle).   # noqa: E501

    OpenAPI spec version: 156

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class ApiEvaluationResultCounterDTO:
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
    swagger_types = {'critical': 'int', 'severe': 'int', 'moderate': 'int'}

    attribute_map = {'critical': 'critical', 'severe': 'severe', 'moderate': 'moderate'}

    def __init__(self, critical=None, severe=None, moderate=None):  # noqa: E501
        """ApiEvaluationResultCounterDTO - a model defined in Swagger"""  # noqa: E501
        self._critical = None
        self._severe = None
        self._moderate = None
        self.discriminator = None
        if critical is not None:
            self.critical = critical
        if severe is not None:
            self.severe = severe
        if moderate is not None:
            self.moderate = moderate

    @property
    def critical(self):
        """Gets the critical of this ApiEvaluationResultCounterDTO.  # noqa: E501


        :return: The critical of this ApiEvaluationResultCounterDTO.  # noqa: E501
        :rtype: int
        """
        return self._critical

    @critical.setter
    def critical(self, critical):
        """Sets the critical of this ApiEvaluationResultCounterDTO.


        :param critical: The critical of this ApiEvaluationResultCounterDTO.  # noqa: E501
        :type: int
        """

        self._critical = critical

    @property
    def severe(self):
        """Gets the severe of this ApiEvaluationResultCounterDTO.  # noqa: E501


        :return: The severe of this ApiEvaluationResultCounterDTO.  # noqa: E501
        :rtype: int
        """
        return self._severe

    @severe.setter
    def severe(self, severe):
        """Sets the severe of this ApiEvaluationResultCounterDTO.


        :param severe: The severe of this ApiEvaluationResultCounterDTO.  # noqa: E501
        :type: int
        """

        self._severe = severe

    @property
    def moderate(self):
        """Gets the moderate of this ApiEvaluationResultCounterDTO.  # noqa: E501


        :return: The moderate of this ApiEvaluationResultCounterDTO.  # noqa: E501
        :rtype: int
        """
        return self._moderate

    @moderate.setter
    def moderate(self, moderate):
        """Sets the moderate of this ApiEvaluationResultCounterDTO.


        :param moderate: The moderate of this ApiEvaluationResultCounterDTO.  # noqa: E501
        :type: int
        """

        self._moderate = moderate

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
        if issubclass(ApiEvaluationResultCounterDTO, dict):
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
        if not isinstance(other, ApiEvaluationResultCounterDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
