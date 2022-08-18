from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from BGRemoval import *

app = Flask(__name__)

dir_path =  os.path.join('temp/')
#img_path = dir_path + "temp.jpg"
img_path = os.path.join('static', 'people_photo', 'temp')
PEOPLE_FOLDER = os.path.join('static', 'people_photo')
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

@app.route('/')
def upload_file():
   return render_template('upload.html')
	
'''
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_files():
   if request.method == 'POST':
      f = request.files['file']
      # f.save(secure_filename(f.filename))
      f.save(img_path)
      
      return render_template('uploader.html')
'''

@app.route('/start', methods=['GET', 'POST'])
def start():
    before = os.path.join(app.config['UPLOAD_FOLDER'], 'temp.jpg')
    if request.method == 'POST':
        f = request.files['file']
        # f.save(secure_filename(f.filename))
        f.save(before)
    
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'image.jpg')
    
    BG = BGRemove()
    #image_path = 'temp/temp.jpg' # 'images/1.jpg'
    rgb = (255.0,0.0,0.0)
    img = cv2.imread(before)
    output = BG.inference(img,rgb)
    cv2.imwrite(full_filename,output)
    print("done")
    return render_template('output.html',user_image =full_filename, before=before)


if __name__ == "__main__":
    app.run()
