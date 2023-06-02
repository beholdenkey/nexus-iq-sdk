# ApiWaivedPolicyViolationDTO

## Properties

| Name                      | Type                                                                | Description | Notes      |
| ------------------------- | ------------------------------------------------------------------- | ----------- | ---------- |
| **policy_id**             | **str**                                                             |             | [optional] |
| **policy_name**           | **str**                                                             |             | [optional] |
| **policy_violation_id**   | **str**                                                             |             | [optional] |
| **threat_level**          | **int**                                                             |             | [optional] |
| **constraint_violations** | [**list[ApiConstraintViolationDTO]**](ApiConstraintViolationDTO.md) |             | [optional] |
| **policy_waiver**         | [**ApiPolicyWaiverDTO**](ApiPolicyWaiverDTO.md)                     |             | [optional] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
