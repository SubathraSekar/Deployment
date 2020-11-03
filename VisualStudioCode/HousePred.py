from flask import Flask, request, render_template
import joblib

app = Flask(__name__)
model=joblib.load('HousePrediction.pkl')

@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/pricePrediction',methods = ['POST'])
def result():
    
    if request.method == 'POST':
        construction  = request.form["construction"]
        construction = int(construction)
        rera  = request.form["rera"]
        rera = int(rera)
        bhk  = request.form["bhk_no"]
        bhk = int(bhk)
        sq_ft  = request.form["sq_ft"]
        sq_ft = float(sq_ft)
        move  = request.form["move"]
        move = int(move)
        resale  = request.form["resale"]
        resale = int(resale)
        longt  = request.form["longt"]
        longt = float(longt)
        lat  = request.form["lat"]
        lat = float(lat)
        final=list()
        final.append(construction)
        final.append(rera)
        final.append(bhk)
        final.append(sq_ft)
        final.append(move)
        final.append(resale)
        final.append(longt)
        final.append(lat)
        price = model.predict([final])
    return render_template('index.html',
                        predicted_price="Price = {}".format(float(price)))
if __name__ == "__main__":
    app.run()                     
