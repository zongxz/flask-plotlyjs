from flask import Flask, render_template, jsonify
from flask_cors import CORS
from backend.Visulize import VisualizeMouseBrainExpress
from backend.Visulize import VisualizeDNMsOnRegulatoryElement, VisualizeGtexGeneExpress, Transcript_DNMs_visualization, \
    VisualizeHumanEPCExpress, VisualizeProteinExpress, VisualizeBrainSpanExpress, VisualizeProteinProteinNetwork, a, b, d
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return render_template('tt.html')


@app.route('/humanEPCExpressData')
def humanEPCExpressData():
    data = VisualizeHumanEPCExpress.getHumanEPCExpressData()
    return jsonify(data)


@app.route('/VisualizeHumanEPCExpress')
def humanEPCExpress():
    return render_template('HumanEPCExpressPlot.html')


@app.route('/brainSpanData')
def brainSpanData():
    data = VisualizeBrainSpanExpress.getBrainSpanData()
    return jsonify(data)


@app.route('/brainSpanExpress')
def brainSpanExpress():
    return render_template('BrainSpanExpressPlot.html')

@app.route('/brainSeqData')
def brainSeqData():
    data = b.a
    return jsonify(data)

@app.route('/gtexGeneExpressData')
def gtexGeneExpressData():
    data = VisualizeGtexGeneExpress.getGexGeneExpressData()
    return jsonify(data)


@app.route('/VisualizeGtexGeneExpress')
def gtexGeneExpress():
    return render_template('GtexGeneExpressPlot.html')


@app.route('/mouseBrainExpressData1')
def mouseBrainExpressData1():
    # data = VisualizeMouseBrainExpress.getMouseBrainExpressData()
    data = a.a
    return jsonify(data)

@app.route('/mouseBrainExpressData')
def mouseBrainExpressData():
    # data = VisualizeMouseBrainExpress.getMouseBrainExpressData()
    data = a.b
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

@app.route('/Transcript_DNMsData1')
def transcript_DNMsData1():
    data = b.a
    return jsonify(data)

@app.route('/Transcript_DNMs')
def transcript_DNMs():
    return render_template('Transcript_DNMsPlot.html')


@app.route('/DNMsOnRegulatoryData')
def DNMsOnRegulatoryData():
    data = VisualizeDNMsOnRegulatoryElement.getDNMsOnRegulatoryData()
    return jsonify(data)

@app.route('/DNMsOnRegulatoryData1')
def DNMsOnRegulatoryData1():
    # data = VisualizeDNMsOnRegulatoryElement.getDNMsOnRegulatoryData()
    data = d.a
    print(data)
    return jsonify(data)

@app.route('/DNMsOnRegulatory')
def DNMsOnRegulatory():
    return render_template('DNMsOnRegulatoryPlot.html')


@app.route('/GeneDetailPPI')
def GeneDetailPPI():
    ppi = VisualizeProteinProteinNetwork.Main()
    nodes_edges = ppi.run('7468')
    return render_template('GeneDetail_PPI.html', nodes_edges=nodes_edges, id=7468)


if __name__ == '__main__':
    app.run()
