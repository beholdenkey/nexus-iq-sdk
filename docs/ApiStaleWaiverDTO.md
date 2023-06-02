# ApiStaleWaiverDTO

## Properties

| Name                  | Type                                                      | Description | Notes      |
| --------------------- | --------------------------------------------------------- | ----------- | ---------- |
| **waiver_id**         | **str**                                                   |             | [optional] |
| **policy_id**         | **str**                                                   |             | [optional] |
| **policy_name**       | **str**                                                   |             | [optional] |
| **comment**           | **str**                                                   |             | [optional] |
| **scope_owner_type**  | **str**                                                   |             | [optional] |
| **scope_owner_id**    | **str**                                                   |             | [optional] |
| **scope_owner_name**  | **str**                                                   |             | [optional] |
| **create_time**       | **datetime**                                              |             | [optional] |
| **expiry_time**       | **datetime**                                              |             | [optional] |
| **creator_id**        | **str**                                                   |             | [optional] |
| **creator_name**      | **str**                                                   |             | [optional] |
| **constraint_facts**  | [**list[ApiConstraintFactDTO]**](ApiConstraintFactDTO.md) |             | [optional] |
| **stale_evaluations** | [**ApiStaleEvaluationsDTO**](ApiStaleEvaluationsDTO.md)   |             | [optional] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
