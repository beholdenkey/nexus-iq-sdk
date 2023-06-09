"""
    Sonatype Nexus IQ Server

    This documents the available APIs into [Sonatype Nexus IQ Server](https://www.sonatype.com/products/open-source-security-dependency-management) (also knwon as Nexus Lifecycle).   # noqa: E501

    OpenAPI spec version: 156

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class SearchResultDTO:
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
        'search_query': 'str',
        'page': 'int',
        'page_size': 'int',
        'total_number_of_hits': 'int',
        'is_exact_total_number_of_hits': 'bool',
        'grouping_by_dtos': 'list[GroupingByDTO]',
    }

    attribute_map = {
        'search_query': 'searchQuery',
        'page': 'page',
        'page_size': 'pageSize',
        'total_number_of_hits': 'totalNumberOfHits',
        'is_exact_total_number_of_hits': 'isExactTotalNumberOfHits',
        'grouping_by_dtos': 'groupingByDTOS',
    }

    def __init__(
        self,
        search_query=None,
        page=None,
        page_size=None,
        total_number_of_hits=None,
        is_exact_total_number_of_hits=None,
        grouping_by_dtos=None,
    ):  # noqa: E501
        """SearchResultDTO - a model defined in Swagger"""  # noqa: E501
        self._search_query = None
        self._page = None
        self._page_size = None
        self._total_number_of_hits = None
        self._is_exact_total_number_of_hits = None
        self._grouping_by_dtos = None
        self.discriminator = None
        if search_query is not None:
            self.search_query = search_query
        if page is not None:
            self.page = page
        if page_size is not None:
            self.page_size = page_size
        if total_number_of_hits is not None:
            self.total_number_of_hits = total_number_of_hits
        if is_exact_total_number_of_hits is not None:
            self.is_exact_total_number_of_hits = is_exact_total_number_of_hits
        if grouping_by_dtos is not None:
            self.grouping_by_dtos = grouping_by_dtos

    @property
    def search_query(self):
        """Gets the search_query of this SearchResultDTO.  # noqa: E501


        :return: The search_query of this SearchResultDTO.  # noqa: E501
        :rtype: str
        """
        return self._search_query

    @search_query.setter
    def search_query(self, search_query):
        """Sets the search_query of this SearchResultDTO.


        :param search_query: The search_query of this SearchResultDTO.  # noqa: E501
        :type: str
        """

        self._search_query = search_query

    @property
    def page(self):
        """Gets the page of this SearchResultDTO.  # noqa: E501


        :return: The page of this SearchResultDTO.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this SearchResultDTO.


        :param page: The page of this SearchResultDTO.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def page_size(self):
        """Gets the page_size of this SearchResultDTO.  # noqa: E501


        :return: The page_size of this SearchResultDTO.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this SearchResultDTO.


        :param page_size: The page_size of this SearchResultDTO.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def total_number_of_hits(self):
        """Gets the total_number_of_hits of this SearchResultDTO.  # noqa: E501


        :return: The total_number_of_hits of this SearchResultDTO.  # noqa: E501
        :rtype: int
        """
        return self._total_number_of_hits

    @total_number_of_hits.setter
    def total_number_of_hits(self, total_number_of_hits):
        """Sets the total_number_of_hits of this SearchResultDTO.


        :param total_number_of_hits: The total_number_of_hits of this SearchResultDTO.  # noqa: E501
        :type: int
        """

        self._total_number_of_hits = total_number_of_hits

    @property
    def is_exact_total_number_of_hits(self):
        """Gets the is_exact_total_number_of_hits of this SearchResultDTO.  # noqa: E501


        :return: The is_exact_total_number_of_hits of this SearchResultDTO.  # noqa: E501
        :rtype: bool
        """
        return self._is_exact_total_number_of_hits

    @is_exact_total_number_of_hits.setter
    def is_exact_total_number_of_hits(self, is_exact_total_number_of_hits):
        """Sets the is_exact_total_number_of_hits of this SearchResultDTO.


        :param is_exact_total_number_of_hits: The is_exact_total_number_of_hits of this SearchResultDTO.  # noqa: E501
        :type: bool
        """

        self._is_exact_total_number_of_hits = is_exact_total_number_of_hits

    @property
    def grouping_by_dtos(self):
        """Gets the grouping_by_dtos of this SearchResultDTO.  # noqa: E501


        :return: The grouping_by_dtos of this SearchResultDTO.  # noqa: E501
        :rtype: list[GroupingByDTO]
        """
        return self._grouping_by_dtos

    @grouping_by_dtos.setter
    def grouping_by_dtos(self, grouping_by_dtos):
        """Sets the grouping_by_dtos of this SearchResultDTO.


        :param grouping_by_dtos: The grouping_by_dtos of this SearchResultDTO.  # noqa: E501
        :type: list[GroupingByDTO]
        """

        self._grouping_by_dtos = grouping_by_dtos

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
        if issubclass(SearchResultDTO, dict):
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
        if not isinstance(other, SearchResultDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
