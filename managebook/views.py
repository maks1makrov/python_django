from django.db.models import Q, Value, CharField
from django.db.models.functions import Cast
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


# class BookView(View):
#     def get(self, request):
#         return HttpResponse("hello maks")
from managebook.forms import CommentForm
from managebook.models import Book


class BookView(View):
    # @method_decorator(cache_page(5))
    def get(self, request):
        response = {}
        if request.user.is_authenticated:
            quary = Q(book_like__user_id=request.user.id)
            sub_quary = Book.objects.filter(quary). \
                annotate(user_rate=Cast('book_like__rate', CharField())). \
                prefetch_related("author", "genre", "comment", "comment__user")
            result = Book.objects.filter(~quary).annotate(user_rate=Value(-1, CharField())). \
                prefetch_related("author", "genre", "comment", "comment__user").union(sub_quary)
            response['content'] = result.all()
        else:
            response['content'] = Book.objects. \
                prefetch_related("author", "genre", "comment", "comment__user").all()
        response['form'] = CommentForm()
        return render(request, "index.html", response)
