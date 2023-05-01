"""jobportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from job .views import *

urlpatterns = [
    path('adminpanel/', admin.site.urls),
    path('', index, name="index"),
    path('admin_login', admin_login, name="admin_login"),
    path('admin_home', admin_home, name="admin_home"),
    path('candidate_login', candidate_login, name="candidate_login"),
    path('candidate_signup', candidate_signup, name="candidate_signup"),
    path('candidate_home', candidate_home, name="candidate_home"),
    path('recruiter_login', recruiter_login, name="recruiter_login"),
    path('recruiter_signup', recruiter_signup, name="recruiter_signup"),
    path('recruiter_home', recruiter_home, name="recruiter_home"),
    path('view_candidates', view_candidates, name="view_candidates"),
    path('delete_user/<int:pid>', delete_user, name="delete_user"),
    path('recruiter_pending', recruiter_pending, name="recruiter_pending"),
    path('recruiter_accept', recruiter_accept, name="recruiter_accept"),
    path('recruiter_all', recruiter_all, name="recruiter_all"),
    path('delete_recruiter/<int:pid>', delete_recruiter, name="delete_recruiter"),
    path('change_status/<int:pid>', change_status, name="change_status"),
    path('change_adminpass', change_adminpass, name="change_adminpass"),
    path('change_recruiterpass', change_recruiterpass, name="change_recruiterpass"),
    path('change_userpass', change_userpass, name="change_userpass"),
    path('add_job', add_job, name="add_job"),
    path('job_list', job_list, name="job_list"),
    path('edit_job/<int:pid>', edit_job, name="edit_job"),
    path('latest_jobs', latest_jobs, name="latest_jobs"),
    path('user_latestjobs', user_latestjobs, name="user_latestjobs"),
    path('job_detail/<int:pid>', job_detail, name="job_detail"),
    path('apply_job/<int:pid>', apply_job, name="apply_job"),
    path('applied_list', applied_list, name="applied_list"),
    path('Logout', Logout, name="Logout"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
