from flask import Flask, render_template


app=Flask(__name__)

@app.route("/")
def index():
    main_data={
        'a':"A",
        'b':"B",
        'c':"C"
    }
    return render_template ("index.html", main_data=main_data)

@app.route("/contacts/")
def contacts():
    developer_name= "Leo"
    # context={'name=developer_name'}
    # return render_template ("contacts.html", props=context)
    return render_template("contacts.html", name=developer_name, creation_date="24.07.2022")

if __name__ ==" _main_ ":
    app.run(debug=True)


