from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.core.context_processors import csrf
from userprofile.forms import UserProfileForm
from django.contrib.auth.decorators import login_required

@login_required
def user_profile(request):
	if request.method == 'POST':
		form = UserProfileForm(request.POST, instance=request.user.profile)
		if form.is_valid():
			form.save()
			return redirect('mainsite.views.loggedin')

	else:
		user = request.user
		profile = user.profile
		form = UserProfileForm(instance=profile)

	args = {}
	args.update(csrf(request))

	args['form'] = form

	return render_to_response('userprofile/profile.html', args)

# Create your views here.
