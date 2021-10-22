from django.urls import path
from api.views import ( UserList, UserDetails, PostList, PostDetail,
                        CommentList, Commentdetail, CategoryList,CategoryDetail )


urlpatterns = [
    path('users/', UserList.as_view(), name='User'),
    path('users/<int:pk>/', UserDetails.as_view(), name='UserDetail'),
    path('posts/', PostList.as_view(), name = 'posts'),
    path('posts/<int:pk>/', PostDetail.as_view(), name = 'postDetail'),
    path('comment/', CommentList.as_view(), name = 'commentList'),
    path('comment/<int:pk>/', Commentdetail.as_view()),
    path('categories/', CategoryList.as_view()),
    path('categories/<int:pk>/', CategoryDetail.as_view()),

    
    
    
    
]

# urlpatterns = [
#     # code omitted for brevity
#     path('categories/', views.CategoryList.as_view()),
#     path('categories/<int:pk>/', views.CategoryDetail.as_view()),
# ]

