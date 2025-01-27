from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views import View
from django.contrib.auth import get_user_model
from .models import Like, Bookmark, Follow
from .serializers import LikeSerializer, BookmarkSerializer, FollowSerializer
from django.db.models import F

User = get_user_model()

# (Clean) 이름이 모호하고, 다양한 책임이 한 함수에 뭉쳐지기 쉬움
def doLike(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        content_type = request.POST.get('content_type')
        object_id = request.POST.get('object_id')

        # 사용자 확인
        user = get_object_or_404(User, id=user_id)
        # (Optimize) 중복 제거 시도, 그러나 로직이 함수와 뒤섞임
        like_exists = Like.objects.filter(user=user, content_type=content_type, object_id=object_id).exists()
        if not like_exists:
            Like.objects.create(user=user, content_type=content_type, object_id=object_id)
        return JsonResponse({'message': 'Like processed'}, status=201)

    return JsonResponse({'error': 'Invalid request method'}, status=400)


def doBookmark(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        url = request.POST.get('url')
        note = request.POST.get('note', '')

        user = get_object_or_404(User, id=user_id)
        bm = Bookmark.objects.create(user=user, url=url, note=note)
        data = BookmarkSerializer(bm).data
        return JsonResponse({'bookmark': data}, status=201)

    return JsonResponse({'error': 'Invalid request method'}, status=400)


# (Clean) 클래스 이름은 직관적이지만, HTTP 메서드별 세분화 부족
class FollowView(View):
    def get(self, request):
        user_id = request.GET.get('user_id')
        if user_id:
            follows = Follow.objects.select_related('follower', 'following').filter(follower_id=user_id)
        else:
            follows = Follow.objects.select_related('follower', 'following').all()

        data = FollowSerializer(follows, many=True).data
        return JsonResponse({'follows': data}, safe=False)

    def post(self, request):
        follower_id = request.POST.get('follower_id')
        following_id = request.POST.get('following_id')
        follower_user = get_object_or_404(User, id=follower_id)
        following_user = get_object_or_404(User, id=following_id)

        follow_obj, created = Follow.objects.get_or_create(follower=follower_user, following=following_user)
        return JsonResponse({
            'followed': True,
            'created': created,
            'follower': follower_user.username,
            'following': following_user.username
        }, status=201)
