from celery import Celery

celery = Celery('tellocontrol', autofinalize=False)


def create_app():
    """
    Creates and returns a Celery applications.

    :return: Celery application.
    """
    configure_celery()
    return celery


def configure_celery():
    """
    Configures Celery application based on configuration.
    """
    celery.config_from_object('config')
    celery.autodiscover_tasks(['tellocontrol.control', ])

    celery.finalize()
