from flask import Flask,request,send_file,make_response,jsonify,render_template
from DeepImageSearch import Load_Data,Search_Setup
import requests
import base64
from io import BytesIO
from PIL import Image
# image_list = Load_Data().from_folder(['./images'])
# st = Search_Setup(image_list=image_list,model_name='resnet50',pretrained=True,image_count=100)
# st.run_index()
# metadata = st.get_image_metadata_file()
# st.add_images_to_index(image_list[1001:1010])
ans={'1': '0c3d04bcf5.jpg',
 '2': '0cfaf08fce.jpg',
 '3': '0d0d6d90d8.jpg',
 '4': '1a2dce7848.jpg'}

app=Flask(__name__)
@app.route("/image",methods=["GET","POST"])
def download_og():
    if request.method=="POST":
        if 'image' not in request.files:
            return jsonify({'error': 'No image found in request'})

    image = request.files['image']
    path="uploads/"+image.filename
    image.save(path)
    # ans=st.get_similar_images(image_path=path,number_of_images=10)
    out_=[]
    for i in list(ans.values()):
        with Image.open(i) as img:
            buffered = BytesIO()
            img.save(buffered, format="JPEG")
            img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
            out_.append('data:image/jpeg;base64,' + img_str)
    return render_template('display.html', images=out_)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
