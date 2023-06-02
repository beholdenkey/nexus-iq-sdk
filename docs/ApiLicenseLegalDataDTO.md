# ApiLicenseLegalDataDTO

## Properties

| Name                                             | Type                                                                                | Description | Notes      |
| ------------------------------------------------ | ----------------------------------------------------------------------------------- | ----------- | ---------- |
| **declared_licenses**                            | **list[str]**                                                                       |             | [optional] |
| **observed_licenses**                            | **list[str]**                                                                       |             | [optional] |
| **effective_licenses**                           | **list[str]**                                                                       |             | [optional] |
| **highest_effective_license_threat_group**       | [**ApiLicenseThreatDTOV2**](ApiLicenseThreatDTOV2.md)                               |             | [optional] |
| **copyrights**                                   | [**list[ApiLicenseLegalCopyrightDTO]**](ApiLicenseLegalCopyrightDTO.md)             |             | [optional] |
| **license_files**                                | [**list[ApiLicenseLegalFileDTO]**](ApiLicenseLegalFileDTO.md)                       |             | [optional] |
| **notice_files**                                 | [**list[ApiLicenseLegalFileDTO]**](ApiLicenseLegalFileDTO.md)                       |             | [optional] |
| **obligations**                                  | [**list[ApiLicenseLegalObligationDTO]**](ApiLicenseLegalObligationDTO.md)           |             | [optional] |
| **attributions**                                 | [**list[ComponentObligationAttributionDTO]**](ComponentObligationAttributionDTO.md) |             | [optional] |
| **source_links**                                 | [**list[LegalSourceLinkDTO]**](LegalSourceLinkDTO.md)                               |             | [optional] |
| **effective_license_status**                     | **str**                                                                             |             | [optional] |
| **component_copyright_id**                       | **str**                                                                             |             | [optional] |
| **component_copyright_scope_owner_id**           | **str**                                                                             |             | [optional] |
| **component_copyright_last_updated_by_username** | **str**                                                                             |             | [optional] |
| **component_copyright_last_updated_at**          | **datetime**                                                                        |             | [optional] |
| **component_licenses_id**                        | **str**                                                                             |             | [optional] |
| **component_licenses_scope_owner_id**            | **str**                                                                             |             | [optional] |
| **component_licenses_last_updated_by_username**  | **str**                                                                             |             | [optional] |
| **component_licenses_last_updated_at**           | **datetime**                                                                        |             | [optional] |
| **component_notices_id**                         | **str**                                                                             |             | [optional] |
| **component_notices_scope_owner_id**             | **str**                                                                             |             | [optional] |
| **component_notices_last_updated_by_username**   | **str**                                                                             |             | [optional] |
| **component_notices_last_updated_at**            | **datetime**                                                                        |             | [optional] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
