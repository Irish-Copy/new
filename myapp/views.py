from django.shortcuts import render, HttpResponse

topics = [
{'id':1, 'title':'routing', 'body':'Routing is...'},
{'id':2, 'title':'view', 'body':'view is...'},
{'id':3, 'title':'model', 'body':'model is...'}
]

def HTMLTemlate(articleTag):
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return f'''
    <html>
    <body>
        <h1><a href="/">Django</a></h1>
        <ol>
            {ol}
        </ol>
        {articleTag}
    </body>
    </html>
    '''

def index(request):
    article ='''
    <h2>Welcome<h2>
    Hollo, Django
    '''
    return HttpResponse(HTMLTemlate(article))

def read(request,id):
    global topics
    article =''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'

    return HttpResponse(HTMLTemlate(article))
def create(request):

    return HttpResponse('create!')

