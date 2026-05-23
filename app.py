from flask import Flask, render_template, request, send_file
import os
from style_transfer import apply_style

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stylize', methods=['POST'])
def stylize():
    content = request.files['content']
    style = request.files['style']
    
    content_path = os.path.join(UPLOAD_FOLDER, 'content.jpg')
    style_path = os.path.join(UPLOAD_FOLDER, 'style.jpg')
    output_path = os.path.join(UPLOAD_FOLDER, 'stylized.jpg')

    content.save(content_path)
    style.save(style_path)

    apply_style(content_path, style_path, output_path)

    return send_file(output_path, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)
