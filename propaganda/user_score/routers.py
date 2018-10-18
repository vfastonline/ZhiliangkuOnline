# encoding: utf-8

from utils.tools import router
from .add_user_score import AddUserScoreViewSet
from .date_range_user_score import *
from .today_has_user_score_record import TodayHasUserScoreRecordViewSet

# router.register(r'get_score_item', GetScoreItemViewSet, base_name="get_score_item")
router.register(r'today_has_user_score_record', TodayHasUserScoreRecordViewSet, base_name="today_has_user_score_record")
router.register(r'add_user_score', AddUserScoreViewSet, base_name="add_user_score")

# 汇总
# router.register(r'date_range_user_score_avg', DateRangeUserScoreAvgViewSet, base_name="date_range_user_score_avg")
router.register(r'date_range_user_score', DateRangeUserScoreViewSet, base_name="date_range_user_score")
