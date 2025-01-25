from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views import View
from django.contrib.auth import get_user_model
from .models import Like, Bookmark, Follow
from .serializers import LikeSerializer, BookmarkSerializer, FollowSerializer
from django.db.models import F

User = get_user_model()

# (Clean) 함수 이름이 모호하고,
# (Optimize) DB 접근 최소화를 위해 필요한 로직만 수행
def doLike(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        content_type = request.POST.get('content_type')
        object_id = request.POST.get('object_id')

        user = get_object_or_404(User, id=user_id)
        # (Optimize) 중복 Like를 막기 위한 필터 -> 1회 쿼리
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
        # (Optimize) DB insert 1회
        bm = Bookmark.objects.create(user=user, url=url, note=note)
        data = BookmarkSerializer(bm).data

        return JsonResponse({'bookmark': data}, status=201)
    return JsonResponse({'error': 'Invalid request method'}, status=400)


# (Clean) 클래스 이름은 직관적이지만 메서드별 로직이 부족
# (Optimize) get/post 분리 -> DB 접근 최소화
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
        # (Optimize) create or get -> 1회 쿼리
        follow_obj, created = Follow.objects.get_or_create(follower=follower_user, following=following_user)
        return JsonResponse({
            'followed': True,
            'created': created,
            'follower': follower_user.username,
            'following': following_user.username
        }, status=201)
