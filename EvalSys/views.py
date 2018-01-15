from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from .forms import HomeForm, IndexForm
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, Http404
from django.template.loader import render_to_string
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Qualia
from django.db.models import Q

# with open('/Users/ghamzak/PycharmProjects/OntologyMapping/TelicRelations.json') as df:
# 	data_telic = json.load(df)

# with open('/Users/ghamzak/PycharmProjects/OntologyMapping/AgentiveRelations.json') as df2:
# 	data_agentive = json.load(df2)

# with open('/Users/ghamzak/PycharmProjects/OntologyMapping/ConstitutiveRelations.json') as df3:
# 	data_const = json.load(df3)

# import pickle

# def load_obj(name ):
#     with open('obj/' + name + '.pkl', 'rb') as f:
#         return pickle.load(f)
# with open('/Users/ghamzak/PycharmProjects/OntologyMapping/obj/'+'telic_25' + '.pkl', 'rb') as f:
# 	telic_25 = pickle.load(f)



class IndexView(TemplateView):
	"""docstring for IndexView"""
	template_name = 'EvalSys/index.html'

	def get(self, request, *args, **kwargs):
		userform = IndexForm()
		args = {'userform': userform}
		return render(request, self.template_name, args)
	def post(self, request, *args, **kwargs):
		userlist = {'sb': 'Susan', 'cb': 'Claire'}
		userform = IndexForm(request.POST)
		if userform.is_valid():
			print('form is valid')
			uservar = userform.cleaned_data.get('user')

			if uservar in userlist.keys():
				print('User is authenticated.')
				user_name = userlist[uservar]
				request.session['user_name'] = uservar
				print(request.session['user_name'])
				return HttpResponse('Thank you %s . Please add 4588 to the end of URL to see your first task.' % user_name)
			else:
				user_name = ''
				return HttpResponse('Sorry! You are not an authenticated user!')

		
		
class ThanksView(TemplateView):
	"""docstring for ClassName"""
	template_name = 'EvalSys/thanks.html'
	def get(self, request):
		from random import randint

		rndTelic = randint(4588, 5363)
		while Qualia.objects.get(pk=rndTelic).post == True:
			rndTelic = randint(4588, 5363)
		rndConstitutive = randint(5364, 5845)
		while Qualia.objects.get(pk=rndConstitutive).post == True:
			rndConstitutive = randint(5364, 5845)
		rndintAgentive = randint(5846, 5960)
		while Qualia.objects.get(pk=rndintAgentive).post == True:
			rndintAgentive = randint(5846, 5960)

		args = {'rt': rndTelic, 'rc': rndConstitutive, 'ra': rndintAgentive}
		return render(request, self.template_name, args)


class TelicDetailView(DetailView):
	# model = Qualia
	# if request.session['user_name'] == 'sb':
	# 	queryset = Qualia.objects.filter(sb_annotations = False)
	queryset = Qualia.objects.filter(post=False)
	template_name = 'EvalSys/qualia_detail.html'

	def get(self, request, *args, **kwargs):
		if request.session['user_name'] == 'sb':
			queryset = Qualia.objects.filter(sb_annotations = False)
		elif request.session['user_name'] == 'cb':
			queryset = Qualia.objects.filter(cb_annotations = False)

		form = HomeForm()

		obj = self.get_object()
		print(obj.node)
		print(obj.pk)
		if obj.pk < 5364:
			return render(request, self.template_name, {'form': form, 'object': obj})
		elif obj.pk < 5846:
			return render(request, 'EvalSys/qualia_detail_constitutive.html', {'form': form, 'object': obj})
		else:
			return render(request, 'EvalSys/qualia_detail_agentive.html', {'form': form, 'object': obj})


	def post(self, request, *args, **kwargs):
		form = HomeForm(request.POST)
		obj = self.get_object()
		print(obj.post)
		if form.is_valid():
			print(form.cleaned_data.get('reasonable'))
			print(obj.post)
			if request.session['user_name'] == 'sb':
				obj.sb_annotations = form.cleaned_data.get('reasonable')
				print(obj.sb_annotations)
			elif request.session['user_name'] == 'cb':
				obj.cb_annotations = form.cleaned_data.get('reasonable')
				print(obj.cb_annotations)
			# obj.post = form.cleaned_data.get('reasonable')
			# print(obj.post)
			obj.save()
		return HttpResponseRedirect('thanks')


# class AgentiveDetailView(DetailView):
# 	queryset = Qualia.objects.filter(qualename__iexact='Agentive')
# 	template_name = 'EvalSys/qualia_detail_agentive.html'

# 	def get(self, request, *args, **kwargs):
# 		form = HomeForm()
# 		return render(request, self.template_name, {'form': form, 'object': self.get_object()})

# 	def post(self, request, *args, **kwargs):
# 		form = HomeForm(request.POST)
# 		obj = self.get_object()
# 		print(obj.post)
# 		if form.is_valid():
# 			print(form.cleaned_data.get('reasonable'))
# 			obj.post = form.cleaned_data.get('reasonable')
# 			obj.save()
# 		return HttpResponse('Thanks! To go to the next page, increase the number in the URL by one. ')

# class ConstitutiveDetailView(DetailView):
# 	queryset = Qualia.objects.filter(qualename__iexact='Constitutive')
# 	template_name = 'EvalSys/qualia_detail_constitutive.html'

# 	def get(self, request, *args, **kwargs):
# 		form = HomeForm()
# 		return render(request, self.template_name, {'form': form, 'object': self.get_object()})

# 	def post(self, request, *args, **kwargs):
# 		form = HomeForm(request.POST)
# 		obj = self.get_object()
# 		print(obj.post)
# 		if form.is_valid():
# 			print(form.cleaned_data.get('post'))
# 			# obj.post = form.cleaned_data.get('post')
# 			# obj.save()
# 		return HttpResponse('Thanks! To go to the next page, increase the number in the URL by one. ')


class HomeView(ListView):
	template_name = 'EvalSys/home.html'
	thanks_page = 'EvalSys/thanks.html'
	

	def get(self, request, *args, **kwargs):
		object_list = Qualia.objects.filter(Q(qualename__iexact="Telic") & Q(post=False))
		form = HomeForm()
		print('getting request')
		args2 = {'form': form, 'object_list': object_list}
		return render(request, self.template_name, args2)

	def post(self, request, *args, **kwargs):
		form = HomeForm(request.POST)
		print(request.POST)
		myobjects = Qualia.objects.filter(Q(category__iexact="telic1") & Q(post=False))

		if form.is_valid():
			print("form is valid")
			print(form)
			print(form.cleaned_data.get('post'))
			return HttpResponseRedirect('Telic1')
		if form.errors:
			print(form.errors)
		return render(request, self.thanks_page)

# class HomeView2(ListView):
# 	template_name = 'EvalSys/home.html'
# 	thanks_page = 'EvalSys/thanks.html'
	

# 	def get(self, request, *args, **kwargs):
# 		object_list = Qualia.objects.filter(Q(category__iexact="telic2") & Q(post=False))
# 		form = HomeForm()
# 		print('getting request')
# 		args2 = {'form': form, 'object_list': object_list}
# 		return render(request, self.template_name, args2)

# 	def post(self, request, *args, **kwargs):
# 		form = HomeForm(request.POST)
# 		print(request.POST)
# 		myobjects = Qualia.objects.filter(Q(category__iexact="telic2") & Q(post=False))

# 		if form.is_valid():
# 			print("form is valid")
# 			print(form)
# 			print(form.cleaned_data.get('post'))
# 			return HttpResponseRedirect('Telic1')
# 		if form.errors:
# 			print(form.errors)
# 		return render(request, self.thanks_page)



# class AgentiveView(TemplateView):
# 	"""docstring for AgantiveView"""
# 	template_name = 'EvalSys/agentive.html'

# 	def get(self, request):
# 		form = HomeForm()
# 		return render(request, self.template_name, {'form': form, 'dic_agentive': data_agentive})


# class ConstitutiveView(TemplateView):
# 	"""docstring for ClassName"""
# 	template_name = 'EvalSys/constitutive.html'

# 	def get(self, request):
# 		form = HomeForm()
# 		return render(request, self.template_name, {'form': form, 'dic_const': data_const})


