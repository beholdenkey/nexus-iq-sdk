# API Endpoints

All URIs are relative to _/_

| Class                                      | Method                                                                                                                                                                       | HTTP request                                                                                                      | Description |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------- |
| _ApplicationCategoriesApi_                 | [**add_tag**](docs/ApplicationCategoriesApi.md#add_tag)                                                                                                                      | **POST** /api/v2/applicationCategories/organization/{organizationId}                                              |
| _ApplicationCategoriesApi_                 | [**delete_tag**](docs/ApplicationCategoriesApi.md#delete_tag)                                                                                                                | **DELETE** /api/v2/applicationCategories/organization/{organizationId}/{tagId}                                    |
| _ApplicationCategoriesApi_                 | [**get_applicable_tags**](docs/ApplicationCategoriesApi.md#get_applicable_tags)                                                                                              | **GET** /api/v2/applicationCategories/organization/{organizationId}/applicable                                    |
| _ApplicationCategoriesApi_                 | [**get_applicable_tags_by_application_public_id**](docs/ApplicationCategoriesApi.md#get_applicable_tags_by_application_public_id)                                            | **GET** /api/v2/applicationCategories/application/{applicationPublicId}/applicable                                |
| _ApplicationCategoriesApi_                 | [**get_application_applicable_tags**](docs/ApplicationCategoriesApi.md#get_application_applicable_tags)                                                                      | **GET** /api/v2/applicationCategories/application/{applicationPublicId}                                           |
| _ApplicationCategoriesApi_                 | [**get_applied_policy_tags**](docs/ApplicationCategoriesApi.md#get_applied_policy_tags)                                                                                      | **GET** /api/v2/applicationCategories/organization/{organizationId}/policy                                        |
| _ApplicationCategoriesApi_                 | [**get_applied_tags**](docs/ApplicationCategoriesApi.md#get_applied_tags)                                                                                                    | **GET** /api/v2/applicationCategories/organization/{organizationId}/applied                                       |
| _ApplicationCategoriesApi_                 | [**get_tags**](docs/ApplicationCategoriesApi.md#get_tags)                                                                                                                    | **GET** /api/v2/applicationCategories/organization/{organizationId}                                               |
| _ApplicationCategoriesApi_                 | [**get_tags_used_by_applications**](docs/ApplicationCategoriesApi.md#get_tags_used_by_applications)                                                                          | **GET** /api/v2/applicationCategories/application                                                                 |
| _ApplicationCategoriesApi_                 | [**update_tag**](docs/ApplicationCategoriesApi.md#update_tag)                                                                                                                | **PUT** /api/v2/applicationCategories/organization/{organizationId}                                               |
| _ApplicationsApi_                          | [**add_application**](docs/ApplicationsApi.md#add_application)                                                                                                               | **POST** /api/v2/applications                                                                                     |
| _ApplicationsApi_                          | [**clone_application**](docs/ApplicationsApi.md#clone_application)                                                                                                           | **POST** /api/v2/applications/{sourceApplicationId}/clone                                                         |
| _ApplicationsApi_                          | [**delete_application**](docs/ApplicationsApi.md#delete_application)                                                                                                         | **DELETE** /api/v2/applications/{applicationId}                                                                   |
| _ApplicationsApi_                          | [**get_application**](docs/ApplicationsApi.md#get_application)                                                                                                               | **GET** /api/v2/applications/{applicationId}                                                                      |
| _ApplicationsApi_                          | [**get_applications**](docs/ApplicationsApi.md#get_applications)                                                                                                             | **GET** /api/v2/applications                                                                                      |
| _ApplicationsApi_                          | [**get_applications_by_organization_id**](docs/ApplicationsApi.md#get_applications_by_organization_id)                                                                       | **GET** /api/v2/applications/organization/{organizationId}                                                        |
| _ApplicationsApi_                          | [**get_data**](docs/ApplicationsApi.md#get_data)                                                                                                                             | **GET** /api/v2/applications/{applicationPublicId}/reports/{scanId}                                               |
| _ApplicationsApi_                          | [**get_dependency_tree**](docs/ApplicationsApi.md#get_dependency_tree)                                                                                                       | **GET** /api/v2/applications/{applicationPublicId}/reports/{scanId}/dependencyTree                                |
| _ApplicationsApi_                          | [**get_policy_violation_diff**](docs/ApplicationsApi.md#get_policy_violation_diff)                                                                                           | **GET** /api/v2/applications/{applicationPublicId}/reports/policyViolations/diff                                  |
| _ApplicationsApi_                          | [**get_policy_violations1**](docs/ApplicationsApi.md#get_policy_violations1)                                                                                                 | **GET** /api/v2/applications/{applicationPublicId}/reports/{scanId}/policy                                        |
| _ApplicationsApi_                          | [**get_raw_data**](docs/ApplicationsApi.md#get_raw_data)                                                                                                                     | **GET** /api/v2/applications/{applicationPublicId}/reports/{scanId}/raw                                           |
| _ApplicationsApi_                          | [**move_application**](docs/ApplicationsApi.md#move_application)                                                                                                             | **POST** /api/v2/applications/{applicationId}/move/organization/{organizationId}                                  |
| _ApplicationsApi_                          | [**update_application**](docs/ApplicationsApi.md#update_application)                                                                                                         | **PUT** /api/v2/applications/{applicationId}                                                                      |
| _ClaimApi_                                 | [**delete**](docs/ClaimApi.md#delete)                                                                                                                                        | **DELETE** /api/v2/claim/components/{hash}                                                                        |
| _ClaimApi_                                 | [**get**](docs/ClaimApi.md#get)                                                                                                                                              | **GET** /api/v2/claim/components/{hash}                                                                           |
| _ClaimApi_                                 | [**get_all**](docs/ClaimApi.md#get_all)                                                                                                                                      | **GET** /api/v2/claim/components                                                                                  |
| _ClaimApi_                                 | [**set**](docs/ClaimApi.md#set)                                                                                                                                              | **POST** /api/v2/claim/components                                                                                 |
| _ComponentsApi_                            | [**delete_component_label**](docs/ComponentsApi.md#delete_component_label)                                                                                                   | **DELETE** /api/v2/components/{componentHash}/labels/{labelName}/{ownerType}s/{internalOwnerId}                   |
| _ComponentsApi_                            | [**get_component_details**](docs/ComponentsApi.md#get_component_details)                                                                                                     | **POST** /api/v2/components/details                                                                               |
| _ComponentsApi_                            | [**get_component_versions**](docs/ComponentsApi.md#get_component_versions)                                                                                                   | **POST** /api/v2/components/versions                                                                              |
| _ComponentsApi_                            | [**get_suggested_remediation_for_component**](docs/ComponentsApi.md#get_suggested_remediation_for_component)                                                                 | **POST** /api/v2/components/remediation/{ownerType}/{ownerId}                                                     |
| _ComponentsApi_                            | [**set_component_label**](docs/ComponentsApi.md#set_component_label)                                                                                                         | **POST** /api/v2/components/{componentHash}/labels/{labelName}/{ownerType}s/{internalOwnerId}                     |
| _CompositeSourceControlApi_                | [**get_composite_source_control_by_owner**](docs/CompositeSourceControlApi.md#get_composite_source_control_by_owner)                                                         | **GET** /api/v2/compositeSourceControl/{ownerType}/{internalOwnerId}                                              |
| _CompositeSourceControlConfigValidatorApi_ | [**validate_source_control_config**](docs/CompositeSourceControlConfigValidatorApi.md#validate_source_control_config)                                                        | **GET** /api/v2/compositeSourceControlConfigValidator/application/{applicationId}                                 |
| _ConfigApi_                                | [**delete_configuration**](docs/ConfigApi.md#delete_configuration)                                                                                                           | **DELETE** /api/v2/config                                                                                         |
| _ConfigApi_                                | [**disable_feature**](docs/ConfigApi.md#disable_feature)                                                                                                                     | **DELETE** /api/v2/config/features/{feature}                                                                      |
| _ConfigApi_                                | [**enabled_feature**](docs/ConfigApi.md#enabled_feature)                                                                                                                     | **POST** /api/v2/config/features/{feature}                                                                        |
| _ConfigApi_                                | [**get_configuration**](docs/ConfigApi.md#get_configuration)                                                                                                                 | **GET** /api/v2/config                                                                                            |
| _ConfigApi_                                | [**set_configuration**](docs/ConfigApi.md#set_configuration)                                                                                                                 | **PUT** /api/v2/config                                                                                            |
| _ConfigArtifactoryConnectionApi_           | [**add_artifactory_connection**](docs/ConfigArtifactoryConnectionApi.md#add_artifactory_connection)                                                                          | **POST** /api/v2/config/artifactoryConnection/{ownerType}/{internalOwnerId}                                       |
| _ConfigArtifactoryConnectionApi_           | [**delete_artifactory_connection**](docs/ConfigArtifactoryConnectionApi.md#delete_artifactory_connection)                                                                    | **DELETE** /api/v2/config/artifactoryConnection/{ownerType}/{internalOwnerId}/{artifactoryConnectionId}           |
| _ConfigArtifactoryConnectionApi_           | [**get_artifactory_connection**](docs/ConfigArtifactoryConnectionApi.md#get_artifactory_connection)                                                                          | **GET** /api/v2/config/artifactoryConnection/{ownerType}/{internalOwnerId}/{artifactoryConnectionId}              |
| _ConfigArtifactoryConnectionApi_           | [**get_owner_artifactory_connection**](docs/ConfigArtifactoryConnectionApi.md#get_owner_artifactory_connection)                                                              | **GET** /api/v2/config/artifactoryConnection/{ownerType}/{internalOwnerId}                                        |
| _ConfigArtifactoryConnectionApi_           | [**test_artifactory_connection**](docs/ConfigArtifactoryConnectionApi.md#test_artifactory_connection)                                                                        | **POST** /api/v2/config/artifactoryConnection/{ownerType}/{internalOwnerId}/test                                  |
| _ConfigArtifactoryConnectionApi_           | [**test_artifactory_connection1**](docs/ConfigArtifactoryConnectionApi.md#test_artifactory_connection1)                                                                      | **POST** /api/v2/config/artifactoryConnection/{ownerType}/{internalOwnerId}/{artifactoryConnectionId}/test        |
| _ConfigArtifactoryConnectionApi_           | [**update_artifactory_connection**](docs/ConfigArtifactoryConnectionApi.md#update_artifactory_connection)                                                                    | **PUT** /api/v2/config/artifactoryConnection/{ownerType}/{internalOwnerId}/{artifactoryConnectionId}              |
| _ConfigArtifactoryConnectionApi_           | [**update_owner_artifactory_connection_status**](docs/ConfigArtifactoryConnectionApi.md#update_owner_artifactory_connection_status)                                          | **PUT** /api/v2/config/artifactoryConnection/{ownerType}/{internalOwnerId}                                        |
| _ConfigCrowdApi_                           | [**delete_crowd_configuration**](docs/ConfigCrowdApi.md#delete_crowd_configuration)                                                                                          | **DELETE** /api/v2/config/crowd                                                                                   |
| _ConfigCrowdApi_                           | [**get_crowd_configuration**](docs/ConfigCrowdApi.md#get_crowd_configuration)                                                                                                | **GET** /api/v2/config/crowd                                                                                      |
| _ConfigCrowdApi_                           | [**insert_or_update_crowd_configuration**](docs/ConfigCrowdApi.md#insert_or_update_crowd_configuration)                                                                      | **PUT** /api/v2/config/crowd                                                                                      |
| _ConfigCrowdApi_                           | [**test_crowd_configuration**](docs/ConfigCrowdApi.md#test_crowd_configuration)                                                                                              | **POST** /api/v2/config/crowd/test                                                                                |
| _ConfigJIRAApi_                            | [**delete_configuration1**](docs/ConfigJIRAApi.md#delete_configuration1)                                                                                                     | **DELETE** /api/v2/config/jira                                                                                    |
| _ConfigJIRAApi_                            | [**get_configuration1**](docs/ConfigJIRAApi.md#get_configuration1)                                                                                                           | **GET** /api/v2/config/jira                                                                                       |
| _ConfigJIRAApi_                            | [**set_configuration1**](docs/ConfigJIRAApi.md#set_configuration1)                                                                                                           | **PUT** /api/v2/config/jira                                                                                       |
| _ConfigMailApi_                            | [**delete_configuration2**](docs/ConfigMailApi.md#delete_configuration2)                                                                                                     | **DELETE** /api/v2/config/mail                                                                                    |
| _ConfigMailApi_                            | [**get_configuration2**](docs/ConfigMailApi.md#get_configuration2)                                                                                                           | **GET** /api/v2/config/mail                                                                                       |
| _ConfigMailApi_                            | [**set_configuration2**](docs/ConfigMailApi.md#set_configuration2)                                                                                                           | **PUT** /api/v2/config/mail                                                                                       |
| _ConfigMailApi_                            | [**test_configuration**](docs/ConfigMailApi.md#test_configuration)                                                                                                           | **POST** /api/v2/config/mail/test/{recipientEmail}                                                                |
| _ConfigProxyServerApi_                     | [**delete_configuration3**](docs/ConfigProxyServerApi.md#delete_configuration3)                                                                                              | **DELETE** /api/v2/config/httpProxyServer                                                                         |
| _ConfigProxyServerApi_                     | [**get_configuration3**](docs/ConfigProxyServerApi.md#get_configuration3)                                                                                                    | **GET** /api/v2/config/httpProxyServer                                                                            |
| _ConfigProxyServerApi_                     | [**set_configuration3**](docs/ConfigProxyServerApi.md#set_configuration3)                                                                                                    | **PUT** /api/v2/config/httpProxyServer                                                                            |
| _ConfigReverseProxyAuthenticationApi_      | [**delete_configuration4**](docs/ConfigReverseProxyAuthenticationApi.md#delete_configuration4)                                                                               | **DELETE** /api/v2/config/reverseProxyAuthentication                                                              |
| _ConfigReverseProxyAuthenticationApi_      | [**get_configuration4**](docs/ConfigReverseProxyAuthenticationApi.md#get_configuration4)                                                                                     | **GET** /api/v2/config/reverseProxyAuthentication                                                                 |
| _ConfigReverseProxyAuthenticationApi_      | [**set_configuration4**](docs/ConfigReverseProxyAuthenticationApi.md#set_configuration4)                                                                                     | **PUT** /api/v2/config/reverseProxyAuthentication                                                                 |
| _ConfigSAMLApi_                            | [**delete_saml_configuration**](docs/ConfigSAMLApi.md#delete_saml_configuration)                                                                                             | **DELETE** /api/v2/config/saml                                                                                    |
| _ConfigSAMLApi_                            | [**get_metadata**](docs/ConfigSAMLApi.md#get_metadata)                                                                                                                       | **GET** /api/v2/config/saml/metadata                                                                              |
| _ConfigSAMLApi_                            | [**get_saml_configuration**](docs/ConfigSAMLApi.md#get_saml_configuration)                                                                                                   | **GET** /api/v2/config/saml                                                                                       |
| _ConfigSourceControlApi_                   | [**delete_configuration5**](docs/ConfigSourceControlApi.md#delete_configuration5)                                                                                            | **DELETE** /api/v2/config/sourceControl                                                                           |
| _ConfigSourceControlApi_                   | [**get_configuration5**](docs/ConfigSourceControlApi.md#get_configuration5)                                                                                                  | **GET** /api/v2/config/sourceControl                                                                              |
| _ConfigSourceControlApi_                   | [**set_configuration5**](docs/ConfigSourceControlApi.md#set_configuration5)                                                                                                  | **PUT** /api/v2/config/sourceControl                                                                              |
| _CycloneDxApi_                             | [**get_by_report_id**](docs/CycloneDxApi.md#get_by_report_id)                                                                                                                | **GET** /api/v2/cycloneDx/{applicationId}/reports/{reportId}                                                      |
| _CycloneDxApi_                             | [**get_by_report_id1**](docs/CycloneDxApi.md#get_by_report_id1)                                                                                                              | **GET** /api/v2/cycloneDx/{cdxVersion}/{applicationId}/reports/{reportId}                                         |
| _CycloneDxApi_                             | [**get_latest**](docs/CycloneDxApi.md#get_latest)                                                                                                                            | **GET** /api/v2/cycloneDx/{applicationId}/stages/{stageId}                                                        |
| _CycloneDxApi_                             | [**get_latest1**](docs/CycloneDxApi.md#get_latest1)                                                                                                                          | **GET** /api/v2/cycloneDx/{cdxVersion}/{applicationId}/stages/{stageId}                                           |
| _DataRetentionPoliciesApi_                 | [**get_data_retention_policies**](docs/DataRetentionPoliciesApi.md#get_data_retention_policies)                                                                              | **GET** /api/v2/dataRetentionPolicies/organizations/{organizationId}                                              |
| _DataRetentionPoliciesApi_                 | [**set_data_retention_policies**](docs/DataRetentionPoliciesApi.md#set_data_retention_policies)                                                                              | **PUT** /api/v2/dataRetentionPolicies/organizations/{organizationId}                                              |
| _EndpointsApi_                             | [**get_open_api**](docs/EndpointsApi.md#get_open_api)                                                                                                                        | **GET** /api/v2/endpoints/{apiType}                                                                               |
| _EvaluationApi_                            | [**deprecated_manifest_evaluation**](docs/EvaluationApi.md#deprecated_manifest_evaluation)                                                                                   | **POST** /api/v2/evaluation/applications/{applicationId}/manifestEvaluation                                       |
| _EvaluationApi_                            | [**evaluate_components**](docs/EvaluationApi.md#evaluate_components)                                                                                                         | **POST** /api/v2/evaluation/applications/{applicationId}                                                          |
| _EvaluationApi_                            | [**evaluate_source_control**](docs/EvaluationApi.md#evaluate_source_control)                                                                                                 | **POST** /api/v2/evaluation/applications/{applicationId}/sourceControlEvaluation                                  |
| _EvaluationApi_                            | [**get_application_evaluation_status**](docs/EvaluationApi.md#get_application_evaluation_status)                                                                             | **GET** /api/v2/evaluation/applications/{applicationId}/status/{statusId}                                         |
| _EvaluationApi_                            | [**get_component_evaluation**](docs/EvaluationApi.md#get_component_evaluation)                                                                                               | **GET** /api/v2/evaluation/applications/{applicationId}/results/{resultId}                                        |
| _EvaluationApi_                            | [**promote_scan**](docs/EvaluationApi.md#promote_scan)                                                                                                                       | **POST** /api/v2/evaluation/applications/{applicationId}/promoteScan                                              |
| _FirewallApi_                              | [**get_firewall_auto_unquarantine_config**](docs/FirewallApi.md#get_firewall_auto_unquarantine_config)                                                                       | **GET** /api/v2/firewall/releaseQuarantine/configuration                                                          |
| _FirewallApi_                              | [**get_firewall_unquarantine_summary**](docs/FirewallApi.md#get_firewall_unquarantine_summary)                                                                               | **GET** /api/v2/firewall/releaseQuarantine/summary                                                                |
| _FirewallApi_                              | [**get_quarantine_list**](docs/FirewallApi.md#get_quarantine_list)                                                                                                           | **GET** /api/v2/firewall/components/quarantined                                                                   |
| _FirewallApi_                              | [**get_quarantine_summary**](docs/FirewallApi.md#get_quarantine_summary)                                                                                                     | **GET** /api/v2/firewall/quarantine/summary                                                                       |
| _FirewallApi_                              | [**get_quarantined_component_view_anonymous_access**](docs/FirewallApi.md#get_quarantined_component_view_anonymous_access)                                                   | **GET** /api/v2/firewall/quarantinedComponentView/configuration/anonymousAccess                                   |
| _FirewallApi_                              | [**get_unquarantine_list**](docs/FirewallApi.md#get_unquarantine_list)                                                                                                       | **GET** /api/v2/firewall/components/autoReleasedFromQuarantine                                                    |
| _FirewallApi_                              | [**set_firewall_auto_unquarantine_config**](docs/FirewallApi.md#set_firewall_auto_unquarantine_config)                                                                       | **PUT** /api/v2/firewall/releaseQuarantine/configuration                                                          |
| _FirewallApi_                              | [**set_quarantined_component_view_anonymous_access**](docs/FirewallApi.md#set_quarantined_component_view_anonymous_access)                                                   | **PUT** /api/v2/firewall/quarantinedComponentView/configuration/anonymousAccess/{enabled}                         |
| _LabelsApi_                                | [**add_label**](docs/LabelsApi.md#add_label)                                                                                                                                 | **POST** /api/v2/labels/{ownerType}/{ownerId}                                                                     |
| _LabelsApi_                                | [**delete_label**](docs/LabelsApi.md#delete_label)                                                                                                                           | **DELETE** /api/v2/labels/{ownerType}/{ownerId}/{labelId}                                                         |
| _LabelsApi_                                | [**get_applicable_contexts**](docs/LabelsApi.md#get_applicable_contexts)                                                                                                     | **GET** /api/v2/labels/{ownerType}/{ownerId}/applicable/context/{labelId}                                         |
| _LabelsApi_                                | [**get_applicable_labels**](docs/LabelsApi.md#get_applicable_labels)                                                                                                         | **GET** /api/v2/labels/{ownerType}/{ownerId}/applicable                                                           |
| _LabelsApi_                                | [**get_labels**](docs/LabelsApi.md#get_labels)                                                                                                                               | **GET** /api/v2/labels/{ownerType}/{ownerId}                                                                      |
| _LabelsApi_                                | [**update_label**](docs/LabelsApi.md#update_label)                                                                                                                           | **PUT** /api/v2/labels/{ownerType}/{ownerId}                                                                      |
| _LicenseLegalMetadataApi_                  | [**delete_attribution_report_template**](docs/LicenseLegalMetadataApi.md#delete_attribution_report_template)                                                                 | **DELETE** /api/v2/licenseLegalMetadata/report-template/{id}                                                      |
| _LicenseLegalMetadataApi_                  | [**get_all_attribution_report_templates**](docs/LicenseLegalMetadataApi.md#get_all_attribution_report_templates)                                                             | **GET** /api/v2/licenseLegalMetadata/report-template                                                              |
| _LicenseLegalMetadataApi_                  | [**get_attribution_report_template_by_id**](docs/LicenseLegalMetadataApi.md#get_attribution_report_template_by_id)                                                           | **GET** /api/v2/licenseLegalMetadata/report-template/{id}                                                         |
| _LicenseLegalMetadataApi_                  | [**get_license_legal_application_html_report**](docs/LicenseLegalMetadataApi.md#get_license_legal_application_html_report)                                                   | **GET** /api/v2/licenseLegalMetadata/application/{applicationId}/stage/{stageId}/report                           |
| _LicenseLegalMetadataApi_                  | [**get_license_legal_application_report**](docs/LicenseLegalMetadataApi.md#get_license_legal_application_report)                                                             | **GET** /api/v2/licenseLegalMetadata/application/{applicationId}                                                  |
| _LicenseLegalMetadataApi_                  | [**get_license_legal_application_report1**](docs/LicenseLegalMetadataApi.md#get_license_legal_application_report1)                                                           | **GET** /api/v2/licenseLegalMetadata/application/{applicationId}/stage/{stageId}                                  |
| _LicenseLegalMetadataApi_                  | [**get_license_legal_component_report**](docs/LicenseLegalMetadataApi.md#get_license_legal_component_report)                                                                 | **GET** /api/v2/licenseLegalMetadata/{ownerType}/{ownerId}/component                                              |
| _LicenseLegalMetadataApi_                  | [**get_license_legal_custom_application_html_report**](docs/LicenseLegalMetadataApi.md#get_license_legal_custom_application_html_report)                                     | **POST** /api/v2/licenseLegalMetadata/application/{applicationId}/stage/{stageId}/report                          |
| _LicenseLegalMetadataApi_                  | [**get_license_legal_custom_application_html_report1**](docs/LicenseLegalMetadataApi.md#get_license_legal_custom_application_html_report1)                                   | **POST** /api/v2/licenseLegalMetadata/application/{applicationId}/stage/{stageId}/report/templateId/{templateId}  |
| _LicenseLegalMetadataApi_                  | [**get_license_legal_custom_multi_application_html_report1**](docs/LicenseLegalMetadataApi.md#get_license_legal_custom_multi_application_html_report1)                       | **POST** /api/v2/licenseLegalMetadata/multiApplication/report/templateId/{templateId}                             |
| _LicenseLegalMetadataApi_                  | [**get_license_legal_multi_application_html_report**](docs/LicenseLegalMetadataApi.md#get_license_legal_multi_application_html_report)                                       | **POST** /api/v2/licenseLegalMetadata/multiApplication/report                                                     |
| _LicenseLegalMetadataApi_                  | [**get_license_legal_multi_application_report_from_active_user_filter**](docs/LicenseLegalMetadataApi.md#get_license_legal_multi_application_report_from_active_user_filter) | **POST** /api/v2/licenseLegalMetadata/multiApplication/activeUserFilter/report/templateId/{templateId}            |
| _LicenseLegalMetadataApi_                  | [**save_attribution_report_template**](docs/LicenseLegalMetadataApi.md#save_attribution_report_template)                                                                     | **POST** /api/v2/licenseLegalMetadata/report-template                                                             |
| _OrganizationsApi_                         | [**add_organization**](docs/OrganizationsApi.md#add_organization)                                                                                                            | **POST** /api/v2/organizations                                                                                    |
| _OrganizationsApi_                         | [**get_organization**](docs/OrganizationsApi.md#get_organization)                                                                                                            | **GET** /api/v2/organizations/{organizationId}                                                                    |
| _OrganizationsApi_                         | [**get_organizations**](docs/OrganizationsApi.md#get_organizations)                                                                                                          | **GET** /api/v2/organizations                                                                                     |
| _PoliciesApi_                              | [**get_policies**](docs/PoliciesApi.md#get_policies)                                                                                                                         | **GET** /api/v2/policies                                                                                          |
| _PolicyViolationsApi_                      | [**get_applicable_waivers**](docs/PolicyViolationsApi.md#get_applicable_waivers)                                                                                             | **GET** /api/v2/policyViolations/{violationId}/applicableWaivers                                                  |
| _PolicyViolationsApi_                      | [**get_cross_stage_policy_violation_by_constituent_id**](docs/PolicyViolationsApi.md#get_cross_stage_policy_violation_by_constituent_id)                                     | **GET** /api/v2/policyViolations/crossStage                                                                       |
| _PolicyViolationsApi_                      | [**get_cross_stage_policy_violation_by_id**](docs/PolicyViolationsApi.md#get_cross_stage_policy_violation_by_id)                                                             | **GET** /api/v2/policyViolations/crossStage/{violationId}                                                         |
| _PolicyViolationsApi_                      | [**get_policy_violations**](docs/PolicyViolationsApi.md#get_policy_violations)                                                                                               | **GET** /api/v2/policyViolations                                                                                  |
| _PolicyViolationsApi_                      | [**get_transitive_policy_violations_by_app_scan_component**](docs/PolicyViolationsApi.md#get_transitive_policy_violations_by_app_scan_component)                             | **GET** /api/v2/policyViolations/transitive/{ownerType}/{ownerId}/{scanId}                                        |
| _PolicyViolationsApi_                      | [**get_transitive_policy_violations_by_owner_stage_component**](docs/PolicyViolationsApi.md#get_transitive_policy_violations_by_owner_stage_component)                       | **GET** /api/v2/policyViolations/transitive/{ownerType}/{ownerId}/stages/{stageId}                                |
| _PolicyWaiverApi_                          | [**add_policy_waiver**](docs/PolicyWaiverApi.md#add_policy_waiver)                                                                                                           | **POST** /api/v2/policyWaiver/{policyViolationId}/{ownerType}                                                     |
| _PolicyWaiversApi_                         | [**add_policy_waiver_by_policy_violation_id**](docs/PolicyWaiversApi.md#add_policy_waiver_by_policy_violation_id)                                                            | **POST** /api/v2/policyWaivers/{ownerType}/{ownerId}/{policyViolationId}                                          |
| _PolicyWaiversApi_                         | [**add_waiver_to_transitive_policy_violations_by_app_scan_component**](docs/PolicyWaiversApi.md#add_waiver_to_transitive_policy_violations_by_app_scan_component)            | **POST** /api/v2/policyWaivers/transitive/{ownerType}/{ownerId}/{scanId}                                          |
| _PolicyWaiversApi_                         | [**add_waiver_to_transitive_policy_violations_by_owner_stage_component**](docs/PolicyWaiversApi.md#add_waiver_to_transitive_policy_violations_by_owner_stage_component)      | **POST** /api/v2/policyWaivers/transitive/{ownerType}/{ownerId}/stages/{stageId}                                  |
| _PolicyWaiversApi_                         | [**delete_policy_waiver**](docs/PolicyWaiversApi.md#delete_policy_waiver)                                                                                                    | **DELETE** /api/v2/policyWaivers/{ownerType}/{ownerId}/{policyWaiverId}                                           |
| _PolicyWaiversApi_                         | [**get_policy_waiver**](docs/PolicyWaiversApi.md#get_policy_waiver)                                                                                                          | **GET** /api/v2/policyWaivers/{ownerType}/{ownerId}/{policyWaiverId}                                              |
| _PolicyWaiversApi_                         | [**get_policy_waivers**](docs/PolicyWaiversApi.md#get_policy_waivers)                                                                                                        | **GET** /api/v2/policyWaivers/{ownerType}/{ownerId}                                                               |
| _PolicyWaiversApi_                         | [**get_transitive_policy_waivers_by_app_scan_component**](docs/PolicyWaiversApi.md#get_transitive_policy_waivers_by_app_scan_component)                                      | **GET** /api/v2/policyWaivers/transitive/{ownerType}/{ownerId}/{scanId}                                           |
| _ReportsApi_                               | [**get_all1**](docs/ReportsApi.md#get_all1)                                                                                                                                  | **GET** /api/v2/reports/applications                                                                              |
| _ReportsApi_                               | [**get_by_application_id**](docs/ReportsApi.md#get_by_application_id)                                                                                                        | **GET** /api/v2/reports/applications/{applicationId}                                                              |
| _ReportsApi_                               | [**get_components_in_quarantine**](docs/ReportsApi.md#get_components_in_quarantine)                                                                                          | **GET** /api/v2/reports/components/quarantined                                                                    |
| _ReportsApi_                               | [**get_components_with_waivers**](docs/ReportsApi.md#get_components_with_waivers)                                                                                            | **GET** /api/v2/reports/components/waivers                                                                        |
| _ReportsApi_                               | [**get_metrics**](docs/ReportsApi.md#get_metrics)                                                                                                                            | **POST** /api/v2/reports/metrics                                                                                  |
| _ReportsApi_                               | [**get_report_history_for_application**](docs/ReportsApi.md#get_report_history_for_application)                                                                              | **GET** /api/v2/reports/applications/{applicationId}/history                                                      |
| _ReportsApi_                               | [**get_stale_waivers**](docs/ReportsApi.md#get_stale_waivers)                                                                                                                | **GET** /api/v2/reports/waivers/stale                                                                             |
| _RepositoriesApi_                          | [**get_quarantined_by_path**](docs/RepositoriesApi.md#get_quarantined_by_path)                                                                                               | **POST** /api/v2/repositories/{repositoryManagerInstanceId}/{repositoryPublicId}/components/quarantined/pathnames |
| _RepositoriesApi_                          | [**release_quarantine_without_re_eval**](docs/RepositoriesApi.md#release_quarantine_without_re_eval)                                                                         | **POST** /api/v2/repositories/quarantine/{quarantineId}/release                                                   |
| _RoleMembershipsApi_                       | [**get_role_memberships_application_or_organization**](docs/RoleMembershipsApi.md#get_role_memberships_application_or_organization)                                          | **GET** /api/v2/roleMemberships/{ownerType}/{internalOwnerId}                                                     |
| _RoleMembershipsApi_                       | [**get_role_memberships_global_or_repository_container**](docs/RoleMembershipsApi.md#get_role_memberships_global_or_repository_container)                                    | **GET** /api/v2/roleMemberships/{ownerType}                                                                       |
| _RoleMembershipsApi_                       | [**grant_role_membership_application_or_organization**](docs/RoleMembershipsApi.md#grant_role_membership_application_or_organization)                                        | **PUT** /api/v2/roleMemberships/{ownerType}/{internalOwnerId}/role/{roleId}/{memberType}/{memberName}             |
| _RoleMembershipsApi_                       | [**grant_role_membership_global_or_repository_container**](docs/RoleMembershipsApi.md#grant_role_membership_global_or_repository_container)                                  | **PUT** /api/v2/roleMemberships/{ownerType}/role/{roleId}/{memberType}/{memberName}                               |
| _RoleMembershipsApi_                       | [**revoke_role_membership_application_or_organization**](docs/RoleMembershipsApi.md#revoke_role_membership_application_or_organization)                                      | **DELETE** /api/v2/roleMemberships/{ownerType}/{internalOwnerId}/role/{roleId}/{memberType}/{memberName}          |
| _RoleMembershipsApi_                       | [**revoke_role_membership_global_or_repository_container**](docs/RoleMembershipsApi.md#revoke_role_membership_global_or_repository_container)                                | **DELETE** /api/v2/roleMemberships/{ownerType}/role/{roleId}/{memberType}/{memberName}                            |
| _RolesApi_                                 | [**get_roles**](docs/RolesApi.md#get_roles)                                                                                                                                  | **GET** /api/v2/roles                                                                                             |
| _ScanApi_                                  | [**get_scan_status**](docs/ScanApi.md#get_scan_status)                                                                                                                       | **GET** /api/v2/scan/applications/{applicationId}/status/{scanRequestId}                                          |
| _ScanApi_                                  | [**scan_components**](docs/ScanApi.md#scan_components)                                                                                                                       | **POST** /api/v2/scan/applications/{applicationId}/sources/{source}                                               |
| _SearchApi_                                | [**create_search_index_async**](docs/SearchApi.md#create_search_index_async)                                                                                                 | **POST** /api/v2/search/advanced/index                                                                            |
| _SearchApi_                                | [**get_export_results**](docs/SearchApi.md#get_export_results)                                                                                                               | **GET** /api/v2/search/advanced/export/csv                                                                        |
| _SearchApi_                                | [**search_component**](docs/SearchApi.md#search_component)                                                                                                                   | **GET** /api/v2/search/component                                                                                  |
| _SearchApi_                                | [**search_index**](docs/SearchApi.md#search_index)                                                                                                                           | **GET** /api/v2/search/advanced                                                                                   |
| _SecurityOverridesApi_                     | [**get_security_vulnerability_overrides**](docs/SecurityOverridesApi.md#get_security_vulnerability_overrides)                                                                | **GET** /api/v2/securityOverrides                                                                                 |
| _SourceControlApi_                         | [**add_or_update_source_control**](docs/SourceControlApi.md#add_or_update_source_control)                                                                                    | **POST** /api/v2/sourceControl                                                                                    |
| _SourceControlApi_                         | [**add_source_control**](docs/SourceControlApi.md#add_source_control)                                                                                                        | **POST** /api/v2/sourceControl/{ownerType}/{internalOwnerId}                                                      |
| _SourceControlApi_                         | [**delete_source_control**](docs/SourceControlApi.md#delete_source_control)                                                                                                  | **DELETE** /api/v2/sourceControl/{ownerType}/{internalOwnerId}                                                    |
| _SourceControlApi_                         | [**get_source_control1**](docs/SourceControlApi.md#get_source_control1)                                                                                                      | **GET** /api/v2/sourceControl/{ownerType}/{internalOwnerId}                                                       |
| _SourceControlApi_                         | [**update_source_control**](docs/SourceControlApi.md#update_source_control)                                                                                                  | **PUT** /api/v2/sourceControl/{ownerType}/{internalOwnerId}                                                       |
| _SourceControlMetricsApi_                  | [**get_source_control**](docs/SourceControlMetricsApi.md#get_source_control)                                                                                                 | **GET** /api/v2/sourceControlMetrics/{ownerType}/{internalOwnerId}                                                |
| _TelemetryApi_                             | [**post_external_telemetry**](docs/TelemetryApi.md#post_external_telemetry)                                                                                                  | **POST** /api/v2/telemetry                                                                                        |
| _UserTokensApi_                            | [**create_user_token**](docs/UserTokensApi.md#create_user_token)                                                                                                             | **POST** /api/v2/userTokens/currentUser                                                                           |
| _UserTokensApi_                            | [**delete_current_user_token**](docs/UserTokensApi.md#delete_current_user_token)                                                                                             | **DELETE** /api/v2/userTokens/currentUser                                                                         |
| _UserTokensApi_                            | [**delete_user_token_by_user_code**](docs/UserTokensApi.md#delete_user_token_by_user_code)                                                                                   | **DELETE** /api/v2/userTokens/userCode/{userCode}                                                                 |
| _UserTokensApi_                            | [**get_user_token_by_username_and_realm_id**](docs/UserTokensApi.md#get_user_token_by_username_and_realm_id)                                                                 | **GET** /api/v2/userTokens/{username}                                                                             |
| _UserTokensApi_                            | [**get_user_token_exists_for_current_user**](docs/UserTokensApi.md#get_user_token_exists_for_current_user)                                                                   | **GET** /api/v2/userTokens/currentUser/hasToken                                                                   |
| _UserTokensApi_                            | [**get_user_tokens_by_created_between_and_realm_id**](docs/UserTokensApi.md#get_user_tokens_by_created_between_and_realm_id)                                                 | **GET** /api/v2/userTokens                                                                                        |
| _UserTokensApi_                            | [**purge_user_tokens**](docs/UserTokensApi.md#purge_user_tokens)                                                                                                             | **DELETE** /api/v2/userTokens/purge                                                                               |
| _UsersApi_                                 | [**add**](docs/UsersApi.md#add)                                                                                                                                              | **POST** /api/v2/users                                                                                            |
| _UsersApi_                                 | [**delete1**](docs/UsersApi.md#delete1)                                                                                                                                      | **DELETE** /api/v2/users/{username}                                                                               |
| _UsersApi_                                 | [**get1**](docs/UsersApi.md#get1)                                                                                                                                            | **GET** /api/v2/users/{username}                                                                                  |
| _UsersApi_                                 | [**get_all2**](docs/UsersApi.md#get_all2)                                                                                                                                    | **GET** /api/v2/users                                                                                             |
| _UsersApi_                                 | [**update**](docs/UsersApi.md#update)                                                                                                                                        | **PUT** /api/v2/users/{username}                                                                                  |
| _VulnerabilitiesApi_                       | [**get_security_vulnerability_details**](docs/VulnerabilitiesApi.md#get_security_vulnerability_details)                                                                      | **GET** /api/v2/vulnerabilities/{refId}                                                                           |

## Documentation For Models

- [Action](docs/Action.md)
- [ApiApplicationBaseDTO](docs/ApiApplicationBaseDTO.md)
- [ApiApplicationCategoryDTO](docs/ApiApplicationCategoryDTO.md)
- [ApiApplicationDTO](docs/ApiApplicationDTO.md)
- [ApiApplicationEvaluationCommitDTO](docs/ApiApplicationEvaluationCommitDTO.md)
- [ApiApplicationEvaluationResultDTOV2](docs/ApiApplicationEvaluationResultDTOV2.md)
- [ApiApplicationEvaluationStatusDTOV2](docs/ApiApplicationEvaluationStatusDTOV2.md)
- [ApiApplicationListDTO](docs/ApiApplicationListDTO.md)
- [ApiApplicationReportDTOV2](docs/ApiApplicationReportDTOV2.md)
- [ApiApplicationTagDTO](docs/ApiApplicationTagDTO.md)
- [ApiApplicationViolationDTOV2](docs/ApiApplicationViolationDTOV2.md)
- [ApiApplicationViolationListDTOV2](docs/ApiApplicationViolationListDTOV2.md)
- [ApiApplicationWaiverDTO](docs/ApiApplicationWaiverDTO.md)
- [ApiArtifactoryConnectionDTO](docs/ApiArtifactoryConnectionDTO.md)
- [ApiArtifactoryConnectionStatusRequestDTO](docs/ApiArtifactoryConnectionStatusRequestDTO.md)
- [ApiArtifactoryConnectionStatusResponseDTO](docs/ApiArtifactoryConnectionStatusResponseDTO.md)
- [ApiComponentChangeActionDTO](docs/ApiComponentChangeActionDTO.md)
- [ApiComponentDTOV2](docs/ApiComponentDTOV2.md)
- [ApiComponentDetailsDTOV2](docs/ApiComponentDetailsDTOV2.md)
- [ApiComponentDetailsRequestDTOV2](docs/ApiComponentDetailsRequestDTOV2.md)
- [ApiComponentDetailsResultDTOV2](docs/ApiComponentDetailsResultDTOV2.md)
- [ApiComponentEvaluationRequestDTOV2](docs/ApiComponentEvaluationRequestDTOV2.md)
- [ApiComponentEvaluationResultDTOV2](docs/ApiComponentEvaluationResultDTOV2.md)
- [ApiComponentEvaluationTicketDTOV2](docs/ApiComponentEvaluationTicketDTOV2.md)
- [ApiComponentIdentifierDTOV2](docs/ApiComponentIdentifierDTOV2.md)
- [ApiComponentOrPurlIdentifierDTOV2](docs/ApiComponentOrPurlIdentifierDTOV2.md)
- [ApiComponentPolicyViolationDTO](docs/ApiComponentPolicyViolationDTO.md)
- [ApiComponentPolicyViolationListDTOV2](docs/ApiComponentPolicyViolationListDTOV2.md)
- [ApiComponentPolicyWaiversDTO](docs/ApiComponentPolicyWaiversDTO.md)
- [ApiComponentProjectDataDTO](docs/ApiComponentProjectDataDTO.md)
- [ApiComponentProjectMetadataDTO](docs/ApiComponentProjectMetadataDTO.md)
- [ApiComponentProjectScmDTO](docs/ApiComponentProjectScmDTO.md)
- [ApiComponentProjectScmDetailsDTO](docs/ApiComponentProjectScmDetailsDTO.md)
- [ApiComponentProjectScmMetadataDTO](docs/ApiComponentProjectScmMetadataDTO.md)
- [ApiComponentReleasedFromQuarantineDTO](docs/ApiComponentReleasedFromQuarantineDTO.md)
- [ApiComponentRemediationDTO](docs/ApiComponentRemediationDTO.md)
- [ApiComponentRemediationValueDTO](docs/ApiComponentRemediationValueDTO.md)
- [ApiComponentTransitivePolicyViolationsDTO](docs/ApiComponentTransitivePolicyViolationsDTO.md)
- [ApiComponentWaiversDTO](docs/ApiComponentWaiversDTO.md)
- [ApiComponentsInQuarantineDTO](docs/ApiComponentsInQuarantineDTO.md)
- [ApiCompositeSourceControlDTO](docs/ApiCompositeSourceControlDTO.md)
- [ApiCompositeValueDTOBoolean](docs/ApiCompositeValueDTOBoolean.md)
- [ApiCompositeValueDTOString](docs/ApiCompositeValueDTOString.md)
- [ApiConditionFactReasonDTO](docs/ApiConditionFactReasonDTO.md)
- [ApiConstraintFactDTO](docs/ApiConstraintFactDTO.md)
- [ApiConstraintViolationDTO](docs/ApiConstraintViolationDTO.md)
- [ApiConstraintViolationReasonDTO](docs/ApiConstraintViolationReasonDTO.md)
- [ApiCrossStageViolationDTOV2](docs/ApiCrossStageViolationDTOV2.md)
- [ApiCrowdConfigurationDTO](docs/ApiCrowdConfigurationDTO.md)
- [ApiDataRetentionPoliciesDTO](docs/ApiDataRetentionPoliciesDTO.md)
- [ApiDependencyDataDTO](docs/ApiDependencyDataDTO.md)
- [ApiDependencyTreeNodeDTO](docs/ApiDependencyTreeNodeDTO.md)
- [ApiDependencyTreeResponseDTO](docs/ApiDependencyTreeResponseDTO.md)
- [ApiEnhancedPolicyViolationDTOV2](docs/ApiEnhancedPolicyViolationDTOV2.md)
- [ApiEvaluationResultCounterDTO](docs/ApiEvaluationResultCounterDTO.md)
- [ApiFirewallQuarantineSummaryDTO](docs/ApiFirewallQuarantineSummaryDTO.md)
- [ApiFirewallReleaseQuarantineConfigDTO](docs/ApiFirewallReleaseQuarantineConfigDTO.md)
- [ApiFirewallReleaseQuarantineSummaryDTO](docs/ApiFirewallReleaseQuarantineSummaryDTO.md)
- [ApiHashComponentIdentifierDTO](docs/ApiHashComponentIdentifierDTO.md)
- [ApiHashComponentIdentifiersDTO](docs/ApiHashComponentIdentifiersDTO.md)
- [ApiJiraConfigurationDTO](docs/ApiJiraConfigurationDTO.md)
- [ApiLabelDTO](docs/ApiLabelDTO.md)
- [ApiLicenseDTO](docs/ApiLicenseDTO.md)
- [ApiLicenseDataDTO](docs/ApiLicenseDataDTO.md)
- [ApiLicenseDataDTOV2](docs/ApiLicenseDataDTOV2.md)
- [ApiLicenseLegalApplicationReportDTO](docs/ApiLicenseLegalApplicationReportDTO.md)
- [ApiLicenseLegalComponentDTO](docs/ApiLicenseLegalComponentDTO.md)
- [ApiLicenseLegalComponentReportDTO](docs/ApiLicenseLegalComponentReportDTO.md)
- [ApiLicenseLegalCopyrightDTO](docs/ApiLicenseLegalCopyrightDTO.md)
- [ApiLicenseLegalDataDTO](docs/ApiLicenseLegalDataDTO.md)
- [ApiLicenseLegalFileDTO](docs/ApiLicenseLegalFileDTO.md)
- [ApiLicenseLegalMetadataDTO](docs/ApiLicenseLegalMetadataDTO.md)
- [ApiLicenseLegalObligationDTO](docs/ApiLicenseLegalObligationDTO.md)
- [ApiLicenseLegalStageScanDTO](docs/ApiLicenseLegalStageScanDTO.md)
- [ApiLicenseThreatDTOV2](docs/ApiLicenseThreatDTOV2.md)
- [ApiMailConfigurationDTO](docs/ApiMailConfigurationDTO.md)
- [ApiMatchStateSummaryDTOV2](docs/ApiMatchStateSummaryDTOV2.md)
- [ApiMemberDTO](docs/ApiMemberDTO.md)
- [ApiMetricsReportingQueryDTOV2](docs/ApiMetricsReportingQueryDTOV2.md)
- [ApiMoveApplicationResponseDTOV2](docs/ApiMoveApplicationResponseDTOV2.md)
- [ApiOrganizationDTO](docs/ApiOrganizationDTO.md)
- [ApiOrganizationListDTO](docs/ApiOrganizationListDTO.md)
- [ApiOwnerArtifactoryConnectionDTO](docs/ApiOwnerArtifactoryConnectionDTO.md)
- [ApiOwnerDTO](docs/ApiOwnerDTO.md)
- [ApiPolicyDTO](docs/ApiPolicyDTO.md)
- [ApiPolicyListDTO](docs/ApiPolicyListDTO.md)
- [ApiPolicyViolationDTOV2](docs/ApiPolicyViolationDTOV2.md)
- [ApiPolicyViolationDiffDTO](docs/ApiPolicyViolationDiffDTO.md)
- [ApiPolicyViolationForDiffDTO](docs/ApiPolicyViolationForDiffDTO.md)
- [ApiPolicyViolationStageDTO](docs/ApiPolicyViolationStageDTO.md)
- [ApiPolicyWaiverDTO](docs/ApiPolicyWaiverDTO.md)
- [ApiPolicyWaiversApplicableToViolationDTO](docs/ApiPolicyWaiversApplicableToViolationDTO.md)
- [ApiPromoteScanRequestDTOV2](docs/ApiPromoteScanRequestDTOV2.md)
- [ApiProxyServerConfigurationDTO](docs/ApiProxyServerConfigurationDTO.md)
- [ApiPullRequestResult](docs/ApiPullRequestResult.md)
- [ApiPullRequestResults](docs/ApiPullRequestResults.md)
- [ApiReportComponentDTOV2](docs/ApiReportComponentDTOV2.md)
- [ApiReportComponentPolicyViolationsDTOV2](docs/ApiReportComponentPolicyViolationsDTOV2.md)
- [ApiReportConstraintConditionDTOV2](docs/ApiReportConstraintConditionDTOV2.md)
- [ApiReportConstraintViolationDTOV2](docs/ApiReportConstraintViolationDTOV2.md)
- [ApiReportHistoryDTO](docs/ApiReportHistoryDTO.md)
- [ApiReportPolicyDataDTOV2](docs/ApiReportPolicyDataDTOV2.md)
- [ApiReportPolicyViolationDTOV2](docs/ApiReportPolicyViolationDTOV2.md)
- [ApiReportRawDataDTOV2](docs/ApiReportRawDataDTOV2.md)
- [ApiReportResultsDTO](docs/ApiReportResultsDTO.md)
- [ApiReportRetentionPoliciesDTO](docs/ApiReportRetentionPoliciesDTO.md)
- [ApiReportRetentionPolicyDTO](docs/ApiReportRetentionPolicyDTO.md)
- [ApiRepositoryComponentDTO](docs/ApiRepositoryComponentDTO.md)
- [ApiRepositoryComponentPath](docs/ApiRepositoryComponentPath.md)
- [ApiRepositoryComponentPolicyViolationDTO](docs/ApiRepositoryComponentPolicyViolationDTO.md)
- [ApiRepositoryComponentsInQuarantineDTO](docs/ApiRepositoryComponentsInQuarantineDTO.md)
- [ApiRepositoryDTO](docs/ApiRepositoryDTO.md)
- [ApiRepositoryPathResponseDTO](docs/ApiRepositoryPathResponseDTO.md)
- [ApiRepositoryPathVersions](docs/ApiRepositoryPathVersions.md)
- [ApiRepositoryWaiverDTO](docs/ApiRepositoryWaiverDTO.md)
- [ApiReverseProxyAuthenticationConfigurationDTO](docs/ApiReverseProxyAuthenticationConfigurationDTO.md)
- [ApiRoleDTO](docs/ApiRoleDTO.md)
- [ApiRoleListDTO](docs/ApiRoleListDTO.md)
- [ApiRoleMemberMappingDTO](docs/ApiRoleMemberMappingDTO.md)
- [ApiRoleMemberMappingListDTO](docs/ApiRoleMemberMappingListDTO.md)
- [ApiSamlConfigurationDTO](docs/ApiSamlConfigurationDTO.md)
- [ApiSamlConfigurationResponseDTO](docs/ApiSamlConfigurationResponseDTO.md)
- [ApiSearchCriteriaDTOV2](docs/ApiSearchCriteriaDTOV2.md)
- [ApiSearchResultDTOV2](docs/ApiSearchResultDTOV2.md)
- [ApiSearchResultsDTOV2](docs/ApiSearchResultsDTOV2.md)
- [ApiSecurityDataDTO](docs/ApiSecurityDataDTO.md)
- [ApiSecurityIssueDTO](docs/ApiSecurityIssueDTO.md)
- [ApiSecurityVulnerabilityOverrideDTOV2](docs/ApiSecurityVulnerabilityOverrideDTOV2.md)
- [ApiSecurityVulnerabilityOverrideResponseDTOV2](docs/ApiSecurityVulnerabilityOverrideResponseDTOV2.md)
- [ApiSourceControlConfigurationDTO](docs/ApiSourceControlConfigurationDTO.md)
- [ApiSourceControlDTO](docs/ApiSourceControlDTO.md)
- [ApiSourceControlEvaluationRequestDTO](docs/ApiSourceControlEvaluationRequestDTO.md)
- [ApiStagePolicyViolationComponentDTO](docs/ApiStagePolicyViolationComponentDTO.md)
- [ApiStaleApplicationEvaluationDTO](docs/ApiStaleApplicationEvaluationDTO.md)
- [ApiStaleEvaluationStageDTO](docs/ApiStaleEvaluationStageDTO.md)
- [ApiStaleEvaluationsDTO](docs/ApiStaleEvaluationsDTO.md)
- [ApiStaleRepositoryEvaluationDTO](docs/ApiStaleRepositoryEvaluationDTO.md)
- [ApiStaleWaiverDTO](docs/ApiStaleWaiverDTO.md)
- [ApiStaleWaiversResponseDTO](docs/ApiStaleWaiversResponseDTO.md)
- [ApiStatusDTO](docs/ApiStatusDTO.md)
- [ApiSuccessMetricsRetentionPolicyDTO](docs/ApiSuccessMetricsRetentionPolicyDTO.md)
- [ApiTagDTO](docs/ApiTagDTO.md)
- [ApiThirdPartyScanResultDTO](docs/ApiThirdPartyScanResultDTO.md)
- [ApiUserDTO](docs/ApiUserDTO.md)
- [ApiUserListDTO](docs/ApiUserListDTO.md)
- [ApiUserTokenDTO](docs/ApiUserTokenDTO.md)
- [ApiUserTokenExistsDTO](docs/ApiUserTokenExistsDTO.md)
- [ApiVersionChangeOptionDTO](docs/ApiVersionChangeOptionDTO.md)
- [ApiWaivedPolicyViolationDTO](docs/ApiWaivedPolicyViolationDTO.md)
- [ApiWaiverOptionsDTO](docs/ApiWaiverOptionsDTO.md)
- [ApplicableContext](docs/ApplicableContext.md)
- [ApplicableLabels](docs/ApplicableLabels.md)
- [ApplicableTagsDTO](docs/ApplicableTagsDTO.md)
- [ApplicationTag](docs/ApplicationTag.md)
- [ApplicationTagsByOwnerDTO](docs/ApplicationTagsByOwnerDTO.md)
- [AppliedTagsDTO](docs/AppliedTagsDTO.md)
- [AttributionReportTemplateDTO](docs/AttributionReportTemplateDTO.md)
- [BodyPart](docs/BodyPart.md)
- [BodyPartMediaType](docs/BodyPartMediaType.md)
- [ComponentDisplayName](docs/ComponentDisplayName.md)
- [ComponentDisplayNamePart](docs/ComponentDisplayNamePart.md)
- [ComponentFact](docs/ComponentFact.md)
- [ComponentIdentifier](docs/ComponentIdentifier.md)
- [ComponentObligationAttributionDTO](docs/ComponentObligationAttributionDTO.md)
- [ConditionFact](docs/ConditionFact.md)
- [ConfigurationValidationResult](docs/ConfigurationValidationResult.md)
- [ConstraintFact](docs/ConstraintFact.md)
- [ContentDisposition](docs/ContentDisposition.md)
- [CweId](docs/CweId.md)
- [FormDataBodyPart](docs/FormDataBodyPart.md)
- [FormDataContentDisposition](docs/FormDataContentDisposition.md)
- [FormDataMultiPart](docs/FormDataMultiPart.md)
- [GroupingByDTO](docs/GroupingByDTO.md)
- [InnerSourceData](docs/InnerSourceData.md)
- [JsonNode](docs/JsonNode.md)
- [LabelsByOwner](docs/LabelsByOwner.md)
- [LegalSourceLinkDTO](docs/LegalSourceLinkDTO.md)
- [LicenseObligationDTO](docs/LicenseObligationDTO.md)
- [LicenseThreatGroupDTO](docs/LicenseThreatGroupDTO.md)
- [MessageBodyWorkers](docs/MessageBodyWorkers.md)
- [MultiPart](docs/MultiPart.md)
- [ParameterizedHeader](docs/ParameterizedHeader.md)
- [PolicyAlert](docs/PolicyAlert.md)
- [PolicyEvaluationResult](docs/PolicyEvaluationResult.md)
- [PolicyFact](docs/PolicyFact.md)
- [PolicyOwner](docs/PolicyOwner.md)
- [PolicyTag](docs/PolicyTag.md)
- [ReferenceLink](docs/ReferenceLink.md)
- [RootCause](docs/RootCause.md)
- [SearchResultDTO](docs/SearchResultDTO.md)
- [SearchResultItemDTO](docs/SearchResultItemDTO.md)
- [SecurityVulnerabilityData](docs/SecurityVulnerabilityData.md)
- [SecurityVulnerabilitySeverity](docs/SecurityVulnerabilitySeverity.md)
- [SecurityVulnerabilityWeakness](docs/SecurityVulnerabilityWeakness.md)
- [StageData](docs/StageData.md)
- [TagsByOwnerDTO](docs/TagsByOwnerDTO.md)
- [TriggerReference](docs/TriggerReference.md)
- [ValidationResult](docs/ValidationResult.md)
- [VulnerabilitySource](docs/VulnerabilitySource.md)
