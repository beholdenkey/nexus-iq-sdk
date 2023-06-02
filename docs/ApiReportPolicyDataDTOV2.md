# ApiReportPolicyDataDTOV2

## Properties

| Name             | Type                                                                                            | Description | Notes      |
| ---------------- | ----------------------------------------------------------------------------------------------- | ----------- | ---------- |
| **report_time**  | **datetime**                                                                                    |             | [optional] |
| **report_title** | **str**                                                                                         |             | [optional] |
| **commit_hash**  | **str**                                                                                         |             | [optional] |
| **initiator**    | **str**                                                                                         |             | [optional] |
| **application**  | [**ApiApplicationBaseDTO**](ApiApplicationBaseDTO.md)                                           |             | [optional] |
| **counts**       | **dict(str, int)**                                                                              |             | [optional] |
| **components**   | [**list[ApiReportComponentPolicyViolationsDTOV2]**](ApiReportComponentPolicyViolationsDTOV2.md) |             | [optional] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
