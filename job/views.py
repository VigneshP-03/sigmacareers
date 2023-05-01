from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import date
# Create your views here.

def index(request):
    return render(request, 'index.html')

def admin_login(request):
    error=""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    d = {'error': error}
    return render(request, 'admin_login.html', d)

def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    rcount = Recruiter.objects.all().count()
    scount = StudentUser.objects.all().count()
    d = {'rcount': rcount, 'scount': scount}
    return render(request, 'admin_home.html', d)

def candidate_login(request):
    error=""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        if user:
            try:
                user1 = StudentUser.objects.get(user=user)
                if user1.type == "student":
                    login(request, user)
                    error="no"
                else:
                    error="yes"
            except:
                error="yes"
        else:
            error="yes"
    d = {'error': error}
    return render(request, 'candidate_login.html', d)

def candidate_home(request):
    if not request.user.is_authenticated:
        return redirect('candidate_login')
    user = request.user
    student = StudentUser.objects.get(user=user)
    error = ""
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        mob = request.POST['mobile']
        gen = request.POST['gender']

        student.user.first_name = f
        student.user.last_name = l
        student.user.mobile = mob
        student.user.gender = gen
        try:
            student.save()
            student.user.save()
            error="no"
        except:
            error="yes"
        try:
            i = request.FILES['image']
            student.image = i
            student.save()
            error="no"
        except:
            pass
    d = {'student': student, 'error': error}
    return render(request, 'candidate_home.html', d)

def candidate_signup(request):
    error = ""
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        i = request.FILES['image']
        p = request.POST['pwd']
        e = request.POST['email']
        mob = request.POST['mobile']
        gen = request.POST['gender']
        try:
            user = User.objects.create_user(first_name=f, last_name=l, username=e, password=p)
            StudentUser.objects.create(user=user, mobile=mob, image=i, gender=gen, type="student")
            error="no"
        except:
            error="yes"
    d = {'error': error}
    return render(request, 'candidate_signup.html', d)

def recruiter_login(request):
    error=""
    if request.method == 'POST':
        u = request.POST['email']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        if user:
            try:
                user1 = Recruiter.objects.get(user=user)
                if user1.type == "recruiter" and user1.status != "pending":
                    login(request, user)
                    error="no"
                else:
                    error="not"
            except:
                error="yes"
        else:
            error="yes"
    d = {'error': error}
    return render(request, 'recruiter_login.html', d)

def recruiter_home(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    user = request.user
    recruiter = Recruiter.objects.get(user=user)
    error = ""
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        mob = request.POST['mobile']
        gen = request.POST['gender']

        recruiter.user.first_name = f
        recruiter.user.last_name = l
        recruiter.user.mobile = mob
        recruiter.user.gender = gen
        try:
            recruiter.save()
            recruiter.user.save()
            error="no"
        except:
            error="yes"
        try:
            i = request.FILES['image']
            recruiter.image = i
            recruiter.save()
            error="no"
        except:
            pass
    d = {'recruiter': recruiter, 'error': error}
    return render(request, 'recruiter_home.html', d)

def recruiter_signup(request):
    error = ""
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        i = request.FILES['image']
        p = request.POST['pwd']
        e = request.POST['email']
        mob = request.POST['mobile']
        gen = request.POST['gender']
        com = request.POST['company']
        try:
            user = User.objects.create_user(first_name=f, last_name=l, username=e, password=p)
            Recruiter.objects.create(user=user, mobile=mob, image=i, gender=gen, company=com, type="recruiter", status="pending")
            error="no"
        except:
            error="yes"
    d = {'error': error}
    return render(request, 'recruiter_signup.html', d)

def view_candidates(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = StudentUser.objects.all()
    d = {'data': data}
    return render(request, 'view_candidates.html', d)

def delete_user(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    student = User.objects.get(id=pid)
    student.delete()
    return redirect('view_candidates')

def delete_recruiter(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    recruiter = User.objects.get(id=pid)
    recruiter.delete()
    return redirect('view_candidates')

def recruiter_pending(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.filter(status='pending')
    d = {'data': data}
    return render(request, 'recruiter_pending.html', d)

def add_job(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    error = ""
    if request.method == 'POST':
        jt = request.POST['jobtitle']
        sd = request.POST['startdate']
        sal = request.POST['salary']
        exp = request.POST['experience']
        loc = request.POST['location']
        skl = request.POST['skills']
        desc = request.POST['description']
        user = request.user
        recruiter = Recruiter.objects.get(user=user)
        try:
            Job.objects.create(recruiter=recruiter, start_date=sd, title=jt, salary=sal, experience=exp, location=loc, skills=skl, description=desc, creationdate=date.today())
            error="no"
        except:
            error="yes"
    d = {'error': error}
    return render(request, 'add_job.html', d)

def job_list(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    user = request.user
    recruiter = Recruiter.objects.get(user=user)
    job = Job.objects.filter(recruiter=recruiter)
    d = {'job': job}
    return render(request, 'job_list.html', d)

def edit_job(request, pid):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    error = ""
    job = Job.objects.get(id=pid)
    if request.method == 'POST':
        jt = request.POST['jobtitle']
        sd = request.POST['startdate']
        sal = request.POST['salary']
        exp = request.POST['experience']
        loc = request.POST['location']
        skl = request.POST['skills']
        desc = request.POST['description']
        job.title = jt
        job.salary = sal
        job.experience = exp
        job.location = loc
        job.skills = skl
        job.description = desc
        try:
            job.save()
            error="no"
        except:
            error="yes"
        if sd:
            try:
                job.start_date = sd
                job.save()
            except:
                pass
        else:
            pass
    d = {'error': error, 'job': job}
    return render(request, 'edit_job.html', d)

def change_status(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    recruiter = Recruiter.objects.get(id=pid)
    error=""
    if request.method == "POST":
        recruiter.status = request.POST['status']
        try:
            recruiter.save()
            error="no"
        except:
            error="yes"
    d = {'recruiter': recruiter, 'error': error}
    return render(request, 'change_status.html', d)

def change_adminpass(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error=""
    if request.method == "POST":
        c = request.POST['currentpass']
        n = request.POST['newpass']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="not"
        except:
            error="yes"
    d = {'error': error}
    return render(request, 'change_adminpass.html', d)

def change_userpass(request):
    if not request.user.is_authenticated:
        return redirect('candidate_login')
    error=""
    if request.method == "POST":
        c = request.POST['currentpass']
        n = request.POST['newpass']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="not"
        except:
            error="yes"
    d = {'error': error}
    return render(request, 'change_userpass.html', d)

def change_recruiterpass(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    error=""
    if request.method == "POST":
        c = request.POST['currentpass']
        n = request.POST['newpass']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="not"
        except:
            error="yes"
    d = {'error': error}
    return render(request, 'change_recruiterpass.html', d)

def recruiter_accept(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.filter(status='Accept')
    d = {'data': data}
    return render(request, 'recruiter_accept.html', d)

def recruiter_all(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.all()
    d = {'data': data}
    return render(request, 'recruiter_all.html', d)

def latest_jobs(request):
    job = Job.objects.all().order_by('-start_date')
    d = {'job': job}
    return render(request, 'latest_jobs.html', d)

def job_list(request):
    job = Job.objects.all().order_by('-start_date')
    d = {'job': job}
    return render(request, 'job_list.html', d)

def user_latestjobs(request):
    job = Job.objects.all().order_by('-start_date')
    user = request.user
    student = StudentUser.objects.get(user=user)
    data = Apply.objects.filter(student=student)
    li = []
    for i in data:
        li.append(i.job.id)
    d = {'job': job, 'li': li}
    return render(request, 'user_latestjobs.html', d)

def job_detail(request, pid):
    job = Job.objects.get(id=pid)
    d = {'job': job}
    return render(request, 'job_detail.html', d)

def apply_job(request, pid):
    if not request.user.is_authenticated:
        return redirect('candidate_login')
    error = ""
    user = request.user
    student = StudentUser.objects.get(user=user)
    job = Job.objects.get(id=pid)
    date1 = date.today()
    if job.start_date < date1:
        error = "close"
    else:
        if request.method == 'POST':
            res = request.FILES['resume']
            Apply.objects.create(job=job, student=student, resume=res, applydate=date.today())
            error="open"
    d = {'error': error}
    return render(request, 'apply_job.html', d)

def applied_list(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    data = Apply.objects.all()
    d = {'data': data}
    return render(request, 'applied_list.html', d)

def Logout(request):
    logout(request)
    return redirect('index')
