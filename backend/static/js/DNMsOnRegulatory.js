function get_promoter_color(text) {
    var s = text.split(',');
    var len = s.length;
    s = s[len - 1];
    var color;
    if (s === 'permissive') {
        color = 'rgb(234,255,0)';
    } else {
        color = 'rgb(255,165,0)';
    }
    return color;
}

function get_enhancer_color(text) {
    var s = text.split(',');
    var len = s.length;
    s = s[len - 1].trim();
    var color;
    if (s === 'targetgene') {
        color = 'rgb(0,100,0)';
    } else {
        color = 'rgb(144,238,144)';
    }
    return color;
}

function get_DNM_color(m_type) {
    var color;
    if ((['frameshift deletion', 'frameshift insertion', 'frameshift substitution',
        'splice-site mutation', 'stopgain'].includes(m_type)) || m_type.startsWith('frameshift')) {
        color = 'red';
    } else if ((['nonframeshift deletion', 'nonframeshift insertion', 'nonsynonymous snv',
        'nonframeshift substitution', 'nonsynonymous SNV', 'strat gain', 'start gain',
        'stoploss'].includes(m_type)) || m_type.startsWith('nonframeshift')) {
        color = 'pink';
    } else if (['synonymous SNV', 'exonic', 'coding complex', 'synonymous snv'].includes(m_type)) {
        color = 'purple';
    } else if (['unknown'].includes(m_type)) {
        color = 'yellow';
    } else {
        color = 'blue';
    }
    return color;
}

function get_heights(length) {
    if (length <= 2) {
        return 200;
    } else if (length <= 4) {
        return 400;
    } else if (length <= 10) {
        return 600;
    } else if (length <= 13) {
        return 800;
    } else {
        return length * 30;
    }
}

function getData() {

    $.ajax({
        url: "http://127.0.0.1:5000/DNMsOnRegulatoryData",
        type: "GET",
        dataType: "json",
        data: {},
        success: function (data) {
            var exton_plot_data = data[0];
            var utr_plot_data = data[1];
            var promoter_plot_data = data[2];
            var enhancer_plot_data = data[3];
            var dnm_plot_data = data[4];
            var trans_count = data[5];
            var trace = [];
            for (let i = 0; i < exton_plot_data.length; i++) {
                var item = exton_plot_data[i];
                var trace_item = {
                    type: 'scatter',
                    visible: true,
                    hoverinfo: 'text',
                    hoverlabel: {
                        'font': {
                            'size': 10
                        }
                    },
                    showlegend: false,
                    mode: 'lines',
                    x: [item[0][0], item[1][0]],
                    y: [item[0][1], item[1][1]],
                    text: String(item[0][2]) + '-' + String(item[1][2]),
                    line: {
                        color: 'rgb(72,130,180)',
                        shape: 'linear',
                        width: 10,
                        simplify: true
                    }
                };
                trace.push(trace_item);
            }
            for (let i = 0; i < utr_plot_data.length; i++) {
                var item = utr_plot_data[i];
                var trace_item = {
                    type: 'scatter',
                    visible: true,
                    hoverinfo: 'text',
                    hoverlabel: {
                        'font': {
                            'size': 10
                        }
                    },
                    showlegend: false,
                    mode: 'lines',
                    x: [item[0][0], item[1][0]],
                    y: [item[0][1], item[1][1]],
                    text: String(item[0][2]) + '-' + String(item[1][2]),
                    line: {
                        color: 'gray',
                        shape: 'linear',
                        width: 5,
                    }
                };

                trace.push(trace_item);
            }
            if (promoter_plot_data.length !== 0) {
                for (let i = 0; i < promoter_plot_data.length; i++) {
                    var item = promoter_plot_data[i];
                    var trace_item = {
                        type: 'scatter',
                        visible: true,
                        hoverinfo: 'text',
                        hoverlabel: {
                            'font': {
                                'size': 10
                            }
                        },
                        showlegend: false,
                        mode: 'lines',
                        x: [item[0][0], item[1][0]],
                        y: [item[0][1], item[1][1]],
                        text: String(item[0][2]),
                        line: {
                            color: get_promoter_color(String(item[0][2])),
                            shape: 'linear',
                            width: 10,
                            simplify: true
                        }
                    };
                    trace.push(trace_item);
                }
            }
            if (enhancer_plot_data.length !== 0) {
                for (let i = 0; i < enhancer_plot_data.length; i++) {
                    var item = enhancer_plot_data[i];
                    var trace_item = {
                        type: 'scatter',
                        visible: true,
                        hoverinfo: 'text',
                        hoverlabel: {
                            'font': {
                                'size': 10
                            }
                        },
                        showlegend: false,
                        mode: 'lines',
                        x: [item[0][0], item[1][0]],
                        y: [item[0][1], item[1][1]],
                        text: String(item[0][2]),
                        line: {
                            color: get_enhancer_color(String(item[0][2])),
                            shape: 'linear',
                            width: 10,
                            simplify: true
                        }
                    };
                    trace.push(trace_item);
                }
            }
            for (let i = 0; i < dnm_plot_data.length; i++) {
                var item = dnm_plot_data[i];
                var type = item[0][2].split(',')[2];
                var c = get_DNM_color(type);
                var trace_item = {
                    type: 'scatter',
                    visible: true,
                    hoverinfo: 'text',
                    hoverlabel: {
                        'font': {
                            'size': 10
                        }
                    },
                    showlegend: false,
                    mode: 'lines',
                    x: [item[0][0], item[1][0]],
                    y: [item[0][1], item[1][1]],
                    text: String(item[0][2]),
                    line: {
                        color: c,
                        shape: 'linear',
                        width: 10,
                        simplify: true
                    }
                };

                trace.push(trace_item);
            }
            var layout = {
                paper_bgcolor: 'rgb(249, 249, 249)',
                plot_bgcolor: 'rgb(249, 249, 249)',
                width: 800,
                height: get_heights(trans_count),
                hovermode: "closest",
                spikedistance: 0,
                hoverdistance: 2,
                xaxis: {
                    showgrid: false,
                    zeroline: false,
                    showline: false,
                    showticklabels: false,
                    autorange: true,
                    dtick: 100
                },
                yaxis: {
                    titlefont: {
                        family: 'Arial, sans-serif',
                        size: 18,
                        color: 'lightgrey'
                    },
                    showticklabels: true,
                    tickangle: 360,
                    tickfont: {
                        family: 'Arial, serif',
                        size: 10,
                        color: 'black'

                    },
                    exponentformat: 'e',
                    showexponent: 'ALL',
                },
                margin: {
                    l: 110,
                    r: 5,
                    t: 10,
                    pad: 0
                },
                // showlegend: false
            }
            Plotly.plot('DNMsOnRegulatory_box', trace, layout)
        },
        error: function (err) {
            console.log("错误！");
        }
    });

}

getData();