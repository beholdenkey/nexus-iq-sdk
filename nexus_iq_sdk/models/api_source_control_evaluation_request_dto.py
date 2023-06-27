"""
    Sonatype Nexus IQ Server

    This documents the available APIs into [Sonatype Nexus IQ Server](https://www.sonatype.com/products/open-source-security-dependency-management) (also knwon as Nexus Lifecycle).   # noqa: E501

    OpenAPI spec version: 156

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class ApiSourceControlEvaluationRequestDTO:
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
        'stage_id': 'str',
        'branch_name': 'str',
        'scan_targets': 'list[str]',
    }

    attribute_map = {
        'stage_id': 'stageId',
        'branch_name': 'branchName',
        'scan_targets': 'scanTargets',
    }

    def __init__(
        self, stage_id=None, branch_name=None, scan_targets=None
    ):  # noqa: E501
        """ApiSourceControlEvaluationRequestDTO - a model defined in Swagger"""  # noqa: E501
        self._stage_id = None
        self._branch_name = None
        self._scan_targets = None
        self.discriminator = None
        if stage_id is not None:
            self.stage_id = stage_id
        if branch_name is not None:
            self.branch_name = branch_name
        if scan_targets is not None:
            self.scan_targets = scan_targets

    @property
    def stage_id(self):
        """Gets the stage_id of this ApiSourceControlEvaluationRequestDTO.  # noqa: E501


        :return: The stage_id of this ApiSourceControlEvaluationRequestDTO.  # noqa: E501
        :rtype: str
        """
        return self._stage_id

    @stage_id.setter
    def stage_id(self, stage_id):
        """Sets the stage_id of this ApiSourceControlEvaluationRequestDTO.


        :param stage_id: The stage_id of this ApiSourceControlEvaluationRequestDTO.  # noqa: E501
        :type: str
        """

        self._stage_id = stage_id

    @property
    def branch_name(self):
        """Gets the branch_name of this ApiSourceControlEvaluationRequestDTO.  # noqa: E501


        :return: The branch_name of this ApiSourceControlEvaluationRequestDTO.  # noqa: E501
        :rtype: str
        """
        return self._branch_name

    @branch_name.setter
    def branch_name(self, branch_name):
        """Sets the branch_name of this ApiSourceControlEvaluationRequestDTO.


        :param branch_name: The branch_name of this ApiSourceControlEvaluationRequestDTO.  # noqa: E501
        :type: str
        """

        self._branch_name = branch_name

    @property
    def scan_targets(self):
        """Gets the scan_targets of this ApiSourceControlEvaluationRequestDTO.  # noqa: E501


        :return: The scan_targets of this ApiSourceControlEvaluationRequestDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._scan_targets

    @scan_targets.setter
    def scan_targets(self, scan_targets):
        """Sets the scan_targets of this ApiSourceControlEvaluationRequestDTO.


        :param scan_targets: The scan_targets of this ApiSourceControlEvaluationRequestDTO.  # noqa: E501
        :type: list[str]
        """

        self._scan_targets = scan_targets

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
        if issubclass(ApiSourceControlEvaluationRequestDTO, dict):
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
        if not isinstance(other, ApiSourceControlEvaluationRequestDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
