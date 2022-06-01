from schedule import ReleaseSchedule
from date import Date
from movie import Movie

studio_name = input('What is the name of your studio? ')
movie_season = input('What season do you have a schedule for? ')
movie_schedule = ReleaseSchedule(studio_name, movie_season)
user_action = ''
while user_action != '5':
    user_input = input('Enter 1 to add a movie, 2 to schedule a movie premiere, 3 to postpone a movie premiere, 4 for a summary, 5 to finish. ')
    user_action = user_input
    if user_input == '1':
        film_title = input('Movie Name: ')
        film_genre = input('Genre: ')
        film_info = Movie(film_title, film_genre)
        movie_schedule.add_movie(film_info)
    elif user_input == '2':
        try:
            film_title = input('Movie Name: ')
            movie_release_date = input('Date (mm-dd-yy): ')
            movie_date_1 = movie_release_date.split('-')
            movie_date_2 = Date(movie_date_1[0], movie_date_1[1], movie_date_1[2])
            movie_schedule.schedule_movie(film_title, movie_date_2)
        except:
            print('Could not find movie. Please try again.')
    elif user_input == "3": 
        try:
            film_title = input('Movie Name: ')
            postponed_movie_date = movie_schedule.postpone_movie(film_title)
            print(f'Postponed to {postponed_movie_date}')
        except:
            print('Could not postpone movie. Please try again.')
    elif user_input == '4':
        movie_schedule.display_company_summary()
movie_schedule.display_schedule()