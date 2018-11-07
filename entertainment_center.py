import fresh_tomatoes
import media

#URIs that will be used for the previews and the posters
wikimedia = "http://upload.wikimedia.org/wikipedia"
youTube = "https://www.youtube.com/watch?v="

toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys taht come to life",
    wikimedia + "/en/1/13/Toy_Story.jpg",
    youTube + "KYz2wyBy3kc")

avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    wikimedia + "/id/b/b0/Avatar-Teaser-Poster.jpg",
    youTube + "-9ceBgWV8io")

school_of_rock = media.Movie(
    "School Of Rock",
    "Using Rock Music To Learn",
    wikimedia + "/en/1/11/School_of_Rock_Poster.jpg",
    youTube + "3PsUJFEBC74")

ratatouille = media.Movie(
    "Ratatouille",
    "A rat is a chef in Paris",
    wikimedia + "/en/5/50/RatatouillePoster.jpg",
    youTube + "c3sBBRxDAqk")

midnight_in_paris = media.Movie(
    "Midnight In Paris",
    "Going back in time to meet authors",
    wikimedia + "/en/9/9f/Midnight_in_Paris_Poster.jpg",
    youTube + "FAfR8omt-CY")

hunger_games = media.Movie(
    "Hunger Games",
    "A really real reality show",
    wikimedia + "/en/4/42/HungerGamesPoster.jpg",
    youTube + "PbA63a7H0bo")

#List of the moview that will be sown on the page
movies = [
    toy_story, avatar, school_of_rock,
    ratatouille, midnight_in_paris, hunger_games]

#Generate the HTML page with the movies
fresh_tomatoes.open_movies_page(movies)
