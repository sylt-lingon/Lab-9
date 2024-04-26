from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask('Portfolio')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Project(db.Model):
    title = db.Column(db.String(300), primary_key=True)
    link = db.Column(db.String(300))

    def __repr__(self):
        return f'Project{self.title}, {self.link}'


@app.route('/')
def main():
    projects = Project.query.all()
    return render_template('index.html', projects_list=projects)


@app.route('/add', methods=['POST'])
def add_project():
    data = request.json
    project = Project(**data)
    db.session.add(project)
    db.session.commit()
    return 'OK'


@app.route('/clear')
def clear():
    db.session.query(Project).delete()
    db.session.commit()
    return '', 204


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
