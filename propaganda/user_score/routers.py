# encoding: utf-8

from utils.tools import router
from .add_user_score import AddUserScoreViewSet
from .get_user_score_record import GetUserScoreRecordViewSet
from .user_score_feedback import *

router.register(r'get_user_score_record', GetUserScoreRecordViewSet, base_name="get_user_score_record")
router.register(r'add_user_score', AddUserScoreViewSet, base_name="add_user_score")

# 汇总
# router.register(r'date_range_user_score_avg', DateRangeUserScoreAvgViewSet, base_name="date_range_user_score_avg")
router.register(r'user_score_feedback', UserScoreFeedbackViewSet, base_name="user_score_feedback")
