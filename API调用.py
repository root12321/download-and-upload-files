from flask import Flask
from flask import render_template
from flask import request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/upload',methods=['POST'])
def upload():
    file=request.files.get('file')
    filename=file.filename
    file.save('D:\新建文件夹\static\%s'%filename)
    return 'static/%s' % filename
if __name__=='__main__':
    app.run(debug=True)
