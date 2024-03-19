from flask import Flask, render_template, request
from app2 import create_math_image
import base64
from io import BytesIO

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    image_data = None
    if request.method == 'POST':
        latex_str = request.form['latex_input']
        latex_str = latex_str.replace("&lt;", "<").replace("&gt;", ">")
        image = create_math_image(latex_str)
        img_io = BytesIO()
        image.save(img_io, 'PNG')
        img_io.seek(0)
        image_data = base64.b64encode(img_io.read()).decode('utf8')
    return render_template('index.html', image_data=image_data)

if __name__ == '__main__':
    app.run(debug=True)



#\int_0^1 x^2 dx
#e^{i\pi} + 1 = 0
