"""
This type stub file was generated by pyright.
"""

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.24
    Generated by: https://openapi-generator.tech
"""
class V1ComponentStatus:
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    openapi_types = ...
    attribute_map = ...
    def __init__(self, api_version=..., conditions=..., kind=..., metadata=..., local_vars_configuration=...) -> None:
        """V1ComponentStatus - a model defined in OpenAPI"""
        ...
    
    @property
    def api_version(self): # -> None:
        """Gets the api_version of this V1ComponentStatus.  # noqa: E501

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :return: The api_version of this V1ComponentStatus.  # noqa: E501
        :rtype: str
        """
        ...
    
    @api_version.setter
    def api_version(self, api_version): # -> None:
        """Sets the api_version of this V1ComponentStatus.

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :param api_version: The api_version of this V1ComponentStatus.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def conditions(self): # -> None:
        """Gets the conditions of this V1ComponentStatus.  # noqa: E501

        List of component conditions observed  # noqa: E501

        :return: The conditions of this V1ComponentStatus.  # noqa: E501
        :rtype: list[V1ComponentCondition]
        """
        ...
    
    @conditions.setter
    def conditions(self, conditions): # -> None:
        """Sets the conditions of this V1ComponentStatus.

        List of component conditions observed  # noqa: E501

        :param conditions: The conditions of this V1ComponentStatus.  # noqa: E501
        :type: list[V1ComponentCondition]
        """
        ...
    
    @property
    def kind(self): # -> None:
        """Gets the kind of this V1ComponentStatus.  # noqa: E501

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :return: The kind of this V1ComponentStatus.  # noqa: E501
        :rtype: str
        """
        ...
    
    @kind.setter
    def kind(self, kind): # -> None:
        """Sets the kind of this V1ComponentStatus.

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :param kind: The kind of this V1ComponentStatus.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def metadata(self): # -> None:
        """Gets the metadata of this V1ComponentStatus.  # noqa: E501


        :return: The metadata of this V1ComponentStatus.  # noqa: E501
        :rtype: V1ObjectMeta
        """
        ...
    
    @metadata.setter
    def metadata(self, metadata): # -> None:
        """Sets the metadata of this V1ComponentStatus.


        :param metadata: The metadata of this V1ComponentStatus.  # noqa: E501
        :type: V1ObjectMeta
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
    


