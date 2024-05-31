"""
This type stub file was generated by pyright.
"""

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.24
    Generated by: https://openapi-generator.tech
"""
class V1ServerAddressByClientCIDR:
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    openapi_types = ...
    attribute_map = ...
    def __init__(self, client_cidr=..., server_address=..., local_vars_configuration=...) -> None:
        """V1ServerAddressByClientCIDR - a model defined in OpenAPI"""
        ...
    
    @property
    def client_cidr(self): # -> None:
        """Gets the client_cidr of this V1ServerAddressByClientCIDR.  # noqa: E501

        The CIDR with which clients can match their IP to figure out the server address that they should use.  # noqa: E501

        :return: The client_cidr of this V1ServerAddressByClientCIDR.  # noqa: E501
        :rtype: str
        """
        ...
    
    @client_cidr.setter
    def client_cidr(self, client_cidr): # -> None:
        """Sets the client_cidr of this V1ServerAddressByClientCIDR.

        The CIDR with which clients can match their IP to figure out the server address that they should use.  # noqa: E501

        :param client_cidr: The client_cidr of this V1ServerAddressByClientCIDR.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def server_address(self): # -> None:
        """Gets the server_address of this V1ServerAddressByClientCIDR.  # noqa: E501

        Address of this server, suitable for a client that matches the above CIDR. This can be a hostname, hostname:port, IP or IP:port.  # noqa: E501

        :return: The server_address of this V1ServerAddressByClientCIDR.  # noqa: E501
        :rtype: str
        """
        ...
    
    @server_address.setter
    def server_address(self, server_address): # -> None:
        """Sets the server_address of this V1ServerAddressByClientCIDR.

        Address of this server, suitable for a client that matches the above CIDR. This can be a hostname, hostname:port, IP or IP:port.  # noqa: E501

        :param server_address: The server_address of this V1ServerAddressByClientCIDR.  # noqa: E501
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
    


