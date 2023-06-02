# swagger_client.SourceControlMetricsApi

All URIs are relative to _/_

| Method                                                                  | HTTP request                                                       | Description |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------ | ----------- |
| [**get_source_control**](SourceControlMetricsApi.md#get_source_control) | **GET** /api/v2/sourceControlMetrics/{ownerType}/{internalOwnerId} |

# **get_source_control**

> ApiPullRequestResults get_source_control(owner_type, internal_owner_id)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SourceControlMetricsApi()
owner_type = 'owner_type_example' # str |
internal_owner_id = 'internal_owner_id_example' # str |

try:
    api_response = api_instance.get_source_control(owner_type, internal_owner_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceControlMetricsApi->get_source_control: %s\n" % e)
```

### Parameters

| Name                  | Type    | Description | Notes |
| --------------------- | ------- | ----------- | ----- |
| **owner_type**        | **str** |             |
| **internal_owner_id** | **str** |             |

### Return type

[**ApiPullRequestResults**](ApiPullRequestResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
