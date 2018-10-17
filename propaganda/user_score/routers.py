# encoding: utf-8

from utils.tools import router
from .date_range_user_score import *
from .today_has_user_score_record import TodayHasUserScoreRecordViewSet

router.register(r'today_has_user_score_record', TodayHasUserScoreRecordViewSet, base_name="today_has_user_score_record")
router.register(r'date_range_user_score', DateRangeUserScoreViewSet, base_name="date_range_user_score")
