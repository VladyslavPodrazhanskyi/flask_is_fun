from app import create_app, db
from app.auth.models import User

if __name__ == '__main__':
    flask_app = create_app('dev')
    # Use  app_context() in a
    # with block, and everything that runs in the block
    # will have access to current_app.
    with flask_app.app_context():
        db.create_all()
        if not User.query.filter_by(name='Yaroslav').first():
            User.create_user('Yaroslav',
                             'yaric@gmail.com',
                             'top_secret')

    flask_app.run()
