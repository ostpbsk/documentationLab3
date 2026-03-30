from flask import Blueprint, render_template, request, redirect, url_for
from bll.event_service import EventService

bp = Blueprint("main", __name__)

service = EventService()


@bp.route("/")
def index():
    events = service.get_all()
    return render_template("index.html", events=events)


@bp.route("/add", methods=["GET", "POST"])
def add_event():
    if request.method == "POST":
        service.add(request.form["title"], request.form["genre"])
        return redirect(url_for("main.index"))

    return render_template("add.html")


@bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_event(id):
    event = service.get_by_id(id)

    if request.method == "POST":
        service.update(id, request.form["title"], request.form["genre"])
        return redirect(url_for("main.index"))

    return render_template("edit.html", event=event)


@bp.route("/delete/<int:id>")
def delete_event(id):
    service.delete(id)
    return redirect(url_for("main.index"))