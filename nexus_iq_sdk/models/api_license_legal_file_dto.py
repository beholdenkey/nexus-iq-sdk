"""
    Sonatype Nexus IQ Server

    This documents the available APIs into [Sonatype Nexus IQ Server](https://www.sonatype.com/products/open-source-security-dependency-management) (also knwon as Nexus Lifecycle).   # noqa: E501

    OpenAPI spec version: 156

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class ApiLicenseLegalFileDTO:
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
        'id': 'str',
        'rel_path': 'str',
        'content': 'str',
        'original_content_hash': 'str',
        'status': 'str',
    }

    attribute_map = {
        'id': 'id',
        'rel_path': 'relPath',
        'content': 'content',
        'original_content_hash': 'originalContentHash',
        'status': 'status',
    }

    def __init__(
        self,
        id=None,
        rel_path=None,
        content=None,
        original_content_hash=None,
        status=None,
    ):  # noqa: E501
        """ApiLicenseLegalFileDTO - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._rel_path = None
        self._content = None
        self._original_content_hash = None
        self._status = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if rel_path is not None:
            self.rel_path = rel_path
        if content is not None:
            self.content = content
        if original_content_hash is not None:
            self.original_content_hash = original_content_hash
        if status is not None:
            self.status = status

    @property
    def id(self):
        """Gets the id of this ApiLicenseLegalFileDTO.  # noqa: E501


        :return: The id of this ApiLicenseLegalFileDTO.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiLicenseLegalFileDTO.


        :param id: The id of this ApiLicenseLegalFileDTO.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def rel_path(self):
        """Gets the rel_path of this ApiLicenseLegalFileDTO.  # noqa: E501


        :return: The rel_path of this ApiLicenseLegalFileDTO.  # noqa: E501
        :rtype: str
        """
        return self._rel_path

    @rel_path.setter
    def rel_path(self, rel_path):
        """Sets the rel_path of this ApiLicenseLegalFileDTO.


        :param rel_path: The rel_path of this ApiLicenseLegalFileDTO.  # noqa: E501
        :type: str
        """

        self._rel_path = rel_path

    @property
    def content(self):
        """Gets the content of this ApiLicenseLegalFileDTO.  # noqa: E501


        :return: The content of this ApiLicenseLegalFileDTO.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ApiLicenseLegalFileDTO.


        :param content: The content of this ApiLicenseLegalFileDTO.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def original_content_hash(self):
        """Gets the original_content_hash of this ApiLicenseLegalFileDTO.  # noqa: E501


        :return: The original_content_hash of this ApiLicenseLegalFileDTO.  # noqa: E501
        :rtype: str
        """
        return self._original_content_hash

    @original_content_hash.setter
    def original_content_hash(self, original_content_hash):
        """Sets the original_content_hash of this ApiLicenseLegalFileDTO.


        :param original_content_hash: The original_content_hash of this ApiLicenseLegalFileDTO.  # noqa: E501
        :type: str
        """

        self._original_content_hash = original_content_hash

    @property
    def status(self):
        """Gets the status of this ApiLicenseLegalFileDTO.  # noqa: E501


        :return: The status of this ApiLicenseLegalFileDTO.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ApiLicenseLegalFileDTO.


        :param status: The status of this ApiLicenseLegalFileDTO.  # noqa: E501
        :type: str
        """
        allowed_values = ['enabled', 'disabled']  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                'Invalid value for `status` ({}), must be one of {}'.format(  # noqa: E501
                    status, allowed_values
                )
            )

        self._status = status

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
        if issubclass(ApiLicenseLegalFileDTO, dict):
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
        if not isinstance(other, ApiLicenseLegalFileDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
