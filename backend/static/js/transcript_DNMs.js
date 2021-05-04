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
        url: "http://127.0.0.1:5000/Transcript_DNMsData",
        type: "GET",
        dataType: "json",
        data: {},
        success: function (data) {
            var exton_records = data[0];
            var utr_records = data[1];
            var DNM_xy = data[2];
            var trans_len = data[3];
            var trace_coding = [];
            var exton_num = 0;
            for (let i = 0; i < exton_records.length; i++) {
                var item = exton_records[i];
                var trace_coding_item = {};
                if (i !== exton_records.length - 1) {
                    trace_coding_item = {
                        visible: true,
                        type: 'scatter',
                        hoverinfo: 'text',
                        showlegend: false,
                        mode: 'lines',
                        x: [item[0][0], item[1][0]],
                        y: [item[0][1], item[1][1]],
                        text: '[' + String(item[0][2]) + '-' + String(item[1][2]) + ']',
                        line: {
                            color: 'rgb(72,130,180)',
                            shape: 'linear',
                            width: 10,
                            simplify: true
                        }
                    };

                    trace_coding.push(trace_coding_item);
                    exton_num += 1;

                } else {
                    trace_coding_item = {
                        visible: true,
                        hoverinfo: 'text',
                        name: 'Exon',
                        showlegend: false,
                        mode: 'lines',
                        x: [item[0][0], item[1][0]],
                        y: [item[0][1], item[1][1]],
                        text: '[' + String(item[0][2]) + '-' + String(item[1][2]) + ']',
                        line: {
                            color: 'rgb(70,130,180)',
                            shape: 'linear',
                            width: 10,
                            simplify: true
                        }
                    };
                    trace_coding.push(trace_coding_item);
                    exton_num += 1;

                }

            }
            for (let i = 0; i < utr_records.length; i++) {
                var item = utr_records[i];
                var trace_utr_item = {
                    type: 'scatter',
                    visible: true,
                    hoverinfo: 'text',
                    showlegend: false,
                    mode: 'lines',
                    x: [item[0][0], item[1][0]],
                    y: [item[0][1], item[1][1]],
                    text: '[' + String(item[0][2]) + '-' + String(item[1][2]) + ']',
                    line: {
                        color: 'gray',
                        shape: 'linear',
                        width: 5,
                        simplify: true
                    }
                };
                trace_coding.push(trace_utr_item);
                exton_num += 1;
            }
            for (let i = 0; i < DNM_xy.length; i++) {
                var item = DNM_xy[i];
                var m_type = item[0][2].split(',')[2];
                var mut_color = get_DNM_color(m_type);
                console.log(mut_color);
                var dnm_item = {
                    type: 'scatter',
                    visible: true,
                    hoverinfo: 'text',
                    showlegend: false,
                    mode: 'lines',
                    x: [item[0][0], item[1][0]],
                    y: [item[0][1], item[1][1]],
                    legendgroup: mut_color,
                    name: mut_color,
                    text: String(item[0][2]),
                    hoverlabel: {
                        'font': {
                            'size': 10
                        }
                    },
                    line: {
                        color: mut_color,
                        shape: 'linear',
                        width: 12,
                        simplify: true
                    }
                };
                trace_coding.push(dnm_item);
            }
            var layout = {
                paper_bgcolor: 'rgb(249, 249, 249)',
                plot_bgcolor: 'rgb(249, 249, 249)',
                width: 800,
                height: get_heights(trans_len),
                hovermode: "closest",
                xaxis: {
                    showgrid: false,
                    zeroline: false,
                    showline: false,
                    showticklabels: false,
                    autorange: true,
                    titlefont: {
                        family: 'Arial',
                    },
                },
                yaxis: {
                    titlefont: {
                        family: 'Arial',
                        size: 20,
                        color: 'lightgrey'
                    },
                    ticklen: 0.1,
                    showticklabels: true,
                    tickangle: 360,
                    tickfont: {
                        family: 'Arial, serif',
                        size: 12,
                        color: 'black'

                    },
                    exponentformat: 'e',
                    showexponent: 'ALL',
                },
                margin: {
                    l: 130,
                    r: 0,
                    t: 20,
                    pad: 0
                },
                // showlegend: false
            }
            Plotly.plot('Transcript_DNM_box', trace_coding, layout)
        },
        error: function (err) {
            console.log("错误！");
        }
    });

}

getData();