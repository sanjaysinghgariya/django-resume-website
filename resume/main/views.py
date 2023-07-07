from django.shortcuts import render

# Create your views here.
def index(request):
    name = "Sanjay Singh Gariya"
    job_title  = "Python Django Developer"
    about_me = '''As a fresher Python Django developer, 
    you are embarking on an exciting journey in the world of web development. 
    Python and Django are powerful tools for building dynamic and robust web applications, 
    and your passion for this technology demonstrates your eagerness to learn and grow in this field.'''
    
    qualification = (('Class10','KMSB Himayala Inter College'), ('Class12','KMSB Himayala Inter College'), ('BSc(H)Mathematics','Ramanujan College(Delhi University)'))
    context = {
        'name':name,
        'job_title': job_title,
        'about_me': about_me,
        'qualification': qualification,
    }
    return render(request, 'main/index.html', context)


def languages(request):
    languages = ('Python', 'C++', 'C#', 'Java', 'JavaScript', 'Golang', 'Kotlin', 'Django', 'Flask')
    context = {
        'languages' : languages
    }
    return render(request, 'main/languages.html', context)

def projects(request):
    projects = (('Django','https://github.com/sanjaysinghgariya/my-own-cart-django-project'),
                ('python','https://github.com/sanjaysinghgariya/Python-Projects'),
                ('Git&Github', 'https://github.com/sanjaysinghgariya/git-in-one-Video'))
        
    context = {
        'projects' :projects
    }
    return render(request, 'main/projects.html', context)

