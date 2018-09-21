# encoding: utf-8

def save_profile_team(strategy, details, backend, user, response, *args, **kwargs):
	print(strategy.session_get('key'))
# profile = user.get_profile()
# if profile is None:
# 	profile = Profile(user_id=user.id)
# profile.gender = response.get('gender')
# profile.link = response.get('link')
# profile.timezone = response.get('timezone')
# profile.save()
