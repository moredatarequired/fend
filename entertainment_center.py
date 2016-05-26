import media
import fresh_tomatoes

upstream_color = media.Movie(
	"Upstream Color",
	"http://t2.gstatic.com/images?q=tbn:ANd9GcQnFKWpOXZOkJODjygLlrbqJiwz5tRE8MkQmJhYMip1HQCzLaIs",
	"https://www.youtube.com/watch?v=I1XXV4F5LpQ")
the_immaculate_conception_of_little_dizzle = media.Movie(
	"The Immaculate Conception of Little Dizzle",
	"http://www.newvideo.com/wp-content/uploads/2010/10/NNVG231550-F.jpg",
	"https://www.youtube.com/watch?v=pVaTHpLcVCA")
mr_nobody = media.Movie(
	"Mr. Nobody",
	"http://t1.gstatic.com/images?q=tbn:ANd9GcQ9hWxJsCyiWB894QDiPJEYqZf4RVJbKBOZ1k7r6XrSNOvVD3XK",
	"https://www.youtube.com/watch?v=flX_uN5IKJA")

movies = [upstream_color, the_immaculate_conception_of_little_dizzle, mr_nobody]
fresh_tomatoes.open_movies_page(movies)
