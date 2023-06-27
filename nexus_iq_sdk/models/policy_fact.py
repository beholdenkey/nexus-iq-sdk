"""
    Sonatype Nexus IQ Server

    This documents the available APIs into [Sonatype Nexus IQ Server](https://www.sonatype.com/products/open-source-security-dependency-management) (also knwon as Nexus Lifecycle).   # noqa: E501

    OpenAPI spec version: 156

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class PolicyFact:
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
        'threat_level': 'int',
        'policy_violation_id': 'str',
        'component_facts': 'list[ComponentFact]',
    }

    attribute_map = {
        'policy_id': 'policyId',
        'policy_name': 'policyName',
        'threat_level': 'threatLevel',
        'policy_violation_id': 'policyViolationId',
        'component_facts': 'componentFacts',
    }

    def __init__(
        self,
        policy_id=None,
        policy_name=None,
        threat_level=None,
        policy_violation_id=None,
        component_facts=None,
    ):  # noqa: E501
        """PolicyFact - a model defined in Swagger"""  # noqa: E501
        self._policy_id = None
        self._policy_name = None
        self._threat_level = None
        self._policy_violation_id = None
        self._component_facts = None
        self.discriminator = None
        if policy_id is not None:
            self.policy_id = policy_id
        if policy_name is not None:
            self.policy_name = policy_name
        if threat_level is not None:
            self.threat_level = threat_level
        if policy_violation_id is not None:
            self.policy_violation_id = policy_violation_id
        if component_facts is not None:
            self.component_facts = component_facts

    @property
    def policy_id(self):
        """Gets the policy_id of this PolicyFact.  # noqa: E501


        :return: The policy_id of this PolicyFact.  # noqa: E501
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this PolicyFact.


        :param policy_id: The policy_id of this PolicyFact.  # noqa: E501
        :type: str
        """

        self._policy_id = policy_id

    @property
    def policy_name(self):
        """Gets the policy_name of this PolicyFact.  # noqa: E501


        :return: The policy_name of this PolicyFact.  # noqa: E501
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """Sets the policy_name of this PolicyFact.


        :param policy_name: The policy_name of this PolicyFact.  # noqa: E501
        :type: str
        """

        self._policy_name = policy_name

    @property
    def threat_level(self):
        """Gets the threat_level of this PolicyFact.  # noqa: E501


        :return: The threat_level of this PolicyFact.  # noqa: E501
        :rtype: int
        """
        return self._threat_level

    @threat_level.setter
    def threat_level(self, threat_level):
        """Sets the threat_level of this PolicyFact.


        :param threat_level: The threat_level of this PolicyFact.  # noqa: E501
        :type: int
        """

        self._threat_level = threat_level

    @property
    def policy_violation_id(self):
        """Gets the policy_violation_id of this PolicyFact.  # noqa: E501


        :return: The policy_violation_id of this PolicyFact.  # noqa: E501
        :rtype: str
        """
        return self._policy_violation_id

    @policy_violation_id.setter
    def policy_violation_id(self, policy_violation_id):
        """Sets the policy_violation_id of this PolicyFact.


        :param policy_violation_id: The policy_violation_id of this PolicyFact.  # noqa: E501
        :type: str
        """

        self._policy_violation_id = policy_violation_id

    @property
    def component_facts(self):
        """Gets the component_facts of this PolicyFact.  # noqa: E501


        :return: The component_facts of this PolicyFact.  # noqa: E501
        :rtype: list[ComponentFact]
        """
        return self._component_facts

    @component_facts.setter
    def component_facts(self, component_facts):
        """Sets the component_facts of this PolicyFact.


        :param component_facts: The component_facts of this PolicyFact.  # noqa: E501
        :type: list[ComponentFact]
        """

        self._component_facts = component_facts

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
        if issubclass(PolicyFact, dict):
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
        if not isinstance(other, PolicyFact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
