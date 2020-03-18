import logging
import time

from .conftest import TEST_NAMESPACE

logger = logging.getLogger(__name__)


def test_create_job(concerned_dm, create_namespace):
    """
    Test that default create job works as expected
    """
    job_name = "my-test-job"
    concerned_dm.create_job(
        job_name=job_name, container_image="gcr.io/google_containers/pause-amd64:3.1"
    )
    for _ in range(1, 10):
        created_job = concerned_dm.client_batchv1_api.read_namespaced_job(
            concerned_dm.release_name + "-" + job_name, TEST_NAMESPACE
        )
        if created_job.status.active == 1:
            break
        else:
            logger.info("job not ready yet, waiting...")
            time.sleep(5)
    assert created_job.status.active == 1


def test_create_job_argument(concerned_dm, create_namespace):
    """
    Test that create job with command / args works and finishes as expected
    """
    job_name = "my-test-job"
    concerned_dm.create_job(
        job_name=job_name,
        container_image="alpine:latest",
        command="sh",
        args=["-c", "true"],
    )

    for _ in range(1, 10):
        created_job = concerned_dm.client_batchv1_api.read_namespaced_job(
            concerned_dm.release_name + "-" + job_name, TEST_NAMESPACE
        )
        if created_job.status.succeeded == 1:
            break
        else:
            logger.info("job not finished yet, waiting...")
            time.sleep(5)
    assert created_job.status.succeeded == 1
