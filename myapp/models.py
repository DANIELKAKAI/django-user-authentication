from django.db import models
from django.contrib.auth.models import (
BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
	def create_user(self, email, password,role):
		if not email:
			raise ValueError('Users must have an email address')
		user = self.model(
		email=self.normalize_email(email)
		)
		user.role = role
		user.set_password(password)
		user.save(using=self._db)
		return user


	def create_superuser(self, email,password):
		user = self.create_user(
		email,
		password=password
		)
		user.is_admin = True
		user.save(using=self._db)
		return user


class MyUser(AbstractBaseUser):
	email = models.EmailField(
	verbose_name='email address',
	max_length=255,
	unique=True,
	)
	role = models.CharField(max_length=50)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	objects = MyUserManager()
	USERNAME_FIELD = 'email'
	def __str__(self):
		return self.email
	def has_perm(self, perm, obj=None):
		# Simplest possible answer: Yes, always
		return True
	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
		# Simplest possible answer: Yes, always
		return True
	@property
	def is_staff(self):
		"Is the user a member of staff?"
		# Simplest possible answer: All admins are staff
		return self.is_admin