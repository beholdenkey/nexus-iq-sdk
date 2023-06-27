"""
    Sonatype Nexus IQ Server

    This documents the available APIs into [Sonatype Nexus IQ Server](https://www.sonatype.com/products/open-source-security-dependency-management) (also knwon as Nexus Lifecycle).   # noqa: E501

    OpenAPI spec version: 156

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class ApiRepositoryComponentsInQuarantineDTO:
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
        'components': 'list[ApiRepositoryComponentPolicyViolationDTO]',
    }

    attribute_map = {'repository': 'repository', 'components': 'components'}

    def __init__(self, repository=None, components=None):  # noqa: E501
        """ApiRepositoryComponentsInQuarantineDTO - a model defined in Swagger"""  # noqa: E501
        self._repository = None
        self._components = None
        self.discriminator = None
        if repository is not None:
            self.repository = repository
        if components is not None:
            self.components = components

    @property
    def repository(self):
        """Gets the repository of this ApiRepositoryComponentsInQuarantineDTO.  # noqa: E501


        :return: The repository of this ApiRepositoryComponentsInQuarantineDTO.  # noqa: E501
        :rtype: ApiRepositoryDTO
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this ApiRepositoryComponentsInQuarantineDTO.


        :param repository: The repository of this ApiRepositoryComponentsInQuarantineDTO.  # noqa: E501
        :type: ApiRepositoryDTO
        """

        self._repository = repository

    @property
    def components(self):
        """Gets the components of this ApiRepositoryComponentsInQuarantineDTO.  # noqa: E501


        :return: The components of this ApiRepositoryComponentsInQuarantineDTO.  # noqa: E501
        :rtype: list[ApiRepositoryComponentPolicyViolationDTO]
        """
        return self._components

    @components.setter
    def components(self, components):
        """Sets the components of this ApiRepositoryComponentsInQuarantineDTO.


        :param components: The components of this ApiRepositoryComponentsInQuarantineDTO.  # noqa: E501
        :type: list[ApiRepositoryComponentPolicyViolationDTO]
        """

        self._components = components

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
        if issubclass(ApiRepositoryComponentsInQuarantineDTO, dict):
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
        if not isinstance(other, ApiRepositoryComponentsInQuarantineDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
