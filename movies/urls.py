from django.urls import path


from movies.views import MovieListView, MovieViewSet

movie_list = MovieViewSet.as_view(actions={
    "get": "list",
    "post": "create",
})

urlpatterns = [
    # path('', movie_list_view, name="movie_list"),
    path('', MovieListView.as_view(), name='movie_list'),
    path("api/cinema/movies/", movie_list, name="api-movie-list"),
]

app_name = "movies"
