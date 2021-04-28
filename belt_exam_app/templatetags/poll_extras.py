from django import template
from belt_exam_app.models import Like
register = template.Library()

@register.simple_tag
def like_counter(id):    
    try:
        likes = Like.objects.filter(idea_id=id)        
        if(len(likes) > 0):
            likes_number = len(likes)
        else:
            likes_number = 0        
    except Like.DoesNotExist:
        likes_number = 0
    return likes_number