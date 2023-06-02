# ApiPolicyViolationDiffDTO

## Properties

| Name                   | Type                                                                          | Description | Notes      |
| ---------------------- | ----------------------------------------------------------------------------- | ----------- | ---------- |
| **application**        | [**ApiApplicationDTO**](ApiApplicationDTO.md)                                 |             | [optional] |
| **from_commit**        | [**ApiApplicationEvaluationCommitDTO**](ApiApplicationEvaluationCommitDTO.md) |             | [optional] |
| **to_commit**          | [**ApiApplicationEvaluationCommitDTO**](ApiApplicationEvaluationCommitDTO.md) |             | [optional] |
| **diff_time**          | **datetime**                                                                  |             | [optional] |
| **added_violations**   | [**list[ApiPolicyViolationForDiffDTO]**](ApiPolicyViolationForDiffDTO.md)     |             | [optional] |
| **same_violations**    | [**list[ApiPolicyViolationForDiffDTO]**](ApiPolicyViolationForDiffDTO.md)     |             | [optional] |
| **removed_violations** | [**list[ApiPolicyViolationForDiffDTO]**](ApiPolicyViolationForDiffDTO.md)     |             | [optional] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
