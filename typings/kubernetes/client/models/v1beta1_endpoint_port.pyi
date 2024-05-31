"""
This type stub file was generated by pyright.
"""

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.24
    Generated by: https://openapi-generator.tech
"""
class V1beta1EndpointPort:
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    openapi_types = ...
    attribute_map = ...
    def __init__(self, app_protocol=..., name=..., port=..., protocol=..., local_vars_configuration=...) -> None:
        """V1beta1EndpointPort - a model defined in OpenAPI"""
        ...
    
    @property
    def app_protocol(self): # -> None:
        """Gets the app_protocol of this V1beta1EndpointPort.  # noqa: E501

        The application protocol for this port. This field follows standard Kubernetes label syntax. Un-prefixed names are reserved for IANA standard service names (as per RFC-6335 and https://www.iana.org/assignments/service-names). Non-standard protocols should use prefixed names such as mycompany.com/my-custom-protocol.  # noqa: E501

        :return: The app_protocol of this V1beta1EndpointPort.  # noqa: E501
        :rtype: str
        """
        ...
    
    @app_protocol.setter
    def app_protocol(self, app_protocol): # -> None:
        """Sets the app_protocol of this V1beta1EndpointPort.

        The application protocol for this port. This field follows standard Kubernetes label syntax. Un-prefixed names are reserved for IANA standard service names (as per RFC-6335 and https://www.iana.org/assignments/service-names). Non-standard protocols should use prefixed names such as mycompany.com/my-custom-protocol.  # noqa: E501

        :param app_protocol: The app_protocol of this V1beta1EndpointPort.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def name(self): # -> None:
        """Gets the name of this V1beta1EndpointPort.  # noqa: E501

        The name of this port. All ports in an EndpointSlice must have a unique name. If the EndpointSlice is dervied from a Kubernetes service, this corresponds to the Service.ports[].name. Name must either be an empty string or pass DNS_LABEL validation: * must be no more than 63 characters long. * must consist of lower case alphanumeric characters or '-'. * must start and end with an alphanumeric character. Default is empty string.  # noqa: E501

        :return: The name of this V1beta1EndpointPort.  # noqa: E501
        :rtype: str
        """
        ...
    
    @name.setter
    def name(self, name): # -> None:
        """Sets the name of this V1beta1EndpointPort.

        The name of this port. All ports in an EndpointSlice must have a unique name. If the EndpointSlice is dervied from a Kubernetes service, this corresponds to the Service.ports[].name. Name must either be an empty string or pass DNS_LABEL validation: * must be no more than 63 characters long. * must consist of lower case alphanumeric characters or '-'. * must start and end with an alphanumeric character. Default is empty string.  # noqa: E501

        :param name: The name of this V1beta1EndpointPort.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def port(self): # -> None:
        """Gets the port of this V1beta1EndpointPort.  # noqa: E501

        The port number of the endpoint. If this is not specified, ports are not restricted and must be interpreted in the context of the specific consumer.  # noqa: E501

        :return: The port of this V1beta1EndpointPort.  # noqa: E501
        :rtype: int
        """
        ...
    
    @port.setter
    def port(self, port): # -> None:
        """Sets the port of this V1beta1EndpointPort.

        The port number of the endpoint. If this is not specified, ports are not restricted and must be interpreted in the context of the specific consumer.  # noqa: E501

        :param port: The port of this V1beta1EndpointPort.  # noqa: E501
        :type: int
        """
        ...
    
    @property
    def protocol(self): # -> None:
        """Gets the protocol of this V1beta1EndpointPort.  # noqa: E501

        The IP protocol for this port. Must be UDP, TCP, or SCTP. Default is TCP.  # noqa: E501

        :return: The protocol of this V1beta1EndpointPort.  # noqa: E501
        :rtype: str
        """
        ...
    
    @protocol.setter
    def protocol(self, protocol): # -> None:
        """Sets the protocol of this V1beta1EndpointPort.

        The IP protocol for this port. Must be UDP, TCP, or SCTP. Default is TCP.  # noqa: E501

        :param protocol: The protocol of this V1beta1EndpointPort.  # noqa: E501
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
    


