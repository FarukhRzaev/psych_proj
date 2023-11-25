from blog.models import Hashtag


def get_hashtags(request):
    return {"hashtags": Hashtag.objects.all()}
