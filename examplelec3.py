from flask import Flask, request, render_template, url_for

app = Flask(__name__)

@app.route('/oranges')
def lemons():

    title_var = "My Ice Cream Form"
    options = ["Chocolate", "Vanilla", "Superman", "Pistachio", "Anything I Want!"]
    # Add code -- what type should options hold?
    return render_template('seeform.html',title=title_var, lst_stuff=options)

@app.route('/apples')
def plants():
    ## Add code here
    ## FIX THIS
    

    flavor_options = request.args #.get("flavor")
    #flavor_options = result.items()
    
    name = request.args.get("name", "None")
    name_len = len(name)

    return render_template('results.html',flavors=flavor_options, name_len=name_len, name=name)


if __name__ == "__main__":
    app.run(use_reloader=True,debug=True)
