# encoding: utf-8

from utils.tools import router
from .user_score_record import UserScoreRecordViewSet

router.register(r'user_score_record', UserScoreRecordViewSet, base_name="user_score_record")
