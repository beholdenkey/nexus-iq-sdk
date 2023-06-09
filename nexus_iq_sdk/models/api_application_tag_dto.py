"""
    Sonatype Nexus IQ Server

    This documents the available APIs into [Sonatype Nexus IQ Server](https://www.sonatype.com/products/open-source-security-dependency-management) (also knwon as Nexus Lifecycle).   # noqa: E501

    OpenAPI spec version: 156

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class ApiApplicationTagDTO:
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
    swagger_types = {'id': 'str', 'tag_id': 'str', 'application_id': 'str'}

    attribute_map = {'id': 'id', 'tag_id': 'tagId', 'application_id': 'applicationId'}

    def __init__(self, id=None, tag_id=None, application_id=None):  # noqa: E501
        """ApiApplicationTagDTO - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._tag_id = None
        self._application_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if tag_id is not None:
            self.tag_id = tag_id
        if application_id is not None:
            self.application_id = application_id

    @property
    def id(self):
        """Gets the id of this ApiApplicationTagDTO.  # noqa: E501


        :return: The id of this ApiApplicationTagDTO.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiApplicationTagDTO.


        :param id: The id of this ApiApplicationTagDTO.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def tag_id(self):
        """Gets the tag_id of this ApiApplicationTagDTO.  # noqa: E501


        :return: The tag_id of this ApiApplicationTagDTO.  # noqa: E501
        :rtype: str
        """
        return self._tag_id

    @tag_id.setter
    def tag_id(self, tag_id):
        """Sets the tag_id of this ApiApplicationTagDTO.


        :param tag_id: The tag_id of this ApiApplicationTagDTO.  # noqa: E501
        :type: str
        """

        self._tag_id = tag_id

    @property
    def application_id(self):
        """Gets the application_id of this ApiApplicationTagDTO.  # noqa: E501


        :return: The application_id of this ApiApplicationTagDTO.  # noqa: E501
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this ApiApplicationTagDTO.


        :param application_id: The application_id of this ApiApplicationTagDTO.  # noqa: E501
        :type: str
        """

        self._application_id = application_id

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
        if issubclass(ApiApplicationTagDTO, dict):
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
        if not isinstance(other, ApiApplicationTagDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
