from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "rumbacaramba7890"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def home():
    """Home page. List all pets."""

    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """Show add_pet form and handle add"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        if photo_url == '':
            photo_url = 'https://image.freepik.com/free-vector/pet-shop-veterinary-sign-silhouette-dog-cat-bunny_24877-11357.jpg'
        
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        flash(f"Added {name}")
        return redirect("/")
    else:
        return render_template('add_pet.html', form=form)


@app.route('/<int:pet_id>', methods=["GET", "POST"])
def show_edit_pet_details(pet_id):
    """Show pet details"""

    pet = Pet.query.get_or_404(pet_id)
    form = AddPetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        if pet.photo_url == '':
            pet.photo_url = 'https://image.freepik.com/free-vector/pet-shop-veterinary-sign-silhouette-dog-cat-bunny_24877-11357.jpg'
        pet.age = form.age.data
        pet.notes = form.notes.data

        db.session.commit()
        flash(f"Saved changes for {pet.name}")
        return redirect(f"/{pet_id}")
    else:
        return render_template('pet_details.html', pet=pet, form=form)
