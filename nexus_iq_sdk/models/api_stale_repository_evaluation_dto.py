"""
    Sonatype Nexus IQ Server

    This documents the available APIs into [Sonatype Nexus IQ Server](https://www.sonatype.com/products/open-source-security-dependency-management) (also knwon as Nexus Lifecycle).   # noqa: E501

    OpenAPI spec version: 156

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class ApiStaleRepositoryEvaluationDTO:
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
        'repository': 'ApiRepositoryDTO',
        'stages': 'list[ApiStaleEvaluationStageDTO]',
    }

    attribute_map = {'repository': 'repository', 'stages': 'stages'}

    def __init__(self, repository=None, stages=None):  # noqa: E501
        """ApiStaleRepositoryEvaluationDTO - a model defined in Swagger"""  # noqa: E501
        self._repository = None
        self._stages = None
        self.discriminator = None
        if repository is not None:
            self.repository = repository
        if stages is not None:
            self.stages = stages

    @property
    def repository(self):
        """Gets the repository of this ApiStaleRepositoryEvaluationDTO.  # noqa: E501


        :return: The repository of this ApiStaleRepositoryEvaluationDTO.  # noqa: E501
        :rtype: ApiRepositoryDTO
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this ApiStaleRepositoryEvaluationDTO.


        :param repository: The repository of this ApiStaleRepositoryEvaluationDTO.  # noqa: E501
        :type: ApiRepositoryDTO
        """

        self._repository = repository

    @property
    def stages(self):
        """Gets the stages of this ApiStaleRepositoryEvaluationDTO.  # noqa: E501


        :return: The stages of this ApiStaleRepositoryEvaluationDTO.  # noqa: E501
        :rtype: list[ApiStaleEvaluationStageDTO]
        """
        return self._stages

    @stages.setter
    def stages(self, stages):
        """Sets the stages of this ApiStaleRepositoryEvaluationDTO.


        :param stages: The stages of this ApiStaleRepositoryEvaluationDTO.  # noqa: E501
        :type: list[ApiStaleEvaluationStageDTO]
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
        if issubclass(ApiStaleRepositoryEvaluationDTO, dict):
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
        if not isinstance(other, ApiStaleRepositoryEvaluationDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
