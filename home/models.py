from django.db import models

# Create your models here.

class UserProfile(models.Model):
	first_name =models.CharField(max_length=80)
	last_name =models.CharField(max_length=80)
	phone =models.CharField(max_length=10)
	email =models.EmailField()
	password =models.CharField(max_length=50)
	confirm_password=models.CharField(max_length=50)
	

class Vacancy(models.Model):
	title =models.CharField(max_length=150)
	post =models.CharField(max_length=200,null=True,blank=True)
	seats =models.CharField(max_length=5,null=True,blank=True)
	exam_date =models.CharField(max_length=15,null=True,blank=True)
	regis_start =models.CharField(max_length=20,null=True,blank=True)
	regis_end =models.CharField(max_length=20,null=True,blank=True)
	state =models.CharField(max_length=60,null=True,blank=True)
	description =models.TextField(max_length=500,null=True,blank=True)
	exam_fees_general =models.IntegerField(null=True,blank=True)
	exam_fees_obc =models.IntegerField(null=True,blank=True)
	exam_fees_sc =models.IntegerField(null=True,blank=True)
	portal_fee =models.IntegerField(null=True,blank=True)
	main_website =models.URLField(null=True,blank=True)
	notification =models.URLField()
	result =models.URLField(null=True,blank=True)
	admit_card =models.URLField(null=True,blank=True)
	job_type =models.CharField(max_length=30)
	eligibility =models.CharField(max_length=200)
	age_limit =models.CharField(max_length=200,null=True,blank=True)
	guidelines =models.CharField(max_length=200,null=True,blank=True)
	createdat =models.DateTimeField(auto_now_add=True)
	updatedat =models.DateTimeField(auto_now=True)


	

