import hashlib
import os
import pickle
import pprint
import re
import subprocess
from flask import Blueprint, flash, redirect, render_template, request, url_for

# from flask import session, g
from todo_db import get_db, Post
from dateutil import parser

bp = Blueprint("todo", __name__)


def radio_file_parse(update_dict=True):
    """this script pulls down the radio quiz document and parses the list of
    questions"""
    md5 = hashlib.md5()

    subprocess.call(
        [
            "wget",
            "http://www.ncvec.org/downloads/2016%20ExtraClassPool2nd" "%20Errata.doc",
        ]
    )

    if os.path.exists("/home/ihclark/radio/radioquestions.doc"):
        subprocess.call(["rm", "/home/ihclark/radio/radioquestions.doc"])
    if os.path.exists("/home/ihclark/radio/output"):
        subprocess.call(["rm", "/home/ihclark/radio/output"])

    subprocess.call(["touch", "/home/ihclark/radio/radioquestions.doc"])
    subprocess.call(["touch", "/home/ihclark/radio/output"])

    subprocess.call(
        [
            "mv",
            "/home/ihclark/radio/2016 ExtraClassPool2nd Errata.doc",
            "/home/ihclark/radio/radioquestions.doc",
        ]
    )

    radiofile = open("radioquestions.doc", "rbU")

    md5.update(radiofile.read())

    radio_file_digest = md5.hexdigest()

    if os.path.exists("/home/ihclark/radio/md5hash"):
        md5hash = open("md5hash", "r")
        old_hash = md5hash.read()
        if old_hash == radio_file_digest:
            update_dict = False
            print "the hashes match! our work here is done"
        else:
            print "the matches don't match! time to update"
    else:
        md5hash = open("md5hash", "w")
        md5hash.write(radio_file_digest)
        print "no hash! time to update"
    radiofile.seek(0)
    output_file = open("output", "w")
    ppoutput = open("ppoutput", "w")
    test_dict = {}
    ques_reg_ex = re.compile(r"\w\d\w\d\d\s.\w.")

    while update_dict:
        line = radiofile.readline()
        search = ques_reg_ex.search(line)
        if search:
            question_number = line[0:5]
            correct_answer = line[7]

            # range was 5
            question_text = radiofile.readline()
            answer_a = radiofile.readline()
            answer_b = radiofile.readline()
            answer_c = radiofile.readline()
            answer_d = radiofile.readline()

            # add info to dictionary
            test_dict[question_number] = (
                question_text,
                answer_a,
                answer_b,
                answer_c,
                answer_d,
                correct_answer,
            )
        if not line:
            break

    pickle.dump(test_dict, output_file, 2)
    pprint.pformat(test_dict)

    ppoutput.write("test_dict = " + pprint.pformat(test_dict))
    ppoutput.close()


def radio_input_output(output):
    """test the output independent of it being Pprinted"""
    test_dict = pickle.load(output)

    for key in test_dict.keys():
        print key
        print test_dict[key]


@bp.route("/todo", methods=("GET", "POST"))
def todo():
    db = get_db()

    return render_template("todo/index.html", items=db.query(Post).order_by(Post.date))


@bp.route("/todo/create", methods=("GET", "POST"))
def create():
    # post method means that form is submitted
    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        author = request.form["author"]
        date = request.form["date"]
        error = None

        if not title:
            error = "todo item needs a title"

        if not author:
            author = "Anonymous"

        try:
            date_object = parser.parse(date)
        except ValueError:
            error = "bad date"

        if error is not None:
            flash(error)

        else:
            db = get_db()

            new_post = Post(body=body, date=date_object, author=author, title=title)
            db.add(new_post)

            db.commit()
            db.close()

        return redirect(url_for("todo.todo"))

    return render_template("todo/create.html")


# tinydb is not going to suffice for deleting a post by id, need to implement
#  a relational DB, SQLlite for now
@bp.route("/todo/delete/<int:post_id>", methods=("GET", "POST"))
def delete(post_id):
    if request.method == "POST":
        accept = request.form["accept"]
        error = None
        print post_id

        if accept != "on":
            flash("please select yes to delete post or hit back to go back")

        else:
            db = get_db()

            frank = db.query(Post).filter_by(id=post_id).first()
            print "here is frank"
            print frank
            db.delete(frank)
            # not sure if the lines underneath are needed, to remvoe later
            db.commit()
            db.close()

        return redirect(url_for("todo.todo"))

    return render_template("todo/delete.html")
