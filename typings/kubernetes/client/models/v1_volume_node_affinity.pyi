"""
This type stub file was generated by pyright.
"""

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.24
    Generated by: https://openapi-generator.tech
"""
class V1VolumeNodeAffinity:
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    openapi_types = ...
    attribute_map = ...
    def __init__(self, required=..., local_vars_configuration=...) -> None:
        """V1VolumeNodeAffinity - a model defined in OpenAPI"""
        ...
    
    @property
    def required(self): # -> None:
        """Gets the required of this V1VolumeNodeAffinity.  # noqa: E501


        :return: The required of this V1VolumeNodeAffinity.  # noqa: E501
        :rtype: V1NodeSelector
        """
        ...
    
    @required.setter
    def required(self, required): # -> None:
        """Sets the required of this V1VolumeNodeAffinity.


        :param required: The required of this V1VolumeNodeAffinity.  # noqa: E501
        :type: V1NodeSelector
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
    


