# encoding: utf-8
from user_score.score_items_desc import ScoreItemsDescViewSet
from utils.tools import router
from .user_score import UserScoreViewSet
from .user_score_feedback import UserScoreFeedbackViewSet
from .user_score_item_avg import UserScoreItemAvgViewSet

router.register(r'score_items_desc', ScoreItemsDescViewSet, base_name="score_items_desc")
router.register(r'user_score', UserScoreViewSet, base_name="user_score")
router.register(r'user_score_item_avg', UserScoreItemAvgViewSet, base_name="user_score_item_avg")
router.register(r'user_score_feedback', UserScoreFeedbackViewSet, base_name="user_score_feedback")
