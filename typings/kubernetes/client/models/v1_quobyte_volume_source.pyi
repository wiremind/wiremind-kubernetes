"""
This type stub file was generated by pyright.
"""

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.24
    Generated by: https://openapi-generator.tech
"""
class V1QuobyteVolumeSource:
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    openapi_types = ...
    attribute_map = ...
    def __init__(self, group=..., read_only=..., registry=..., tenant=..., user=..., volume=..., local_vars_configuration=...) -> None:
        """V1QuobyteVolumeSource - a model defined in OpenAPI"""
        ...
    
    @property
    def group(self): # -> None:
        """Gets the group of this V1QuobyteVolumeSource.  # noqa: E501

        group to map volume access to Default is no group  # noqa: E501

        :return: The group of this V1QuobyteVolumeSource.  # noqa: E501
        :rtype: str
        """
        ...
    
    @group.setter
    def group(self, group): # -> None:
        """Sets the group of this V1QuobyteVolumeSource.

        group to map volume access to Default is no group  # noqa: E501

        :param group: The group of this V1QuobyteVolumeSource.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def read_only(self): # -> None:
        """Gets the read_only of this V1QuobyteVolumeSource.  # noqa: E501

        readOnly here will force the Quobyte volume to be mounted with read-only permissions. Defaults to false.  # noqa: E501

        :return: The read_only of this V1QuobyteVolumeSource.  # noqa: E501
        :rtype: bool
        """
        ...
    
    @read_only.setter
    def read_only(self, read_only): # -> None:
        """Sets the read_only of this V1QuobyteVolumeSource.

        readOnly here will force the Quobyte volume to be mounted with read-only permissions. Defaults to false.  # noqa: E501

        :param read_only: The read_only of this V1QuobyteVolumeSource.  # noqa: E501
        :type: bool
        """
        ...
    
    @property
    def registry(self): # -> None:
        """Gets the registry of this V1QuobyteVolumeSource.  # noqa: E501

        registry represents a single or multiple Quobyte Registry services specified as a string as host:port pair (multiple entries are separated with commas) which acts as the central registry for volumes  # noqa: E501

        :return: The registry of this V1QuobyteVolumeSource.  # noqa: E501
        :rtype: str
        """
        ...
    
    @registry.setter
    def registry(self, registry): # -> None:
        """Sets the registry of this V1QuobyteVolumeSource.

        registry represents a single or multiple Quobyte Registry services specified as a string as host:port pair (multiple entries are separated with commas) which acts as the central registry for volumes  # noqa: E501

        :param registry: The registry of this V1QuobyteVolumeSource.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def tenant(self): # -> None:
        """Gets the tenant of this V1QuobyteVolumeSource.  # noqa: E501

        tenant owning the given Quobyte volume in the Backend Used with dynamically provisioned Quobyte volumes, value is set by the plugin  # noqa: E501

        :return: The tenant of this V1QuobyteVolumeSource.  # noqa: E501
        :rtype: str
        """
        ...
    
    @tenant.setter
    def tenant(self, tenant): # -> None:
        """Sets the tenant of this V1QuobyteVolumeSource.

        tenant owning the given Quobyte volume in the Backend Used with dynamically provisioned Quobyte volumes, value is set by the plugin  # noqa: E501

        :param tenant: The tenant of this V1QuobyteVolumeSource.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def user(self): # -> None:
        """Gets the user of this V1QuobyteVolumeSource.  # noqa: E501

        user to map volume access to Defaults to serivceaccount user  # noqa: E501

        :return: The user of this V1QuobyteVolumeSource.  # noqa: E501
        :rtype: str
        """
        ...
    
    @user.setter
    def user(self, user): # -> None:
        """Sets the user of this V1QuobyteVolumeSource.

        user to map volume access to Defaults to serivceaccount user  # noqa: E501

        :param user: The user of this V1QuobyteVolumeSource.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def volume(self): # -> None:
        """Gets the volume of this V1QuobyteVolumeSource.  # noqa: E501

        volume is a string that references an already created Quobyte volume by name.  # noqa: E501

        :return: The volume of this V1QuobyteVolumeSource.  # noqa: E501
        :rtype: str
        """
        ...
    
    @volume.setter
    def volume(self, volume): # -> None:
        """Sets the volume of this V1QuobyteVolumeSource.

        volume is a string that references an already created Quobyte volume by name.  # noqa: E501

        :param volume: The volume of this V1QuobyteVolumeSource.  # noqa: E501
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
    


