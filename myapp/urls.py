from django.urls import path
from . import views
import myapp
from .views import CustomLoginView
from .views import SignUpView
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import ProjectJoinView
from .views import AccountView
from django.urls import path
from .views import GoalCreateView, MilestoneCreateView
from django.urls import path
from .views import StartMilestoneView, CompleteMilestoneView
from .views import project_participants
from django.urls import path
from . import views
from django.urls import path
from .views import AccountView
from django.urls import path
from django.urls import path
from .views import delete_milestone 


urlpatterns = [
    # ユーザー登録
    path('signup/', views.SignUpView.as_view(), name='signup'),

    # プロジェクトのリスト表示
    path('projects/', views.ProjectListView.as_view(), name='project_list'),

    # プロジェクトの詳細表示
    path('projects/<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),

    # プロジェクトの作成
    path('projects/create/', views.ProjectCreateView.as_view(), name='project_create'),

    # ログイン
    path('login/', views.CustomLoginView.as_view(), name='login'),

    # ログアウト
    path('logout/', LogoutView.as_view(), name='logout'),

    # プロジェクトへの参加
    path('projects/join/<int:pk>/', views.ProjectJoinView.as_view(), name='project_join'),

    # アカウントページ
    path('account/', views.AccountView.as_view(), name='account'),
    path('account/<str:username>/', views.AccountView.as_view(), name='account'),

    # ゴールの作成（プロジェクトIDを指定）
    path('projects/<int:pk>/goal/create/', views.GoalCreateView.as_view(), name='goal_create'),

    # マイルストーンの作成（ゴールIDを指定）
    path('goals/<int:goal_id>/milestone/create/', views.MilestoneCreateView.as_view(), name='milestone_create'),

    # 子マイルストーンの作成（親マイルストーンIDを指定）
    path('milestones/<int:parent_milestone_id>/milestone/create/', views.MilestoneCreateView.as_view(), name='milestone_create_with_parent'),
    
    path('milestones/<int:pk>/start/', StartMilestoneView.as_view(), name='start_milestone'),
    
    path('milestones/<int:pk>/complete/', CompleteMilestoneView.as_view(), name='complete_milestone'),
    
    path('projects/<int:pk>/participants/', project_participants, name='project_participants'),
    
    path('milestone/<int:pk>/delete/', delete_milestone, name='delete_milestone'),
    
]