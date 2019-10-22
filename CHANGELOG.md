# wiremind-kubernetes

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
