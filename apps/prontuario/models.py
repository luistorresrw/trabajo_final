from django.db import models
from django.contrib.auth.models import User
from django.db.models import signals

class UserProfile(models.Model):
	user = models.OneToOneField(User,related_name='profile')
	pil  = models.CharField(max_length=3)
	factor_vencimiento = models.IntegerField()
	fecha_ultimo_cambio = models.DateField()
	primer_logueo = models.BooleanField(default = True)
	
	class Meta:
		db_table = 'UserProfile'

	def user_profile(sender, instance, signal, *args, **kwargs):
		profile, new = UserProfile.objects.get_or_create(user=instance)

	signals.post_save.connect(user_profile, sender=User)
