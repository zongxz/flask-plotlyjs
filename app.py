from flask import Flask, render_template, jsonify
from Visulize import VisualizeHumanEPCExpress, VisualizeGtexGeneExpress, VisualizeMouseBrainExpress,\
    VisualizeProteinExpress, Transcript_DNMs_visualization, VisualizeDNMsOnRegulatoryElement

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello!!'


@app.route('/humanEPCExpressData')
def humanEPCExpressData():
    data = VisualizeHumanEPCExpress.getHumanEPCExpressData()
    return jsonify(data)


@app.route('/VisualizeHumanEPCExpress')
def humanEPCExpress():
    return render_template('HumanEPCExpressPlot.html')


@app.route('/gtexGeneExpressData')
def gtexGeneExpressData():
    data = VisualizeGtexGeneExpress.getGexGeneExpressData()
    return jsonify(data)


@app.route('/VisualizeGtexGeneExpress')
def gtexGeneExpress():
    return render_template('GtexGeneExpressPlot.html')


@app.route('/mouseBrainExpressData')
def mouseBrainExpressData():
    data = VisualizeMouseBrainExpress.getMouseBrainExpressData()
    return jsonify(data)


@app.route('/VisualizeMouseBrainExpress')
def mouseBrainExpress():
    return render_template('MouseBrainExpressPlot.html')


@app.route('/proteinExpressData')
def proteinExpressData():
    data = VisualizeProteinExpress.getProteinExpressData()
    return jsonify(data)


@app.route('/VisualizeProteinExpress')
def proteinExpress():
    return render_template('ProteinExpressPlot.html')


@app.route('/Transcript_DNMsData')
def transcript_DNMsData():
    data = Transcript_DNMs_visualization.getTranscript_DNMsData()
    return jsonify(data)


@app.route('/Transcript_DNMs')
def transcript_DNMs():
    return render_template('Transcript_DNMsPlot.html')


@app.route('/DNMsOnRegulatoryData')
def DNMsOnRegulatoryData():
    data = VisualizeDNMsOnRegulatoryElement.getDNMsOnRegulatoryData()
    return jsonify(data)


@app.route('/DNMsOnRegulatory')
def DNMsOnRegulatory():
    return render_template('DNMsOnRegulatoryPlot.html')


if __name__ == '__main__':
    app.run()
