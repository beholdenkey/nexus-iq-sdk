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


class ApiComponentDetailsDTOV2(object):
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
        "component": "ApiComponentDTOV2",
        "match_state": "str",
        "catalog_date": "datetime",
        "relative_popularity": "int",
        "license_data": "ApiLicenseDataDTO",
        "integrity_rating": "str",
        "hygiene_rating": "str",
        "security_data": "ApiSecurityDataDTO",
        "policy_data": "ApiComponentPolicyViolationListDTOV2",
        "project_data": "ApiComponentProjectDataDTO",
    }

    attribute_map = {
        "component": "component",
        "match_state": "matchState",
        "catalog_date": "catalogDate",
        "relative_popularity": "relativePopularity",
        "license_data": "licenseData",
        "integrity_rating": "integrityRating",
        "hygiene_rating": "hygieneRating",
        "security_data": "securityData",
        "policy_data": "policyData",
        "project_data": "projectData",
    }

    def __init__(
        self,
        component=None,
        match_state=None,
        catalog_date=None,
        relative_popularity=None,
        license_data=None,
        integrity_rating=None,
        hygiene_rating=None,
        security_data=None,
        policy_data=None,
        project_data=None,
    ):  # noqa: E501
        """ApiComponentDetailsDTOV2 - a model defined in Swagger"""  # noqa: E501
        self._component = None
        self._match_state = None
        self._catalog_date = None
        self._relative_popularity = None
        self._license_data = None
        self._integrity_rating = None
        self._hygiene_rating = None
        self._security_data = None
        self._policy_data = None
        self._project_data = None
        self.discriminator = None
        if component is not None:
            self.component = component
        if match_state is not None:
            self.match_state = match_state
        if catalog_date is not None:
            self.catalog_date = catalog_date
        if relative_popularity is not None:
            self.relative_popularity = relative_popularity
        if license_data is not None:
            self.license_data = license_data
        if integrity_rating is not None:
            self.integrity_rating = integrity_rating
        if hygiene_rating is not None:
            self.hygiene_rating = hygiene_rating
        if security_data is not None:
            self.security_data = security_data
        if policy_data is not None:
            self.policy_data = policy_data
        if project_data is not None:
            self.project_data = project_data

    @property
    def component(self):
        """Gets the component of this ApiComponentDetailsDTOV2.  # noqa: E501


        :return: The component of this ApiComponentDetailsDTOV2.  # noqa: E501
        :rtype: ApiComponentDTOV2
        """
        return self._component

    @component.setter
    def component(self, component):
        """Sets the component of this ApiComponentDetailsDTOV2.


        :param component: The component of this ApiComponentDetailsDTOV2.  # noqa: E501
        :type: ApiComponentDTOV2
        """

        self._component = component

    @property
    def match_state(self):
        """Gets the match_state of this ApiComponentDetailsDTOV2.  # noqa: E501


        :return: The match_state of this ApiComponentDetailsDTOV2.  # noqa: E501
        :rtype: str
        """
        return self._match_state

    @match_state.setter
    def match_state(self, match_state):
        """Sets the match_state of this ApiComponentDetailsDTOV2.


        :param match_state: The match_state of this ApiComponentDetailsDTOV2.  # noqa: E501
        :type: str
        """

        self._match_state = match_state

    @property
    def catalog_date(self):
        """Gets the catalog_date of this ApiComponentDetailsDTOV2.  # noqa: E501


        :return: The catalog_date of this ApiComponentDetailsDTOV2.  # noqa: E501
        :rtype: datetime
        """
        return self._catalog_date

    @catalog_date.setter
    def catalog_date(self, catalog_date):
        """Sets the catalog_date of this ApiComponentDetailsDTOV2.


        :param catalog_date: The catalog_date of this ApiComponentDetailsDTOV2.  # noqa: E501
        :type: datetime
        """

        self._catalog_date = catalog_date

    @property
    def relative_popularity(self):
        """Gets the relative_popularity of this ApiComponentDetailsDTOV2.  # noqa: E501


        :return: The relative_popularity of this ApiComponentDetailsDTOV2.  # noqa: E501
        :rtype: int
        """
        return self._relative_popularity

    @relative_popularity.setter
    def relative_popularity(self, relative_popularity):
        """Sets the relative_popularity of this ApiComponentDetailsDTOV2.


        :param relative_popularity: The relative_popularity of this ApiComponentDetailsDTOV2.  # noqa: E501
        :type: int
        """

        self._relative_popularity = relative_popularity

    @property
    def license_data(self):
        """Gets the license_data of this ApiComponentDetailsDTOV2.  # noqa: E501


        :return: The license_data of this ApiComponentDetailsDTOV2.  # noqa: E501
        :rtype: ApiLicenseDataDTO
        """
        return self._license_data

    @license_data.setter
    def license_data(self, license_data):
        """Sets the license_data of this ApiComponentDetailsDTOV2.


        :param license_data: The license_data of this ApiComponentDetailsDTOV2.  # noqa: E501
        :type: ApiLicenseDataDTO
        """

        self._license_data = license_data

    @property
    def integrity_rating(self):
        """Gets the integrity_rating of this ApiComponentDetailsDTOV2.  # noqa: E501


        :return: The integrity_rating of this ApiComponentDetailsDTOV2.  # noqa: E501
        :rtype: str
        """
        return self._integrity_rating

    @integrity_rating.setter
    def integrity_rating(self, integrity_rating):
        """Sets the integrity_rating of this ApiComponentDetailsDTOV2.


        :param integrity_rating: The integrity_rating of this ApiComponentDetailsDTOV2.  # noqa: E501
        :type: str
        """

        self._integrity_rating = integrity_rating

    @property
    def hygiene_rating(self):
        """Gets the hygiene_rating of this ApiComponentDetailsDTOV2.  # noqa: E501


        :return: The hygiene_rating of this ApiComponentDetailsDTOV2.  # noqa: E501
        :rtype: str
        """
        return self._hygiene_rating

    @hygiene_rating.setter
    def hygiene_rating(self, hygiene_rating):
        """Sets the hygiene_rating of this ApiComponentDetailsDTOV2.


        :param hygiene_rating: The hygiene_rating of this ApiComponentDetailsDTOV2.  # noqa: E501
        :type: str
        """

        self._hygiene_rating = hygiene_rating

    @property
    def security_data(self):
        """Gets the security_data of this ApiComponentDetailsDTOV2.  # noqa: E501


        :return: The security_data of this ApiComponentDetailsDTOV2.  # noqa: E501
        :rtype: ApiSecurityDataDTO
        """
        return self._security_data

    @security_data.setter
    def security_data(self, security_data):
        """Sets the security_data of this ApiComponentDetailsDTOV2.


        :param security_data: The security_data of this ApiComponentDetailsDTOV2.  # noqa: E501
        :type: ApiSecurityDataDTO
        """

        self._security_data = security_data

    @property
    def policy_data(self):
        """Gets the policy_data of this ApiComponentDetailsDTOV2.  # noqa: E501


        :return: The policy_data of this ApiComponentDetailsDTOV2.  # noqa: E501
        :rtype: ApiComponentPolicyViolationListDTOV2
        """
        return self._policy_data

    @policy_data.setter
    def policy_data(self, policy_data):
        """Sets the policy_data of this ApiComponentDetailsDTOV2.


        :param policy_data: The policy_data of this ApiComponentDetailsDTOV2.  # noqa: E501
        :type: ApiComponentPolicyViolationListDTOV2
        """

        self._policy_data = policy_data

    @property
    def project_data(self):
        """Gets the project_data of this ApiComponentDetailsDTOV2.  # noqa: E501


        :return: The project_data of this ApiComponentDetailsDTOV2.  # noqa: E501
        :rtype: ApiComponentProjectDataDTO
        """
        return self._project_data

    @project_data.setter
    def project_data(self, project_data):
        """Sets the project_data of this ApiComponentDetailsDTOV2.


        :param project_data: The project_data of this ApiComponentDetailsDTOV2.  # noqa: E501
        :type: ApiComponentProjectDataDTO
        """

        self._project_data = project_data

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
        if issubclass(ApiComponentDetailsDTOV2, dict):
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
        if not isinstance(other, ApiComponentDetailsDTOV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
