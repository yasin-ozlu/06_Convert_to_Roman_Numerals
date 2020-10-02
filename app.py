from flask import Flask, render_template, request

app = Flask(__name__)

def convert_to_roman(decimal_num):
    roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    num_to_roman = ""
    for i,d in enumerate(num):
        while (decimal_num >= d):
            decimal_num -= d
            num_to_roman += roman[i]
    return num_to_roman
#print(convert_to_roman(3285))

@app.route('/', methods=['GET'])
def main_get():
    return render_template('index.html', developer_name='Yasin', not_valid=False)

@app.route('/', methods=['POST'])
def main_post():
    alpha = request.form['number']       #alpha=form.get.number
    if not alpha.isdecimal():
        return render_template('index.html', developer_name='Yasin', not_valid=True)

    number = int(alpha)
    if not 0 < number < 4000:
        return render_template('index.html', developer_name='Yasin', not_valid=True)

    return render_template('result.html', number_decimal = number, number_roman = convert_to_roman(number), developer_name='Yasin')

if __name__=="__main__":
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=80)