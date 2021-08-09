
from commentapp.models import Comment
from django.http import HttpResponseForbidden

def comment_ownership_require(func):
    def decorated(request,*args,**kwargs):
        target_comment = Comment.objects.get(pk=kwargs['pk'])
        if target_comment.writer == request.user:
            return func(request,*args,**kwargs)
        else:
            return HttpResponseForbidden()
    return decorated