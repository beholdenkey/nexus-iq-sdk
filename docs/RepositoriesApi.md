# swagger_client.RepositoriesApi

All URIs are relative to _/_

| Method                                                                                          | HTTP request                                                                                                      | Description |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------- |
| [**get_quarantined_by_path**](RepositoriesApi.md#get_quarantined_by_path)                       | **POST** /api/v2/repositories/{repositoryManagerInstanceId}/{repositoryPublicId}/components/quarantined/pathnames |
| [**release_quarantine_without_re_eval**](RepositoriesApi.md#release_quarantine_without_re_eval) | **POST** /api/v2/repositories/quarantine/{quarantineId}/release                                                   |

# **get_quarantined_by_path**

> ApiRepositoryPathResponseDTO get_quarantined_by_path(repository_manager_instance_id, repository_public_id, body=body)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoriesApi()
repository_manager_instance_id = 'repository_manager_instance_id_example' # str |
repository_public_id = 'repository_public_id_example' # str |
body = ['body_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_quarantined_by_path(repository_manager_instance_id, repository_public_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->get_quarantined_by_path: %s\n" % e)
```

### Parameters

| Name                               | Type                    | Description | Notes      |
| ---------------------------------- | ----------------------- | ----------- | ---------- |
| **repository_manager_instance_id** | **str**                 |             |
| **repository_public_id**           | **str**                 |             |
| **body**                           | [**list[str]**](str.md) |             | [optional] |

### Return type

[**ApiRepositoryPathResponseDTO**](ApiRepositoryPathResponseDTO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **release_quarantine_without_re_eval**

> ApiComponentReleasedFromQuarantineDTO release_quarantine_without_re_eval(quarantine_id, body=body)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoriesApi()
quarantine_id = 'quarantine_id_example' # str |
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.release_quarantine_without_re_eval(quarantine_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->release_quarantine_without_re_eval: %s\n" % e)
```

### Parameters

| Name              | Type              | Description | Notes      |
| ----------------- | ----------------- | ----------- | ---------- |
| **quarantine_id** | **str**           |             |
| **body**          | [**str**](str.md) |             | [optional] |

### Return type

[**ApiComponentReleasedFromQuarantineDTO**](ApiComponentReleasedFromQuarantineDTO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
