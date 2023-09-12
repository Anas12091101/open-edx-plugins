import logging
import os

from django.conf import settings
from django.dispatch import receiver
from ol_openedx_git_auto_export.constants import ENABLE_GIT_AUTO_EXPORT
from ol_openedx_git_auto_export.tasks import async_export_to_git
from xmodule.modulestore.django import SignalHandler

log = logging.getLogger(__name__)


@receiver(SignalHandler.course_published)
def listen_for_course_publish(
    sender, course_key, **kwargs  # noqa: ARG001
):  # pylint: disable=unused-argument
    """
    Receives publishing signal and performs publishing related workflows
    """
    git_repo_export_dir = getattr(
        settings, "GIT_REPO_EXPORT_DIR", "/edx/var/edxapp/export_course_repos"
    )
    if not os.path.exists(git_repo_export_dir):  # noqa: PTH110
        # for development/docker/vagrant if GIT_REPO_EXPORT_DIR folder does not exist then create it  # noqa: E501
        log.error(
            "GIT_REPO_EXPORT_DIR is not available in settings, please create it first"
        )
        os.makedirs(git_repo_export_dir, 0o755)  # noqa: PTH103

    if settings.FEATURES.get("ENABLE_EXPORT_GIT") and settings.FEATURES.get(
        ENABLE_GIT_AUTO_EXPORT
    ):
        # If the Git auto-export is enabled, push the course changes to Git
        log.info(
            "Course published with auto-export enabled. Starting export... (course id: %s)",  # noqa: E501
            course_key,
        )
        async_export_to_git.delay(str(course_key))
