
from flask import Flask, request, jsonify, render_template
from models import db, connect_db, Cupcake

"""Flask app for Cupcakes"""

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.config['SECRET_KEY'] = 'uuggtthhkk'


connect_db(app)
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("home_page.html")

@app.route("/api/cupcakes")
def list_cupcakes():
    all_cupcakes =[cupcake.serialize() for cupcake in Cupcake.query.all()]
    
    return jsonify(cupcakes=all_cupcakes)

@app.route("/api/cupcakes/<cupcake_id>")
def get_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)

    return jsonify(cupcake=cupcake.serialize())

@app.route("/api/cupcakes", methods=["POST"])
def create_cupcakes():

    new_cupcake = Cupcake(
        flavor = request.json.get('flavor'),
        size = request.json.get('size'),
        rating = request.json.get('rating'),
        image = request.json.get('image')
    )

    db.session.add(new_cupcake)
    db.session.commit()
    
    json_resp = jsonify(cupcake=new_cupcake.serialize())
    
    return (json_resp, 201)


@app.route("/api/cupcakes/<cupcake_id>", methods=["PATCH"])
def update_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)
    db.session.commit()
    return jsonify(cupcake=cupcake.serialize())

@app.route("/api/cupcakes/<cupcake_id>", methods=["DELETE"])
def delete_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message= "deleted")
