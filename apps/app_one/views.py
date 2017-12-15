from django.shortcuts import render, HttpResponse, redirect
from .models import User, Message, Comment


# Create your views here.
def index(request):
    print("This is index method in views.py")
    context = {
        # 'users': User.objects.filter(id=2),
        'users': User.objects.all(),
        # 'messages': Message.objects.filter(user_id=2),
        # 'messages': Message.objects.all(),
    }
    # users=User.objects.all()
    # print(users[0].messages)
    return render(request, 'app_one/index.html', context)


def post_message(request):
    print("This is post_message method in views.py")

    if request.method == "POST":
        print("POST, messages")
        new_message = request.POST['message']
        print("Message is:", new_message)

        this_user = User.objects.get(id=4)
        print(this_user.id, this_user.first_name, this_user.last_name, this_user.email)

        # user = request.session.this_user
        # print("Session user is:", user.first_name)

        saved_message = Message.objects.create(user_id=this_user, message=new_message)
        print(saved_message)

        return redirect('app_one:post_message')
    return redirect('/')


def post_comment(request, ms_id):
    print("This is post_comment method in views.py")

    if request.method == "POST":
        print("POST, comments")
        print(ms_id)
        ms_id = int(ms_id)
        new_comment = request.POST['comment']
        print("Comment is:", new_comment)

        this_user = User.objects.get(id=4)
        print(this_user.id, this_user.first_name, this_user.last_name, this_user.email)

        this_message = Message.objects.get(id=ms_id)

# creating Comment object
        saved_comment = Comment.objects.create(user_id=this_user, message_id=this_message, comment=new_comment)
        print(saved_comment)

    return redirect('/')


# nonfunctional; for logoff button on html
def logoff(request):
    print("This is logoff method in views.py")
    return redirect('/')
