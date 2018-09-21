# encoding: utf-8
from django.contrib.auth import get_user_model

from apps.users.models import Team

User = get_user_model()


def save_user_team(strategy, details, backend, user, response, *args, **kwargs):
	invitations_code = strategy.session_get('invitations_code')
	print(invitations_code, '===========')
	if invitations_code:
		profile = user.get_profile()
		team = Team.objects.filter(code=invitations_code)
		if team.exists():
			if profile is None:
				profile = User(user_id=user.id)
			profile.team.add(team[0])
			profile.save()
