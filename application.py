from flask import Flask, render_template, request
import pickle


application = Flask(__name__)


@application.route('/', methods=['GET'])
def homepage():
    return render_template('index.html')


@application.route('/predict', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            crim = float(request.form['crim'])
            zn = float(request.form['zn'])
            indus = float(request.form['indus'])
            chas = float(request.form['chas'])
            nox = float(request.form['nox'])
            rm = float(request.form['rm'])
            age = float(request.form['age'])
            dis = float(request.form['dis'])
            rad = float(request.form['rad'])
            tax = float(request.form['tax'])
            ptratio = float(request.form['ptratio'])
            black = float(request.form['black'])
            lstat = float(request.form['lstat'])

            model_filename = 'boston_price_prediction-source.pickle'
            model = pickle.load(open(model_filename, 'rb'))

            prediction = model.predict([[crim,zn,indus,chas,nox,rm,age,dis,rad,tax,ptratio,black,lstat]])

            return render_template('results.html', prediction=prediction)
        except Exception:
            return render_template("Something went wrong")
    else:
        return render_template('index.html')


if __name__ == "__main__":
    application.run()
