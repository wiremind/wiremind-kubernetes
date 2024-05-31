"""
This type stub file was generated by pyright.
"""

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.24
    Generated by: https://openapi-generator.tech
"""
class V1alpha1ServerStorageVersion:
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    openapi_types = ...
    attribute_map = ...
    def __init__(self, api_server_id=..., decodable_versions=..., encoding_version=..., local_vars_configuration=...) -> None:
        """V1alpha1ServerStorageVersion - a model defined in OpenAPI"""
        ...
    
    @property
    def api_server_id(self): # -> None:
        """Gets the api_server_id of this V1alpha1ServerStorageVersion.  # noqa: E501

        The ID of the reporting API server.  # noqa: E501

        :return: The api_server_id of this V1alpha1ServerStorageVersion.  # noqa: E501
        :rtype: str
        """
        ...
    
    @api_server_id.setter
    def api_server_id(self, api_server_id): # -> None:
        """Sets the api_server_id of this V1alpha1ServerStorageVersion.

        The ID of the reporting API server.  # noqa: E501

        :param api_server_id: The api_server_id of this V1alpha1ServerStorageVersion.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def decodable_versions(self): # -> None:
        """Gets the decodable_versions of this V1alpha1ServerStorageVersion.  # noqa: E501

        The API server can decode objects encoded in these versions. The encodingVersion must be included in the decodableVersions.  # noqa: E501

        :return: The decodable_versions of this V1alpha1ServerStorageVersion.  # noqa: E501
        :rtype: list[str]
        """
        ...
    
    @decodable_versions.setter
    def decodable_versions(self, decodable_versions): # -> None:
        """Sets the decodable_versions of this V1alpha1ServerStorageVersion.

        The API server can decode objects encoded in these versions. The encodingVersion must be included in the decodableVersions.  # noqa: E501

        :param decodable_versions: The decodable_versions of this V1alpha1ServerStorageVersion.  # noqa: E501
        :type: list[str]
        """
        ...
    
    @property
    def encoding_version(self): # -> None:
        """Gets the encoding_version of this V1alpha1ServerStorageVersion.  # noqa: E501

        The API server encodes the object to this version when persisting it in the backend (e.g., etcd).  # noqa: E501

        :return: The encoding_version of this V1alpha1ServerStorageVersion.  # noqa: E501
        :rtype: str
        """
        ...
    
    @encoding_version.setter
    def encoding_version(self, encoding_version): # -> None:
        """Sets the encoding_version of this V1alpha1ServerStorageVersion.

        The API server encodes the object to this version when persisting it in the backend (e.g., etcd).  # noqa: E501

        :param encoding_version: The encoding_version of this V1alpha1ServerStorageVersion.  # noqa: E501
        :type: str
        """
        ...
    
    def to_dict(self): # -> dict[Any, Any]:
        """Returns the model properties as a dict"""
        ...
    
    def to_str(self): # -> str:
        """Returns the string representation of the model"""
        ...
    
    def __repr__(self): # -> str:
        """For `print` and `pprint`"""
        ...
    
    def __eq__(self, other) -> bool:
        """Returns true if both objects are equal"""
        ...
    
    def __ne__(self, other) -> bool:
        """Returns true if both objects are not equal"""
        ...
    


