"""
This type stub file was generated by pyright.
"""

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.24
    Generated by: https://openapi-generator.tech
"""
class V2beta1CrossVersionObjectReference:
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    openapi_types = ...
    attribute_map = ...
    def __init__(self, api_version=..., kind=..., name=..., local_vars_configuration=...) -> None:
        """V2beta1CrossVersionObjectReference - a model defined in OpenAPI"""
        ...
    
    @property
    def api_version(self): # -> None:
        """Gets the api_version of this V2beta1CrossVersionObjectReference.  # noqa: E501

        API version of the referent  # noqa: E501

        :return: The api_version of this V2beta1CrossVersionObjectReference.  # noqa: E501
        :rtype: str
        """
        ...
    
    @api_version.setter
    def api_version(self, api_version): # -> None:
        """Sets the api_version of this V2beta1CrossVersionObjectReference.

        API version of the referent  # noqa: E501

        :param api_version: The api_version of this V2beta1CrossVersionObjectReference.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def kind(self): # -> None:
        """Gets the kind of this V2beta1CrossVersionObjectReference.  # noqa: E501

        Kind of the referent; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds\"  # noqa: E501

        :return: The kind of this V2beta1CrossVersionObjectReference.  # noqa: E501
        :rtype: str
        """
        ...
    
    @kind.setter
    def kind(self, kind): # -> None:
        """Sets the kind of this V2beta1CrossVersionObjectReference.

        Kind of the referent; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds\"  # noqa: E501

        :param kind: The kind of this V2beta1CrossVersionObjectReference.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def name(self): # -> None:
        """Gets the name of this V2beta1CrossVersionObjectReference.  # noqa: E501

        Name of the referent; More info: http://kubernetes.io/docs/user-guide/identifiers#names  # noqa: E501

        :return: The name of this V2beta1CrossVersionObjectReference.  # noqa: E501
        :rtype: str
        """
        ...
    
    @name.setter
    def name(self, name): # -> None:
        """Sets the name of this V2beta1CrossVersionObjectReference.

        Name of the referent; More info: http://kubernetes.io/docs/user-guide/identifiers#names  # noqa: E501

        :param name: The name of this V2beta1CrossVersionObjectReference.  # noqa: E501
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
    


