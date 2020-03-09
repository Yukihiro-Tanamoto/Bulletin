from django.shortcuts import render

class IndexView(View):
    def get(self, request, *args, **kwargs):
        # Postsテーブルのデータを全て取得
        queryset = Posts.objects.all().order_by('-created_at')
        # 値付きでpost.htmlに飛ぶ
        return render(request, 'posts/post.html', {'posts': queryset})


index = IndexView.as_view()