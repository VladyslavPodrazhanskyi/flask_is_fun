from app import create_app, db

if __name__ == '__main__':
    flask_app = create_app('dev')
    # Use  app_context() in a
    # with block, and everything that runs in the block
    # will have access to current_app.
    with flask_app.app_context():
        db.create_all()
    flask_app.run()
