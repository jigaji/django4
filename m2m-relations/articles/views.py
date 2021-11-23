from django.shortcuts import render

from articles.models import Article, Relationship


def articles_list(request):
    article = Article.objects.all().order_by('-published_at')
    tags = Relationship.objects.all()

    template = 'articles/news.html'
    context = {
        'object_list': article,
        'tags': tags,

    }


    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template, context)
