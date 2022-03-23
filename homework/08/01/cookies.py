import random
from flask import Flask
from flask import make_response
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/slot-machine")
def slot_machine():
    values = [random.randint(1, 3), random.randint(1, 3), random.randint(1, 3)]
    money = request.cookies.get('money') #haetaan money niminen cookie
    text = ""
    images = ""
    restart = "Play" #play painike html-sivulla, vakiona play, kun rahat loppuu muutetaan restartiksi

    #jos money cookieita ei vielä ole niin asettaa sen valuen 20
    if money == None:
        money = 20
    else: #muuten katsoo normaalisti tuliko rahaa vai ei ja vähentää/lisää sen money muuttujaan
        if values[0] == values[1] == values[2]:
            text = "You won 5€!"
            money = int(money) + 5
        else:
            money = int(money) -1
            text= " You lost."

    #jos raha on 0, niin poistaa cookiet ja vaihtaa play napin restartiksi
    if money == 0:
        text = "You are broke, restart"
        restart = "Restart"
        response = make_response(render_template("index.html", money=money, images=images, text=text, restart=restart))
        response.delete_cookie("money")
        return response

    #ilmoittaa mitkä kuvat menevät serverille vaihtamalla nimi pathiin
    #jostain syystä render_templaten kanssa en saanut kuvia tulemaan http-sivulle, vaikka numerot muuttuvat normaalisti
    #kun painaa GET nappia test.http:stä, niin ilmoittaa tuon <img...> oudossa muodossa. Mistä tod.näk johtuu, ettei kuvat näy.
    for number in values:
        images += f"<img src='/static/{number}.png' width='200' height='200'>"

    #Set cookie
    response = make_response(render_template("index.html", money=money, images=images, text=text, restart=restart))
    response.set_cookie("money", f"{money}")
    return response


if __name__ == "__main__":
    app.run(debug=True)