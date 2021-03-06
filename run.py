import os
from flask import Flask, jsonify, request,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, 
            static_folder='build', 
            static_url_path='')

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'

db = SQLAlchemy(app)

db.init_app(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    rating = db.Column(db.Integer)


@app.route('/add_movie',methods=['POST'])
def add_movie():
    
    movie_data = request.get_json()

    new_movie = Movie(title=movie_data['title'], rating=movie_data['rating'])

    db.session.add(new_movie)
    db.session.commit()


    return 'Done', 201

@app.route('/movies')
def movies():
    movies_list = Movie.query.all()
    movies = []

    for movie in movies_list:
        movies.append({'title': movie.title,'rating': movie.rating})

    return jsonify({'movies':movies})

@app.route('/',methods=["GET"])
def index():
    return app.send_static_file('index.html')




if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, port=os.environ.get('PORT', 80))    
    #app.run(debug=True)