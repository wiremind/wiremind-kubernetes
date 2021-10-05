# wiremind-kubernetes

## v6.3.3 (2021-10-05)
### Fixes
- stop_pods: ignore failed (like Evicted) Pods, print what still needs to be stopped and simplify internal logic.

## v6.3.2 (2021-10-04)
### Fixes
- setup.py: require kubernetes>=18.

## v6.3.1 (2021-10-04)
### Chore
- Open-sourcing
- Requires python>=3.7

## v6.3.0 (2021-04-28)0
### Feature
- allow to give kube context as parameter.

## v6.2.0 (2021-01-13)
### Feature
- Add the possibility to specify the kubernetes context and the config file path while loading the kubernetes config
using `wiremind_kubernetes.kube_config.load_kubernetes_config`

## v6.1.1 (2020-10-12)
### Fixes
- Remove unused expecteddeploymentscale.wiremind.fr support.

## v6.1.0 (2020-09-18)
### Features
- KubernetesHelper: add priority_class_name to generate_job

## v6.0.1 (2020-09-07)
### fixes
- delete-job: propagate deletion to related pod(s). Avoid having orphaned Pods when Job is deleted.

## v6.0.0 (2020-07-03)
### BREAKING CHANGES
- Remove a lot of helper methods, replace them by wrapped kubernetes clients where we dynamically add needed additional parameters like dry_run or pretty to each function.
### fixes
- run_command: fix mypy error check where it considers that process.stdout can be None even if we explicitely request it.

## v5.1.0 (2020-05-07)
### Fixes
- Ensure backward compatibility with wiremind.fr old EDS resources.

## v5.0.0 (2020-04-23)
### BREAKING CHANGE:
- Add support for priorities. Requires upgrade to Kubernetes CustomResourceDefinition ExpectedDeploymentScale.wiremind.io/v1 and changes how dict of deployments are represented internally.
### Features:
- KubernetesDeploymentManager: create_job: support for labels.
- KubernetesDeploymentManager: Add get_job method.
- stop-pods: wait for pods to be stopped for real.

## v4.0.0 (2020-04-10)
### Breaking changes
- NamespacedKubernetesHelper: rename `deployment_namespace` init argument and instance member to `namespace`
- NamespacedKubernetesHelper: rename `is_statefulset_ready` to `is_deployment_ready` with `statefulset=True` parameter
- E2eTests: move `setUpE2E` to `wiremind_kubernetes.tests.e2e_tests.conftest`
- run_command: replace return_output parameter to return_result that does NO longer raise in cse of error, but returns out, err and returncode.
- KubernetesDeploymentManager: release_name __init__ argument is now mandatory.
- load_kubernetes_config: if os.environ["CLASSIC_K8S_CONFIG"]: always use kubeconfig.
### Features
- KubernetesDeploymentManager: add create_job method.
- KubernetesHelper: add should_load_kubernetes_config parameter to init.
### Fixes
- Remove _get_kube_config_loader_for_yaml_file_with_persistence monkey-patch, no longer needed with kubernetes-python 11.x.x.

## 3.0.1 (2019-12-17)
### Fixes
- e2e tests: delegate to gitlab-ci-common >= 10.1.1 configuration of calico.
- e2e tests: fix get_k8s_username.

## 3.0.0 (2019-12-16)
### BREAKING CHANGES
- KubernetesHelper moved to NamespacedKubernetesHelper, and KubernetesHelper is now a simpler helper, not namespaced.
### Features
- For safety reasons, even unit tests should run on isolated tests-platform executors
- Helper function for object deletion/listing with dry_run support.
- Helper function for setting up e2e cluster.

## 2.0.0 (2019-11-25)
### Breaking change
- Require Python 3
### Feature
- Add wiremind_kubernetes.e2e_tests.helpers.check_not_using_wiremind_cluster helper function
### Fix
- get ExpectedDeploymentScale from either old-style label selector (release=...) or new-style (app.kubernetes.io/instance=...)

## 1.3.4 (2019-11-25)
### Temporary Fix
- Kubernetes python client doesn't persist oidc tokens after refresh

## 1.3.3 (2019-10-29)
### Fix
- Do not silently retry/ignore when getting deployment/statefulset scale.

## 1.3.2 (2019-10-22)
### Fix
- Fix dry-run for read kube methods.

## 1.3.1 (2019-09-17)
### Fix
- Fix minimum version of kubernetes python lib.

## 1.3.0 (2019-09-13)
### Features
- Add dry_run support
- Add statefulset helpers

## 1.2.0 (2019-09-04)
### Features
- run_command: allow to give a callback to call for each new stdout line.

## 1.1.7 (2019-08-21)
### Fixes
- remove hardcoded `load_oid_token`, upgrade to kubernetes 10.x.x.

## 1.1.6 (2019-08-01)
### Changes
- scale-down: sleep 1 second instead of 2.

## 1.1.5 (2019-05-14)
### Changes
- `run_command`: allow to return output.

## 1.1.3 (2019-05-14)
### Changes
- stop-pods: wait only 2 seconds before checking, change logger output levels.

## 1.1.2 (2019-05-10)
### Changes
- Move a few logs to debug.

## 1.1.1 (2019-05-10)
### Changes
- improve `run_command` to log live output.

## 1.0.1 (2019-04-09)
### Changes
- KubernetesDeploymentManager: use `release_name` for real.

## 1.0.0 (2019-04-09)
### Breaking changes
- Improve `_run_command` helper, rename it to `run_command`.
### Changes
- Use logger everywhere.
- Add `kubernetes_exec` helper function.

## 0.4.1 (2019-04-05)
### Changes
- Loading kube configuration: autodetect if run from a pod.
