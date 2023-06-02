# swagger_client.VulnerabilitiesApi

All URIs are relative to _/_

| Method                                                                                             | HTTP request                            | Description |
| -------------------------------------------------------------------------------------------------- | --------------------------------------- | ----------- |
| [**get_security_vulnerability_details**](VulnerabilitiesApi.md#get_security_vulnerability_details) | **GET** /api/v2/vulnerabilities/{refId} |

# **get_security_vulnerability_details**

> SecurityVulnerabilityData get_security_vulnerability_details(ref_id, component_identifier=component_identifier, identification_source=identification_source, scan_id=scan_id, owner_type=owner_type, owner_id=owner_id)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VulnerabilitiesApi()
ref_id = 'ref_id_example' # str |
component_identifier = swagger_client.ComponentIdentifier() # ComponentIdentifier |  (optional)
identification_source = 'identification_source_example' # str |  (optional)
scan_id = 'scan_id_example' # str |  (optional)
owner_type = 'owner_type_example' # str |  (optional)
owner_id = 'owner_id_example' # str |  (optional)

try:
    api_response = api_instance.get_security_vulnerability_details(ref_id, component_identifier=component_identifier, identification_source=identification_source, scan_id=scan_id, owner_type=owner_type, owner_id=owner_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VulnerabilitiesApi->get_security_vulnerability_details: %s\n" % e)
```

### Parameters

| Name                      | Type                           | Description | Notes      |
| ------------------------- | ------------------------------ | ----------- | ---------- |
| **ref_id**                | **str**                        |             |
| **component_identifier**  | [**ComponentIdentifier**](.md) |             | [optional] |
| **identification_source** | **str**                        |             | [optional] |
| **scan_id**               | **str**                        |             | [optional] |
| **owner_type**            | **str**                        |             | [optional] |
| **owner_id**              | **str**                        |             | [optional] |

### Return type

[**SecurityVulnerabilityData**](SecurityVulnerabilityData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
