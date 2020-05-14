from django.conf.urls import url
from graphene_django.views import GraphQLView
from django.urls import path


urlpatterns = [
    path('graphql', GraphQLView.as_view(graphiql=True)),
]