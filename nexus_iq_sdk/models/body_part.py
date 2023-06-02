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


class BodyPart(object):
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
        "content_disposition": "ContentDisposition",
        "entity": "object",
        "headers": "dict(str, list[str])",
        "media_type": "BodyPartMediaType",
        "message_body_workers": "MessageBodyWorkers",
        "parent": "MultiPart",
        "providers": "object",
        "parameterized_headers": "dict(str, list[ParameterizedHeader])",
    }

    attribute_map = {
        "content_disposition": "contentDisposition",
        "entity": "entity",
        "headers": "headers",
        "media_type": "mediaType",
        "message_body_workers": "messageBodyWorkers",
        "parent": "parent",
        "providers": "providers",
        "parameterized_headers": "parameterizedHeaders",
    }

    def __init__(
        self,
        content_disposition=None,
        entity=None,
        headers=None,
        media_type=None,
        message_body_workers=None,
        parent=None,
        providers=None,
        parameterized_headers=None,
    ):  # noqa: E501
        """BodyPart - a model defined in Swagger"""  # noqa: E501
        self._content_disposition = None
        self._entity = None
        self._headers = None
        self._media_type = None
        self._message_body_workers = None
        self._parent = None
        self._providers = None
        self._parameterized_headers = None
        self.discriminator = None
        if content_disposition is not None:
            self.content_disposition = content_disposition
        if entity is not None:
            self.entity = entity
        if headers is not None:
            self.headers = headers
        if media_type is not None:
            self.media_type = media_type
        if message_body_workers is not None:
            self.message_body_workers = message_body_workers
        if parent is not None:
            self.parent = parent
        if providers is not None:
            self.providers = providers
        if parameterized_headers is not None:
            self.parameterized_headers = parameterized_headers

    @property
    def content_disposition(self):
        """Gets the content_disposition of this BodyPart.  # noqa: E501


        :return: The content_disposition of this BodyPart.  # noqa: E501
        :rtype: ContentDisposition
        """
        return self._content_disposition

    @content_disposition.setter
    def content_disposition(self, content_disposition):
        """Sets the content_disposition of this BodyPart.


        :param content_disposition: The content_disposition of this BodyPart.  # noqa: E501
        :type: ContentDisposition
        """

        self._content_disposition = content_disposition

    @property
    def entity(self):
        """Gets the entity of this BodyPart.  # noqa: E501


        :return: The entity of this BodyPart.  # noqa: E501
        :rtype: object
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this BodyPart.


        :param entity: The entity of this BodyPart.  # noqa: E501
        :type: object
        """

        self._entity = entity

    @property
    def headers(self):
        """Gets the headers of this BodyPart.  # noqa: E501


        :return: The headers of this BodyPart.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this BodyPart.


        :param headers: The headers of this BodyPart.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._headers = headers

    @property
    def media_type(self):
        """Gets the media_type of this BodyPart.  # noqa: E501


        :return: The media_type of this BodyPart.  # noqa: E501
        :rtype: BodyPartMediaType
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this BodyPart.


        :param media_type: The media_type of this BodyPart.  # noqa: E501
        :type: BodyPartMediaType
        """

        self._media_type = media_type

    @property
    def message_body_workers(self):
        """Gets the message_body_workers of this BodyPart.  # noqa: E501


        :return: The message_body_workers of this BodyPart.  # noqa: E501
        :rtype: MessageBodyWorkers
        """
        return self._message_body_workers

    @message_body_workers.setter
    def message_body_workers(self, message_body_workers):
        """Sets the message_body_workers of this BodyPart.


        :param message_body_workers: The message_body_workers of this BodyPart.  # noqa: E501
        :type: MessageBodyWorkers
        """

        self._message_body_workers = message_body_workers

    @property
    def parent(self):
        """Gets the parent of this BodyPart.  # noqa: E501


        :return: The parent of this BodyPart.  # noqa: E501
        :rtype: MultiPart
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this BodyPart.


        :param parent: The parent of this BodyPart.  # noqa: E501
        :type: MultiPart
        """

        self._parent = parent

    @property
    def providers(self):
        """Gets the providers of this BodyPart.  # noqa: E501


        :return: The providers of this BodyPart.  # noqa: E501
        :rtype: object
        """
        return self._providers

    @providers.setter
    def providers(self, providers):
        """Sets the providers of this BodyPart.


        :param providers: The providers of this BodyPart.  # noqa: E501
        :type: object
        """

        self._providers = providers

    @property
    def parameterized_headers(self):
        """Gets the parameterized_headers of this BodyPart.  # noqa: E501


        :return: The parameterized_headers of this BodyPart.  # noqa: E501
        :rtype: dict(str, list[ParameterizedHeader])
        """
        return self._parameterized_headers

    @parameterized_headers.setter
    def parameterized_headers(self, parameterized_headers):
        """Sets the parameterized_headers of this BodyPart.


        :param parameterized_headers: The parameterized_headers of this BodyPart.  # noqa: E501
        :type: dict(str, list[ParameterizedHeader])
        """

        self._parameterized_headers = parameterized_headers

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
        if issubclass(BodyPart, dict):
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
        if not isinstance(other, BodyPart):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
