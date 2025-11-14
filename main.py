from flask import Flask, jsonify, request
from patterns.media_library import MediaLibrary
from patterns.observer import MediaObserver
from media.book.book import Book
from media.book.book_adapter import BookAdapter
from media.movie.movie import Movie
from media.movie.movie_adapter import MovieAdapter
from media.music.music import Music
from media.music.music_adapter import MusicAdapter

app = Flask(__name__)
library = MediaLibrary()
observer = MediaObserver()
library.attach(observer)


@app.route('/media', methods=['GET'])
def get_all_media():
    media_list = []
    for m in library:
        media_list.append({
            "title": m.get_title(),
            "creator": m.get_creator(),
            "year": m.get_year(),
            "genre": m.get_genre(),
            "rating": m.get_rating()
        })
    return jsonify(media_list)


@app.route('/media', methods=['POST'])
def add_media():
    data = request.get_json()
    media_type = data.get("type")
    title = data.get("title")
    genre = data.get("genre")
    year = data.get("year")
    extra = data.get("extra")  # author/director/artist

    if media_type == "book":
        media_obj = Book(title, extra, year, genre)
        media = BookAdapter(media_obj)
    elif media_type == "movie":
        media_obj = Movie(title, extra, year, genre)
        media = MovieAdapter(media_obj)
    elif media_type == "music":
        media_obj = Music(title, extra, year, genre)
        media = MusicAdapter(media_obj)
    else:
        return jsonify({"error": "Invalid media type"}), 400

    library.add_media(media)
    return jsonify({"message": f"{media_type.capitalize()} added successfully."}), 201


@app.route('/media/genre/<genre>', methods=['GET'])
def filter_genre(genre):
    filtered = library.filter_by_genre(genre)
    media_list = []
    for m in filtered:
        media_list.append({
            "title": m.get_title(),
            "creator": m.get_creator(),
            "genre": m.get_genre(),
            "year": m.get_year(),
            "rating": m.get_rating()
        })
    return jsonify(media_list)


@app.route('/media/<title>/rating', methods=['POST'])
def set_rating(title):
    data = request.get_json()
    rating = data.get("rating")
    for m in library:
        if m.get_title().lower() == title.lower():
            m.set_rating(rating)
            return jsonify({
                "message": f"Rating for '{m.get_title()}' set to {rating}",
                "title": m.get_title(),
                "creator": m.get_creator(),
                "rating": m.get_rating()
            }), 200

    return jsonify({"error": f"Media '{title}' not found"}), 404


@app.route('/media/<title>', methods=['DELETE'])
def delete_media(title):
    for m in list(library):
        if m.get_title().lower() == title.lower():
            library.remove_media(m)
            return jsonify({"message": f"Media '{m.get_title()}' deleted successfully."}), 200
    return jsonify({"error": f"Media '{title}' not found."}), 404


if __name__ == '__main__':
    app.run(debug=True)
