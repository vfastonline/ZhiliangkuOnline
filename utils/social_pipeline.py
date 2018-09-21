# encoding: utf-8
from django.contrib.auth import get_user_model

from users.models import Team

User = get_user_model()


def save_user_team(strategy, details, backend, user, response, *args, **kwargs):
	invitations_code = strategy.session_get('invitations_code')
	print(invitations_code, '===========')
	if invitations_code:
		team = Team.objects.filter(code=invitations_code)
		if team.exists():
			user.team.add(team[0])
			user.save()
