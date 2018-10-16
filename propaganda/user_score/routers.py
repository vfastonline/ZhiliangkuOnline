# encoding: utf-8

from utils.tools import router
from .today_has_user_score_record import TodayHasUserScoreRecordViewSet

router.register(r'today_has_user_score_record', TodayHasUserScoreRecordViewSet, base_name="today_has_user_score_record")
