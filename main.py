from movie_api import create_app

app = create_app()

print('hello')

if __name__ == '__main__':
    app.run(port=5000, debug=True)