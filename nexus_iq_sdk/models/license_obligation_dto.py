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


class LicenseObligationDTO(object):
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
    swagger_types = {"name": "str", "obligation_texts": "list[str]"}

    attribute_map = {"name": "name", "obligation_texts": "obligationTexts"}

    def __init__(self, name=None, obligation_texts=None):  # noqa: E501
        """LicenseObligationDTO - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._obligation_texts = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if obligation_texts is not None:
            self.obligation_texts = obligation_texts

    @property
    def name(self):
        """Gets the name of this LicenseObligationDTO.  # noqa: E501


        :return: The name of this LicenseObligationDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LicenseObligationDTO.


        :param name: The name of this LicenseObligationDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def obligation_texts(self):
        """Gets the obligation_texts of this LicenseObligationDTO.  # noqa: E501


        :return: The obligation_texts of this LicenseObligationDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._obligation_texts

    @obligation_texts.setter
    def obligation_texts(self, obligation_texts):
        """Sets the obligation_texts of this LicenseObligationDTO.


        :param obligation_texts: The obligation_texts of this LicenseObligationDTO.  # noqa: E501
        :type: list[str]
        """

        self._obligation_texts = obligation_texts

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
        if issubclass(LicenseObligationDTO, dict):
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
        if not isinstance(other, LicenseObligationDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
