from app import app, db
from flask import render_template, flash, redirect, url_for, request, jsonify
from app.forms import LoginForm, SignupForm
from app.models import User, Note
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, logout_user, login_required, current_user


@app.route("/")

@app.route("/index", methods=["GET", "POST"])
@login_required
def index():
    notes = Note.query.filter_by(user_id=current_user.id).all()

    return render_template("index.html", title="Home", notes=notes)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password_hashed, form.password.data):
            login_user(user)
            flash("user has successfully logged in!")
            return redirect(url_for("index"))
        else:
            flash("incorrect credentials or user doesn't exist")
            return redirect(url_for("login"))

    return render_template("login.html", title="Login", form=form)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    sform = SignupForm()

    if sform.validate_on_submit():
        user = User.query.filter_by(username=sform.username.data).first()

        if user:
            flash("user already exists")
            return redirect(url_for("login"))
        else:
            hashed_password = generate_password_hash(sform.password.data)
            new_user = User(username=sform.username.data, password_hashed=hashed_password, password=sform.password.data)
            db.session.add(new_user)
            db.session.commit()
            flash("user added to the database")
            return redirect(url_for("login"))
        
    return render_template("signup.html", title="Signup", sform=sform)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("user logged out")
    return redirect(url_for("login"))

@app.route("/add_note", methods=["GET", "POST"])
@login_required
def add_note():
    data = request.get_json()
    note = Note(body=data["body"], column=data["column"], user_id=current_user.id)
    db.session.add(note)
    db.session.commit()
    print("note added")

    return jsonify({
        "id": note.id,
        "body": note.body,
        "column": note.column
    })


@app.route("/update_note", methods=["GET", "POST"])
@login_required
def update_note():
    data = request.get_json()
    note = Note.query.get(data["id"])

    if note and note.user_id == current_user.id:
        note.body = data["body"]
        db.session.commit()
        print(f"note updated: {data["body"]}")

        return jsonify({"status": "success"})
    return jsonify({"status": "error"}), 403

@app.route("/update_column", methods=["GET", "POST"])
@login_required
def update_column():
    data = request.get_json()
    note = Note.query.get(data["id"])

    if note and note.user_id == current_user.id:
        note.column = data["column"]
        db.session.commit()
        print("column moved")

        return jsonify({"status": "success"})
    return jsonify({"status": "error"}), 403


@app.route("/delete_note", methods=["GET", "POST"])
@login_required
def delete_note():
    data = request.get_json()
    note = Note.query.get(data["id"])

    if note and note.user_id == current_user.id:
        db.session.delete(note)
        db.session.commit()
        return jsonify({"status": "success"})
    return jsonify({"status": "error"}), 403
