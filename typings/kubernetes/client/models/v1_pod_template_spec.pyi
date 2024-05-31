"""
This type stub file was generated by pyright.
"""

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.24
    Generated by: https://openapi-generator.tech
"""
class V1PodTemplateSpec:
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    openapi_types = ...
    attribute_map = ...
    def __init__(self, metadata=..., spec=..., local_vars_configuration=...) -> None:
        """V1PodTemplateSpec - a model defined in OpenAPI"""
        ...
    
    @property
    def metadata(self): # -> None:
        """Gets the metadata of this V1PodTemplateSpec.  # noqa: E501


        :return: The metadata of this V1PodTemplateSpec.  # noqa: E501
        :rtype: V1ObjectMeta
        """
        ...
    
    @metadata.setter
    def metadata(self, metadata): # -> None:
        """Sets the metadata of this V1PodTemplateSpec.


        :param metadata: The metadata of this V1PodTemplateSpec.  # noqa: E501
        :type: V1ObjectMeta
        """
        ...
    
    @property
    def spec(self): # -> None:
        """Gets the spec of this V1PodTemplateSpec.  # noqa: E501


        :return: The spec of this V1PodTemplateSpec.  # noqa: E501
        :rtype: V1PodSpec
        """
        ...
    
    @spec.setter
    def spec(self, spec): # -> None:
        """Sets the spec of this V1PodTemplateSpec.


        :param spec: The spec of this V1PodTemplateSpec.  # noqa: E501
        :type: V1PodSpec
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
    


