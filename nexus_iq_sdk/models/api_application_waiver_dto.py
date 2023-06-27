"""
    Sonatype Nexus IQ Server

    This documents the available APIs into [Sonatype Nexus IQ Server](https://www.sonatype.com/products/open-source-security-dependency-management) (also knwon as Nexus Lifecycle).   # noqa: E501

    OpenAPI spec version: 156

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class ApiApplicationWaiverDTO:
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
        'application': 'ApiApplicationBaseDTO',
        'stages': 'list[ApiPolicyViolationStageDTO]',
    }

    attribute_map = {'application': 'application', 'stages': 'stages'}

    def __init__(self, application=None, stages=None):  # noqa: E501
        """ApiApplicationWaiverDTO - a model defined in Swagger"""  # noqa: E501
        self._application = None
        self._stages = None
        self.discriminator = None
        if application is not None:
            self.application = application
        if stages is not None:
            self.stages = stages

    @property
    def application(self):
        """Gets the application of this ApiApplicationWaiverDTO.  # noqa: E501


        :return: The application of this ApiApplicationWaiverDTO.  # noqa: E501
        :rtype: ApiApplicationBaseDTO
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this ApiApplicationWaiverDTO.


        :param application: The application of this ApiApplicationWaiverDTO.  # noqa: E501
        :type: ApiApplicationBaseDTO
        """

        self._application = application

    @property
    def stages(self):
        """Gets the stages of this ApiApplicationWaiverDTO.  # noqa: E501


        :return: The stages of this ApiApplicationWaiverDTO.  # noqa: E501
        :rtype: list[ApiPolicyViolationStageDTO]
        """
        return self._stages

    @stages.setter
    def stages(self, stages):
        """Sets the stages of this ApiApplicationWaiverDTO.


        :param stages: The stages of this ApiApplicationWaiverDTO.  # noqa: E501
        :type: list[ApiPolicyViolationStageDTO]
        """

        self._stages = stages

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
        if issubclass(ApiApplicationWaiverDTO, dict):
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
        if not isinstance(other, ApiApplicationWaiverDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
