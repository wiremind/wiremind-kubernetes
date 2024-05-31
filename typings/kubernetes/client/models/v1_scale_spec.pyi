"""
This type stub file was generated by pyright.
"""

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.24
    Generated by: https://openapi-generator.tech
"""
class V1ScaleSpec:
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    openapi_types = ...
    attribute_map = ...
    def __init__(self, replicas=..., local_vars_configuration=...) -> None:
        """V1ScaleSpec - a model defined in OpenAPI"""
        ...
    
    @property
    def replicas(self): # -> None:
        """Gets the replicas of this V1ScaleSpec.  # noqa: E501

        desired number of instances for the scaled object.  # noqa: E501

        :return: The replicas of this V1ScaleSpec.  # noqa: E501
        :rtype: int
        """
        ...
    
    @replicas.setter
    def replicas(self, replicas): # -> None:
        """Sets the replicas of this V1ScaleSpec.

        desired number of instances for the scaled object.  # noqa: E501

        :param replicas: The replicas of this V1ScaleSpec.  # noqa: E501
        :type: int
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
    


