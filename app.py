from flask import Flask,render_template,request,send_file
from PIL import Image,ImageDraw,ImageFont
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-image', methods=['POST'])
def generate_image():
    data = request.json
    text = data['text']

    img = Image.new('RGB', (300, 50), color = (255, 255, 255))
    d = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    d.text((10,10), text, fill=(0,0,0), font=font)

    img_io = io.BytesIO()
    img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)
