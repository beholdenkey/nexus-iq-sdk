# ApiPolicyWaiverDTO

## Properties

| Name                       | Type                                                              | Description | Notes      |
| -------------------------- | ----------------------------------------------------------------- | ----------- | ---------- |
| **policy_waiver_id**       | **str**                                                           |             | [optional] |
| **policy_violation_id**    | **str**                                                           |             | [optional] |
| **comment**                | **str**                                                           |             | [optional] |
| **create_time**            | **datetime**                                                      |             | [optional] |
| **expiry_time**            | **datetime**                                                      |             | [optional] |
| **is_obsolete**            | **bool**                                                          |             | [optional] |
| **scope_owner_type**       | **str**                                                           |             | [optional] |
| **scope_owner_id**         | **str**                                                           |             | [optional] |
| **scope_owner_name**       | **str**                                                           |             | [optional] |
| **hash**                   | **str**                                                           |             | [optional] |
| **policy_id**              | **str**                                                           |             | [optional] |
| **vulnerability_id**       | **str**                                                           |             | [optional] |
| **policy_name**            | **str**                                                           |             | [optional] |
| **constraint_facts**       | [**list[ConstraintFact]**](ConstraintFact.md)                     |             | [optional] |
| **constraint_facts_json**  | **str**                                                           |             | [optional] |
| **component_name**         | **str**                                                           |             | [optional] |
| **creator_id**             | **str**                                                           |             | [optional] |
| **creator_name**           | **str**                                                           |             | [optional] |
| **matcher_strategy**       | **str**                                                           |             | [optional] |
| **associated_package_url** | **str**                                                           |             | [optional] |
| **component_identifier**   | [**ApiComponentIdentifierDTOV2**](ApiComponentIdentifierDTOV2.md) |             | [optional] |
| **threat_level**           | **int**                                                           |             | [optional] |
| **display_name**           | [**ComponentDisplayName**](ComponentDisplayName.md)               |             | [optional] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
