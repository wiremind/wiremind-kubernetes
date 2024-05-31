"""
This type stub file was generated by pyright.
"""

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.24
    Generated by: https://openapi-generator.tech
"""
class V1Endpoint:
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    openapi_types = ...
    attribute_map = ...
    def __init__(self, addresses=..., conditions=..., deprecated_topology=..., hints=..., hostname=..., node_name=..., target_ref=..., zone=..., local_vars_configuration=...) -> None:
        """V1Endpoint - a model defined in OpenAPI"""
        ...
    
    @property
    def addresses(self): # -> None:
        """Gets the addresses of this V1Endpoint.  # noqa: E501

        addresses of this endpoint. The contents of this field are interpreted according to the corresponding EndpointSlice addressType field. Consumers must handle different types of addresses in the context of their own capabilities. This must contain at least one address but no more than 100. These are all assumed to be fungible and clients may choose to only use the first element. Refer to: https://issue.k8s.io/106267  # noqa: E501

        :return: The addresses of this V1Endpoint.  # noqa: E501
        :rtype: list[str]
        """
        ...
    
    @addresses.setter
    def addresses(self, addresses): # -> None:
        """Sets the addresses of this V1Endpoint.

        addresses of this endpoint. The contents of this field are interpreted according to the corresponding EndpointSlice addressType field. Consumers must handle different types of addresses in the context of their own capabilities. This must contain at least one address but no more than 100. These are all assumed to be fungible and clients may choose to only use the first element. Refer to: https://issue.k8s.io/106267  # noqa: E501

        :param addresses: The addresses of this V1Endpoint.  # noqa: E501
        :type: list[str]
        """
        ...
    
    @property
    def conditions(self): # -> None:
        """Gets the conditions of this V1Endpoint.  # noqa: E501


        :return: The conditions of this V1Endpoint.  # noqa: E501
        :rtype: V1EndpointConditions
        """
        ...
    
    @conditions.setter
    def conditions(self, conditions): # -> None:
        """Sets the conditions of this V1Endpoint.


        :param conditions: The conditions of this V1Endpoint.  # noqa: E501
        :type: V1EndpointConditions
        """
        ...
    
    @property
    def deprecated_topology(self): # -> None:
        """Gets the deprecated_topology of this V1Endpoint.  # noqa: E501

        deprecatedTopology contains topology information part of the v1beta1 API. This field is deprecated, and will be removed when the v1beta1 API is removed (no sooner than kubernetes v1.24).  While this field can hold values, it is not writable through the v1 API, and any attempts to write to it will be silently ignored. Topology information can be found in the zone and nodeName fields instead.  # noqa: E501

        :return: The deprecated_topology of this V1Endpoint.  # noqa: E501
        :rtype: dict(str, str)
        """
        ...
    
    @deprecated_topology.setter
    def deprecated_topology(self, deprecated_topology): # -> None:
        """Sets the deprecated_topology of this V1Endpoint.

        deprecatedTopology contains topology information part of the v1beta1 API. This field is deprecated, and will be removed when the v1beta1 API is removed (no sooner than kubernetes v1.24).  While this field can hold values, it is not writable through the v1 API, and any attempts to write to it will be silently ignored. Topology information can be found in the zone and nodeName fields instead.  # noqa: E501

        :param deprecated_topology: The deprecated_topology of this V1Endpoint.  # noqa: E501
        :type: dict(str, str)
        """
        ...
    
    @property
    def hints(self): # -> None:
        """Gets the hints of this V1Endpoint.  # noqa: E501


        :return: The hints of this V1Endpoint.  # noqa: E501
        :rtype: V1EndpointHints
        """
        ...
    
    @hints.setter
    def hints(self, hints): # -> None:
        """Sets the hints of this V1Endpoint.


        :param hints: The hints of this V1Endpoint.  # noqa: E501
        :type: V1EndpointHints
        """
        ...
    
    @property
    def hostname(self): # -> None:
        """Gets the hostname of this V1Endpoint.  # noqa: E501

        hostname of this endpoint. This field may be used by consumers of endpoints to distinguish endpoints from each other (e.g. in DNS names). Multiple endpoints which use the same hostname should be considered fungible (e.g. multiple A values in DNS). Must be lowercase and pass DNS Label (RFC 1123) validation.  # noqa: E501

        :return: The hostname of this V1Endpoint.  # noqa: E501
        :rtype: str
        """
        ...
    
    @hostname.setter
    def hostname(self, hostname): # -> None:
        """Sets the hostname of this V1Endpoint.

        hostname of this endpoint. This field may be used by consumers of endpoints to distinguish endpoints from each other (e.g. in DNS names). Multiple endpoints which use the same hostname should be considered fungible (e.g. multiple A values in DNS). Must be lowercase and pass DNS Label (RFC 1123) validation.  # noqa: E501

        :param hostname: The hostname of this V1Endpoint.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def node_name(self): # -> None:
        """Gets the node_name of this V1Endpoint.  # noqa: E501

        nodeName represents the name of the Node hosting this endpoint. This can be used to determine endpoints local to a Node. This field can be enabled with the EndpointSliceNodeName feature gate.  # noqa: E501

        :return: The node_name of this V1Endpoint.  # noqa: E501
        :rtype: str
        """
        ...
    
    @node_name.setter
    def node_name(self, node_name): # -> None:
        """Sets the node_name of this V1Endpoint.

        nodeName represents the name of the Node hosting this endpoint. This can be used to determine endpoints local to a Node. This field can be enabled with the EndpointSliceNodeName feature gate.  # noqa: E501

        :param node_name: The node_name of this V1Endpoint.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def target_ref(self): # -> None:
        """Gets the target_ref of this V1Endpoint.  # noqa: E501


        :return: The target_ref of this V1Endpoint.  # noqa: E501
        :rtype: V1ObjectReference
        """
        ...
    
    @target_ref.setter
    def target_ref(self, target_ref): # -> None:
        """Sets the target_ref of this V1Endpoint.


        :param target_ref: The target_ref of this V1Endpoint.  # noqa: E501
        :type: V1ObjectReference
        """
        ...
    
    @property
    def zone(self): # -> None:
        """Gets the zone of this V1Endpoint.  # noqa: E501

        zone is the name of the Zone this endpoint exists in.  # noqa: E501

        :return: The zone of this V1Endpoint.  # noqa: E501
        :rtype: str
        """
        ...
    
    @zone.setter
    def zone(self, zone): # -> None:
        """Sets the zone of this V1Endpoint.

        zone is the name of the Zone this endpoint exists in.  # noqa: E501

        :param zone: The zone of this V1Endpoint.  # noqa: E501
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
    


