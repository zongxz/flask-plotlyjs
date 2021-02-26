from flask import Flask, render_template
import plotly.graph_objects as go
import plotly
import json
from Visulize import VisualizeHumanEPCExpress, VisualizeGtexGeneExpress
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/VisualizeHumanEPCExpress')
def humanEPCExpress():
    res = VisualizeHumanEPCExpress.main()
    print(type(res))
    msgJson = json.dumps(res, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('HumanEPCExpressPlot.html', msg=msgJson)\


@app.route('/VisualizeGtexGeneExpress')
def gtexGeneExpress():
    res = VisualizeGtexGeneExpress.main()
    print(type(res))
    msgJson = json.dumps(res, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('GtexGeneExpressPlot.html', msg=msgJson)


if __name__ == '__main__':
    app.run()
