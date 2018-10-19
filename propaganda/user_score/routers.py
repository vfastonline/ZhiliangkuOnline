# encoding: utf-8

from utils.tools import router
from .user_score import UserScoreViewSet
from .user_score_feedback import *

# from .user_score_item_avg import UserScoreItemAvgViewSet

router.register(r'user_score', UserScoreViewSet, base_name="user_score")

# 汇总
# router.register(r'user_score_item_avg', UserScoreItemAvgViewSet, base_name="user_score_item_avg")
router.register(r'user_score_feedback', UserScoreFeedbackViewSet, base_name="user_score_feedback")
