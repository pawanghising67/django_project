from django.shortcuts import render

posts = [
	{
		'author': 'Pawan',
		'title': 'BlogPost 1',
		'content': 'First post content',
		'date_posted': 'January 23,2018'
	},
	{
		'author': 'Ghising',
		'title': 'BlogPost 2',
		'content': 'second post content',
		'date_posted': 'January 24,2018'
	}

]


def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)


def about(request):
	return render(request, 'blog/about.html')


