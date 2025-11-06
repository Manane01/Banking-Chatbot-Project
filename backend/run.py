# Lancement de Flask API

from app import create_app, db

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all() # Créeles tables si elles n'existent pas encore
    app.run(debug=True)
