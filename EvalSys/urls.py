from django.conf.urls import url, include
from EvalSys.views import IndexView, ThanksView, TelicDetailView, HomeView # ConstitutiveView #AgentiveDetailView # , AgentiveView

urlpatterns = [
	url(r'^$', IndexView.as_view(), name='index'),
	url(r'^Telic/Telic1', HomeView.as_view(), name='home'),
	# url(r'^Telic/Telic2', HomeView2.as_view(), name='home2'),
	url(r'^(?P<pk>\d+)', TelicDetailView.as_view(), name='detail'),
	# url(r'^(?P<pk>\d+)', AgentiveDetailView.as_view(), name='detail2'),
	# url(r'^Agentive/', AgentiveView.as_view(), name='agentive'),
	# url(r'^Constitutive/', ConstitutiveView.as_view(), name='constitutive'),
	url(r'^thanks/', ThanksView.as_view(), name='thanks'),
	]