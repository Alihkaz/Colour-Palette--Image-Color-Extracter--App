#
from flask import Flask,  render_template, redirect, url_for, request 
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from forms import CreateProductForm
import os
from werkzeug.utils import secure_filename
from extracting_colors import ColorResult


colorresult=ColorResult()
image_path=None

   

    
        
      



app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
ckeditor = CKEditor(app)
Bootstrap5(app)




#---------------------------------------------------------------------------------------------------------#

# CONNECT TO DB
UPLOAD_PATH='static/uploads'
app.config['UPLOAD_PATH']=UPLOAD_PATH



#-----------------------------------------------Main Page-----------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------#



@app.route('/')
def home():
    return render_template("main.html",)
 


#------------------------------------------The page that shows the result of extraction-----------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------#

@app.route("/color_result", methods=["GET", "POST"])
def color_result():
    top_10_colors=colorresult.top_10_colors
    proportions=colorresult.proportions
    return render_template("color_result.html",
                           top_10_colors=top_10_colors,
                           proportions=proportions,
                           image_path=image_path)




#------------------------------------------The page that extracts the color from the image-----------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------#




@app.route("/new-image", methods=["GET", "POST"])
def add_new_image():
    form = CreateProductForm()
    colorresult.rgb_colors=[]
    colorresult.proportions=[]
    colorresult.hex_colors=[]
    colorresult.top_10_colors=[]

    if form.validate_on_submit():

       
        uploaded_image = form.image.data
        print(uploaded_image)

        filename = secure_filename(uploaded_image.filename)
        global image_path
        image_path = os.path.join(UPLOAD_PATH, filename)

        uploaded_image.save(image_path)

        colorresult.exract_colors(image_path)
       
        
        return redirect(url_for("color_result",image_path=image_path))
    


    return render_template("extract_color.html", form=form)

     
#-----------------------------------------------------------------------------------------------#

if __name__ == "__main__":
    app.run(debug=False, port=5001)
