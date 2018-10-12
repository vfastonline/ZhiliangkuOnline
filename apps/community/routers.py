#!encoding:utf-8

from community.article import *
from community.article_comment import *
from community.article_drafts import *
from community.faq import *
from community.faq_answer import *
from utils.tools import router

# 登录用户文章
router.register(r'article', ArticleViewSet, base_name="article")
# 指定用户文章
router.register(r'specify_article', SpecifyArticleViewSet, base_name="specify_article")
# 文章草稿箱
router.register(r'article_drafts', ArticleDraftsViewSet, base_name="article_drafts")
router.register(r'article_comment', ArticleCommentViewSet, base_name="article_comment")
router.register(r'specify_article_comment', SpecifyArticleCommentViewSet, base_name="specify_article_comment")

router.register(r'faq', FaqViewSet, base_name="faq")
router.register(r'specify_faq', SpecifyFaqViewSet, base_name="specify_faq")

router.register(r'faq_answer', FaqAnswerViewSet, base_name="faq_answer")
router.register(r'specify_faq_answer', SpecifyFaqAnswerViewSet, base_name="specify_faq_answer")
