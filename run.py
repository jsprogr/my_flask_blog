from src import create_app, db

app = create_app()



@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': 'User', 'Post': 'Post', 'Tag': 'Tag'}

        
if __name__ == '__main__':
    app.run()