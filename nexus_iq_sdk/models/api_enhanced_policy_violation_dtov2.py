"""
    Sonatype Nexus IQ Server

    This documents the available APIs into [Sonatype Nexus IQ Server](https://www.sonatype.com/products/open-source-security-dependency-management) (also knwon as Nexus Lifecycle).   # noqa: E501

    OpenAPI spec version: 156

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class ApiEnhancedPolicyViolationDTOV2:
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
        'policy_id': 'str',
        'policy_name': 'str',
        'policy_violation_id': 'str',
        'threat_level': 'int',
        'constraint_violations': 'list[ApiConstraintViolationDTO]',
        'stage_id': 'str',
        'report_id': 'str',
        'report_url': 'str',
        'open_time': 'datetime',
        'component': 'ApiComponentDTOV2',
    }

    attribute_map = {
        'policy_id': 'policyId',
        'policy_name': 'policyName',
        'policy_violation_id': 'policyViolationId',
        'threat_level': 'threatLevel',
        'constraint_violations': 'constraintViolations',
        'stage_id': 'stageId',
        'report_id': 'reportId',
        'report_url': 'reportUrl',
        'open_time': 'openTime',
        'component': 'component',
    }

    def __init__(
        self,
        policy_id=None,
        policy_name=None,
        policy_violation_id=None,
        threat_level=None,
        constraint_violations=None,
        stage_id=None,
        report_id=None,
        report_url=None,
        open_time=None,
        component=None,
    ):  # noqa: E501
        """ApiEnhancedPolicyViolationDTOV2 - a model defined in Swagger"""  # noqa: E501
        self._policy_id = None
        self._policy_name = None
        self._policy_violation_id = None
        self._threat_level = None
        self._constraint_violations = None
        self._stage_id = None
        self._report_id = None
        self._report_url = None
        self._open_time = None
        self._component = None
        self.discriminator = None
        if policy_id is not None:
            self.policy_id = policy_id
        if policy_name is not None:
            self.policy_name = policy_name
        if policy_violation_id is not None:
            self.policy_violation_id = policy_violation_id
        if threat_level is not None:
            self.threat_level = threat_level
        if constraint_violations is not None:
            self.constraint_violations = constraint_violations
        if stage_id is not None:
            self.stage_id = stage_id
        if report_id is not None:
            self.report_id = report_id
        if report_url is not None:
            self.report_url = report_url
        if open_time is not None:
            self.open_time = open_time
        if component is not None:
            self.component = component

    @property
    def policy_id(self):
        """Gets the policy_id of this ApiEnhancedPolicyViolationDTOV2.  # noqa: E501


        :return: The policy_id of this ApiEnhancedPolicyViolationDTOV2.  # noqa: E501
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this ApiEnhancedPolicyViolationDTOV2.


        :param policy_id: The policy_id of this ApiEnhancedPolicyViolationDTOV2.  # noqa: E501
        :type: str
        """

        self._policy_id = policy_id

    @property
    def policy_name(self):
        """Gets the policy_name of this ApiEnhancedPolicyViolationDTOV2.  # noqa: E501


        :return: The policy_name of this ApiEnhancedPolicyViolationDTOV2.  # noqa: E501
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """Sets the policy_name of this ApiEnhancedPolicyViolationDTOV2.


        :param policy_name: The policy_name of this ApiEnhancedPolicyViolationDTOV2.  # noqa: E501
        :type: str
        """

        self._policy_name = policy_name

    @property
    def policy_violation_id(self):
        """Gets the policy_violation_id of this ApiEnhancedPolicyViolationDTOV2.  # noqa: E501


        :return: The policy_violation_id of this ApiEnhancedPolicyViolationDTOV2.  # noqa: E501
        :rtype: str
        """
        return self._policy_violation_id

    @policy_violation_id.setter
    def policy_violation_id(self, policy_violation_id):
        """Sets the policy_violation_id of this ApiEnhancedPolicyViolationDTOV2.


        :param policy_violation_id: The policy_violation_id of this ApiEnhancedPolicyViolationDTOV2.  # noqa: E501
        :type: str
        """

        self._policy_violation_id = policy_violation_id

    @property
    def threat_level(self):
        """Gets the threat_level of this ApiEnhancedPolicyViolationDTOV2.  # noqa: E501


        :return: The threat_level of this ApiEnhancedPolicyViolationDTOV2.  # noqa: E501
        :rtype: int
        """
        return self._threat_level

    @threat_level.setter
    def threat_level(self, threat_level):
        """Sets the threat_level of this ApiEnhancedPolicyViolationDTOV2.


        :param threat_level: The threat_level of this ApiEnhancedPolicyViolationDTOV2.  # noqa: E501
        :type: int
        """

        self._threat_level = threat_level

    @property
    def constraint_violations(self):
        """Gets the constraint_violations of this ApiEnhancedPolicyViolationDTOV2.  # noqa: E501


        :return: The constraint_violations of this ApiEnhancedPolicyViolationDTOV2.  # noqa: E501
        :rtype: list[ApiConstraintViolationDTO]
        """
        return self._constraint_violations

    @constraint_violations.setter
    def constraint_violations(self, constraint_violations):
        """Sets the constraint_violations of this ApiEnhancedPolicyViolationDTOV2.


        :param constraint_violations: The constraint_violations of this ApiEnhancedPolicyViolationDTOV2.  # noqa: E501
        :type: list[ApiConstraintViolationDTO]
        """

        self._constraint_violations = constraint_violations

    @property
    def stage_id(self):
        """Gets the stage_id of this ApiEnhancedPolicyViolationDTOV2.  # noqa: E501


        :return: The stage_id of this ApiEnhancedPolicyViolationDTOV2.  # noqa: E501
        :rtype: str
        """
        return self._stage_id

    @stage_id.setter
    def stage_id(self, stage_id):
        """Sets the stage_id of this ApiEnhancedPolicyViolationDTOV2.


        :param stage_id: The stage_id of this ApiEnhancedPolicyViolationDTOV2.  # noqa: E501
        :type: str
        """

        self._stage_id = stage_id

    @property
    def report_id(self):
        """Gets the report_id of this ApiEnhancedPolicyViolationDTOV2.  # noqa: E501


        :return: The report_id of this ApiEnhancedPolicyViolationDTOV2.  # noqa: E501
        :rtype: str
        """
        return self._report_id

    @report_id.setter
    def report_id(self, report_id):
        """Sets the report_id of this ApiEnhancedPolicyViolationDTOV2.


        :param report_id: The report_id of this ApiEnhancedPolicyViolationDTOV2.  # noqa: E501
        :type: str
        """

        self._report_id = report_id

    @property
    def report_url(self):
        """Gets the report_url of this ApiEnhancedPolicyViolationDTOV2.  # noqa: E501


        :return: The report_url of this ApiEnhancedPolicyViolationDTOV2.  # noqa: E501
        :rtype: str
        """
        return self._report_url

    @report_url.setter
    def report_url(self, report_url):
        """Sets the report_url of this ApiEnhancedPolicyViolationDTOV2.


        :param report_url: The report_url of this ApiEnhancedPolicyViolationDTOV2.  # noqa: E501
        :type: str
        """

        self._report_url = report_url

    @property
    def open_time(self):
        """Gets the open_time of this ApiEnhancedPolicyViolationDTOV2.  # noqa: E501


        :return: The open_time of this ApiEnhancedPolicyViolationDTOV2.  # noqa: E501
        :rtype: datetime
        """
        return self._open_time

    @open_time.setter
    def open_time(self, open_time):
        """Sets the open_time of this ApiEnhancedPolicyViolationDTOV2.


        :param open_time: The open_time of this ApiEnhancedPolicyViolationDTOV2.  # noqa: E501
        :type: datetime
        """

        self._open_time = open_time

    @property
    def component(self):
        """Gets the component of this ApiEnhancedPolicyViolationDTOV2.  # noqa: E501


        :return: The component of this ApiEnhancedPolicyViolationDTOV2.  # noqa: E501
        :rtype: ApiComponentDTOV2
        """
        return self._component

    @component.setter
    def component(self, component):
        """Sets the component of this ApiEnhancedPolicyViolationDTOV2.


        :param component: The component of this ApiEnhancedPolicyViolationDTOV2.  # noqa: E501
        :type: ApiComponentDTOV2
        """

        self._component = component

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
        if issubclass(ApiEnhancedPolicyViolationDTOV2, dict):
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
        if not isinstance(other, ApiEnhancedPolicyViolationDTOV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
