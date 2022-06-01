from date import Date
from movie_not_found_error import MovieNotFoundError
from movie import Movie

class ReleaseSchedule:
    def __init__(self, studio_name: str, season: str):
        self.studio_name = studio_name
        self.season = season
        self.movies_list = []
        self.schedule_dict = {}
    
    def add_movie(self, movie_object: Movie) -> None:
        self.movies_list.append(movie_object)
    
    def schedule_movie(self, movie_title: str, release_date: Date) -> None:
        movie_found = False
        for movie_object in self.movies_list:
            if movie_title == movie_object.title:
                movie_found = True
        if movie_found == True:
            self.schedule_dict[movie_title] = release_date
        else:
            raise MovieNotFoundError('Could not find movie. Please try again.')
    
    def postpone_movie(self, movie_title: str) -> Date: 
        if movie_title in self.schedule_dict:
            release_date = self.schedule_dict[movie_title]
            release_date.year += 1
            self.schedule_dict[movie_title] = release_date.year
            return release_date
        else:
            raise MovieNotFoundError('Could not postpone movie. Please try again.')
    
    def display_company_summary(self) -> None:
        length_of_schedule_dict = len(self.schedule_dict)
        total_num_of_premieres = len(self.movies_list)
        num_of_premieres_to_be_scheduled = total_num_of_premieres - length_of_schedule_dict
        print(self.studio_name)
        if length_of_schedule_dict == total_num_of_premieres and num_of_premieres_to_be_scheduled == 0:
            print(f'{self.season}: {total_num_of_premieres} movie premieres')
        else:
            print(f'{self.season}: {total_num_of_premieres} movie premieres ({num_of_premieres_to_be_scheduled} to be scheduled)')

    def display_schedule(self) -> None:
        print(f'{self.studio_name} {self.season}')
        for movie_object in self.movies_list:
            print(movie_object)
            if movie_object.title in self.schedule_dict:
                movie_date = self.schedule_dict[movie_object.title]
                print(movie_date)
            else:
                print('To Be Scheduled')