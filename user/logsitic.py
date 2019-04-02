import os
from urllib.parse import urljoin

from django.conf import settings
from lib import qiniuyun
from swiper import config
from commen.keys import ICON_KEY
from user.models import User
from worker import celery_app


@celery_app.task
def upload_qn(uid,icon):
    filename = ICON_KEY % uid
    filepath = os.path.join(settings.BASE_DIR, settings.MEDIA_ROOT, filename)
    with open(filepath, 'wb') as fp:
        for chunk in icon.chunks():
            fp.write(chunk)
    qiniuyun.upload_qiniu(filename,filepath)
    user = User.objects.get(id=uid)
    user.avatar = urljoin(config.QINIU_CLOUD_URL, filename)
    user.save()