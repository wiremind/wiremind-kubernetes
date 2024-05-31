"""
This type stub file was generated by pyright.
"""

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.24
    Generated by: https://openapi-generator.tech
"""
class V1VolumeAttachmentStatus:
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    openapi_types = ...
    attribute_map = ...
    def __init__(self, attach_error=..., attached=..., attachment_metadata=..., detach_error=..., local_vars_configuration=...) -> None:
        """V1VolumeAttachmentStatus - a model defined in OpenAPI"""
        ...
    
    @property
    def attach_error(self): # -> None:
        """Gets the attach_error of this V1VolumeAttachmentStatus.  # noqa: E501


        :return: The attach_error of this V1VolumeAttachmentStatus.  # noqa: E501
        :rtype: V1VolumeError
        """
        ...
    
    @attach_error.setter
    def attach_error(self, attach_error): # -> None:
        """Sets the attach_error of this V1VolumeAttachmentStatus.


        :param attach_error: The attach_error of this V1VolumeAttachmentStatus.  # noqa: E501
        :type: V1VolumeError
        """
        ...
    
    @property
    def attached(self): # -> None:
        """Gets the attached of this V1VolumeAttachmentStatus.  # noqa: E501

        Indicates the volume is successfully attached. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.  # noqa: E501

        :return: The attached of this V1VolumeAttachmentStatus.  # noqa: E501
        :rtype: bool
        """
        ...
    
    @attached.setter
    def attached(self, attached): # -> None:
        """Sets the attached of this V1VolumeAttachmentStatus.

        Indicates the volume is successfully attached. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.  # noqa: E501

        :param attached: The attached of this V1VolumeAttachmentStatus.  # noqa: E501
        :type: bool
        """
        ...
    
    @property
    def attachment_metadata(self): # -> None:
        """Gets the attachment_metadata of this V1VolumeAttachmentStatus.  # noqa: E501

        Upon successful attach, this field is populated with any information returned by the attach operation that must be passed into subsequent WaitForAttach or Mount calls. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.  # noqa: E501

        :return: The attachment_metadata of this V1VolumeAttachmentStatus.  # noqa: E501
        :rtype: dict(str, str)
        """
        ...
    
    @attachment_metadata.setter
    def attachment_metadata(self, attachment_metadata): # -> None:
        """Sets the attachment_metadata of this V1VolumeAttachmentStatus.

        Upon successful attach, this field is populated with any information returned by the attach operation that must be passed into subsequent WaitForAttach or Mount calls. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.  # noqa: E501

        :param attachment_metadata: The attachment_metadata of this V1VolumeAttachmentStatus.  # noqa: E501
        :type: dict(str, str)
        """
        ...
    
    @property
    def detach_error(self): # -> None:
        """Gets the detach_error of this V1VolumeAttachmentStatus.  # noqa: E501


        :return: The detach_error of this V1VolumeAttachmentStatus.  # noqa: E501
        :rtype: V1VolumeError
        """
        ...
    
    @detach_error.setter
    def detach_error(self, detach_error): # -> None:
        """Sets the detach_error of this V1VolumeAttachmentStatus.


        :param detach_error: The detach_error of this V1VolumeAttachmentStatus.  # noqa: E501
        :type: V1VolumeError
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
    


