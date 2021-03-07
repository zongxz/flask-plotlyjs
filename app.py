from flask import Flask, render_template, jsonify
from Visulize import VisualizeHumanEPCExpress, VisualizeGtexGeneExpress, VisualizeMouseBrainExpress, a
from Visulize import VisualizeProteinExpress
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello!'


@app.route('/humanEPCExpressData')
def humanEPCExpressData():
    data = VisualizeHumanEPCExpress.main()
    return jsonify(data)


@app.route('/VisualizeHumanEPCExpress')
def humanEPCExpress():
    return render_template('HumanEPCExpressPlot.html')


@app.route('/gtexGeneExpressData')
def gtexGeneExpressData():
    data = VisualizeGtexGeneExpress.main()
    return jsonify(data)


@app.route('/VisualizeGtexGeneExpress')
def gtexGeneExpress():
    return render_template('GtexGeneExpressPlot.html')


@app.route('/mouseBrainExpressData')
def mouseBrainExpressData():
    data = VisualizeMouseBrainExpress.main()
    return jsonify(data)


@app.route('/VisualizeMouseBrainExpress')
def mouseBrainExpress():
    return render_template('MouseBrainExpressPlot.html')


@app.route('/proteinExpressData')
def proteinExpressData():
    data = a.a
    return jsonify(data)


@app.route('/VisualizeProteinExpress')
def proteinExpress():
    data = VisualizeProteinExpress.ProteinExpressPlot.plot(a.a)
    print(data)
    return render_template('t.html', data=data[0], layout=data[1])

if __name__ == '__main__':
    app.run()
