from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# import pickle
# with open('/Users/ghamzak/PycharmProjects/OntologyMapping/obj/'+'telicset1' + '.pkl', 'rb') as f:
# 	telicset = pickle.load(f)

class Qualia(models.Model):
	node = models.CharField(max_length=50)
	qualevalue = models.CharField(max_length=500)
	post = models.BooleanField(default=False)
	qualename = models.CharField(max_length=20, default='Telic')
	sb_annotations = models.BooleanField(default=False)
	cb_annotations = models.BooleanField(default=False)
	# cb_annotator = models.
	# category = models.CharField(max_length=20, default='telic1')
	# slug = models.SlugField(unique=True)

	def __str__(self):
		return self.node

	# def get_absolute_url(self):
	# 	return reverse('detail', kwargs={'pk': self.pk})


# class Annotation(models.Model):
# 	question = models.CharField(max_length=1000)
# 	answered = models.BooleanField()


# do not uncomment this, it makes a mess. Instead, enter the interactive python through shell, and type it there. 
# of course you need to type the above file import too.

# for i in telicset:
# 	q = Qualia(node=i[0], qualevalue=i[1], post=False, qualename='Telic', category='telic1')
# 	q.save()


# for Agentive (after file import):
# for i in agentiveset:
#	q = Qualia(node=i[0], qualevalue=i[1], post=True, qualename='Agentive')
#	q.save()

# for Constitutive (after file import):
# for i in constitutiveeset:
#	q = Qualia(node=i[0], qualevalue=i[1], post=True, qualename='Constitutive')
#	q.save()

