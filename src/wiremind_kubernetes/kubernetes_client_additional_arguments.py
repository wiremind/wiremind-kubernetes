from typing import Any, Dict

import kubernetes.client


class ClientWithArguments:
    """
    kubernetes.client.CoreApiV1 with arguments added in every function call.

    Currently add dry_run support for write functions and pretty to all.
    """

    client: Any
    read_additional_arguments: Dict[str, Any]
    additional_arguments: Dict[str, Any]

    def __init__(self, client: Any, dry_run: bool = False, pretty: bool = True):
        self.client = client()  # like kubernetes.client.CoreV1Api
        self.read_additional_arguments = {}
        # Only add it when its true because we set pretty client wide,
        # read_cluster_custom_object which accepts it will not have it set, but it's ok for now.
        if pretty:
            self.read_additional_arguments["pretty"] = pretty
        # Every request, either read or write, will have those arguments added
        self.additional_arguments = self.read_additional_arguments.copy()
        if dry_run:
            # Dry run, in kube API, is not true or false, but either dry_run: All or not defined.
            self.additional_arguments["dry_run"] = "All"

    def __getattr__(self, attr: str) -> Any:
        original_attr = getattr(self.client, attr)

        if not callable(original_attr):
            return original_attr

        is_write_function: bool = False
        for name in ["create_", "delete_", "patch_", "replace_"]:
            if attr.startswith(name):
                is_write_function = True
                break

        def fn(*args: Any, **kwargs: Any) -> Any:
            if is_write_function:
                kwargs.update(self.additional_arguments)
            else:  # A read function
                kwargs.update(self.read_additional_arguments)
            return original_attr(*args, **kwargs)

        return fn


class CoreV1ApiWithArguments(ClientWithArguments):
    def __init__(self, *args: Any, dry_run: bool = False, pretty: bool = False, **kwargs: Any) -> None:
        super().__init__(client=kubernetes.client.CoreV1Api, dry_run=dry_run, pretty=pretty)


class AppV1ApiWithArguments(ClientWithArguments):
    def __init__(self, *args: Any, dry_run: bool = False, pretty: bool = False, **kwargs: Any) -> None:
        super().__init__(client=kubernetes.client.AppsV1Api, dry_run=dry_run, pretty=pretty)


class BatchV1ApiWithArguments(ClientWithArguments):
    def __init__(self, *args: Any, dry_run: bool = False, pretty: bool = False, **kwargs: Any) -> None:
        super().__init__(client=kubernetes.client.BatchV1Api, dry_run=dry_run, pretty=pretty)


class AutoscalingV1ApiWithArguments(ClientWithArguments):
    def __init__(self, *args: Any, dry_run: bool = False, pretty: bool = False, **kwargs: Any) -> None:
        super().__init__(client=kubernetes.client.AutoscalingV1Api, dry_run=dry_run, pretty=pretty)


class CustomObjectsApiWithArguments(ClientWithArguments):
    def __init__(self, *args: Any, dry_run: bool = False, pretty: bool = False, **kwargs: Any) -> None:
        super().__init__(client=kubernetes.client.CustomObjectsApi, dry_run=dry_run, pretty=pretty)


class RbacAuthorizationV1ApiWithArguments(ClientWithArguments):
    def __init__(self, *args: Any, dry_run: bool = False, pretty: bool = False, **kwargs: Any) -> None:
        super().__init__(client=kubernetes.client.RbacAuthorizationV1Api, dry_run=dry_run, pretty=pretty)


class NetworkingV1ApiWithArguments(ClientWithArguments):
    def __init__(self, *args: Any, dry_run: bool = False, pretty: bool = False, **kwargs: Any) -> None:
        super().__init__(client=kubernetes.client.NetworkingV1Api, dry_run=dry_run, pretty=pretty)


class StorageV1ApiWithArguments(ClientWithArguments):
    def __init__(self, *args: Any, dry_run: bool = False, pretty: bool = False, **kwargs: Any) -> None:
        super().__init__(client=kubernetes.client.StorageV1Api, dry_run=dry_run, pretty=pretty)


class AdmissionregistrationV1ApiWithArguments(ClientWithArguments):
    def __init__(self, *args: Any, dry_run: bool = False, **kwargs: Any) -> None:
        super().__init__(client=kubernetes.client.AdmissionregistrationV1Api, dry_run=dry_run)
