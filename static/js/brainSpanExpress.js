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
            var geneName = data[0];
            var others_type = data[1];
            var list_others_data = data[2];
            var list_special_striatum = data[3];
            var list_special_cortex = data[4];
            var max = data[5];
            var traces = [];
            var line_special = [];
            var colors = ['rgb(127,127,127)', 'rgb(188,189,34)', '#BC3C29FF', '#20854EFF',
                'rgb(0,0,0)', 'rgb(188,188,34)', 'rgb(144,238,144)']
            if (others_type !== 0) {
                var i = 0;
                var attr = ['Early fetal\n8-9PCW', 'Early fetal\n10-12PCW', 'Early mid-fetal\n13PCW-15PCW',
                    'Early mid-fetal\n16PCW-18PCW',
                    'Late mid-fetal\n19PCW-23PCW', 'Late fetal\n24PCW-37PCW',
                    'Neonatal and early infancy\n0M(birth)-5M',
                    'Late infancy\n6M-11M', 'Early childhood\n1Y-5Y', 'Middle and late childhood\n6Y-11Y',
                    'Adolescence\n12Y-19Y', 'Young adulthood\n20Y-39Y', 'Middle adulthood\n40Y'];
                var list_tmp_striatum_ave = [];
                var list_tmp_striatum_num = [];
                for (let j = 0; j < 13; j++) {
                    list_tmp_striatum_ave.push(0);
                    list_tmp_striatum_num.push(0);
                }
                for (let j = 0; j < 13; j++) {
                    if (list_special_striatum[j] !== []) {
                        for (var item in list_special_striatum[j]) {
                            list_tmp_striatum_ave[i] += item;
                            list_tmp_striatum_num[i] += 1;
                        }
                    }
                    if (list_special_striatum[j] === []) {
                        list_tmp_striatum_ave[i] = '';
                    }
                }
                for (let j = 0; j < 13; j++) {
                    if (list_tmp_striatum_ave[j] !== '') {
                        list_tmp_striatum_ave[j] = list_tmp_striatum_ave[j] / list_tmp_striatum_num[j];
                    }
                }
                line_special.push({
                    series: [{
                        type: 'line',
                        data: list_tmp_striatum_ave,
                    }],
                    title: {
                        text: "striatum"
                    },
                    xAxis: {
                        data: attr,
                        type: "category",
                        interval: 0,
                        label_textsize: 9,
                        rotate: -30,
                    },
                    yAxis: {
                        type: 'value',
                        max: Math.ceil(max),
                    },
                    legend: {
                        selectedmode: false,
                        pos: "top",
                        orient: "vertical"
                    },
                    is_smooth: true,
                });
                traces.push({
                    x: attr,
                    y: list_tmp_striatum_ave,
                    type: 'scatter',
                    name: 'striatum',
                    line: {
                        shape: 'spline',
                        color: 'rgb(155, 48, 255)'
                    },
                    mode: 'lines'
                });
                var list_tmp_cortex_ave = [];
                var list_tmp_cortex_num = [];
                for (let j = 0; j < 13; j++) {
                    list_tmp_cortex_ave.push(0);
                    list_tmp_cortex_num.push(0);
                }
                for (let j = 0; j < 13; j++) {
                    if (list_special_cortex[j] !== []) {
                        for (var item in list_special_cortex[j]) {
                            list_tmp_cortex_ave[i] += item;
                            list_tmp_cortex_num[i] += 1;
                        }
                    }
                    if (list_special_cortex[j] === []) {
                        list_tmp_cortex_ave[i] = '';
                    }
                }
                for (let j = 0; j < 13; j++) {
                    if (list_tmp_cortex_ave[j] !== '') {
                        list_tmp_cortex_ave[j] = list_tmp_cortex_ave[j] / list_tmp_cortex_num[j];
                    }
                }
                traces.push({
                    x: attr,
                    y: list_tmp_cortex_ave,
                    type: 'scatter',
                    name: 'cortex',
                    line: {
                        shape: 'spline',
                        color: 'rgb(122,197,205)'
                    },
                    mode: 'lines'
                });
                line_special.push({
                    series: [{
                        type: 'line',
                        data: list_tmp_cortex_ave,
                    }],
                    title: {
                        text: "cortex"
                    },
                    xAxis: {
                        data: attr,
                        type: "category",
                        interval: 0,
                        label_textsize: 9,
                        rotate: -30,
                    },
                    yAxis: {
                        type: 'value',
                        max: Math.ceil(max),
                        name:'LOG2(RPKM+1)',
                        name_pos: "middle",
                    },
                    legend: {
                        selectedmode: false,
                        pos: '10%',
                        orient: "horizontal"
                    },
                    is_smooth: true,
                });
                var max_length_striatum = 0;
                for (var item in list_special_striatum) {
                    if (item.length >= max_length_striatum) {
                        max_length_striatum = item.length;
                    }
                }
                for (let j = 0; j < 13; j++) {
                    if (list_special_striatum[j].length < max_length_striatum) {
                        for (let k = 0; k < max_length_striatum - list_special_striatum[j].length; k++) {
                            list_special_striatum[j].push('');
                        }
                    }
                }
                var max_length_cortex = 0;
                for (let j = 0; j < 13; j++) {
                    if (list_special_cortex[j].length < max_length_cortex) {
                        for (let k = 0; k < max_length_cortex - list_special_cortex[j].length; k++) {
                            list_special_cortex[j].push('');
                        }
                    }
                }

                for (let j = 0; j < max_length_striatum; j++) {
                    var list_tmp_striatum = [];
                    for (let k = 0; k < 13; k++) {
                        list_tmp_striatum.push(list_special_striatum[k][j]);
                    }
                    traces.push({
                        x: attr,
                        y: list_tmp_striatum,
                        type: 'scatter',
                        mode: 'markers',
                        marker: {
                            color: 'rgb(155, 48, 255)',
                        },
                        showlegend: false,
                        hoverinfo: 'all',
                        name: 'striatum'
                    });
                }

                for (let j = 0; j < max_length_cortex; j++) {
                    var list_linshi_cortex = [];
                    for (let k = 0; k < 13; k++) {
                        list_linshi_cortex.push(list_special_cortex[k][j]);
                    }
                    traces.push({
                        x: attr,
                        y: list_linshi_cortex,
                        type: 'scatter',
                        mode: 'markers',
                        marker: {
                            color: 'rgb(122,197,205)',
                        },
                        showlegend: false,
                        name: 'cortex'
                    });
                }
                var t = 0;
                for (let j = 0; j < others_type.lenth; j++) {
                    var item = others_type[i];
                    traces.push({
                        x: attr,
                        y: list_others_data[t],
                        name: item,
                        line: {
                            shape: 'spline',
                            color: colors[j]
                        },
                        mode: "lines",
                    });
                    t += 1;
                }
            }


            var layout = {
                paper_bgcolor: 'rgb(249, 249, 249)',
                plot_bgcolor: 'rgb(249, 249, 249)',
                width: 800,
                height: 1000,
                hovermode: "closest",
                xaxis: {
                    showgrid: true,
                    zeroline: true,
                    showline: true,
                    showticklabels: true,
                    tickangle: 25,
                    titlefont: {
                        family: 'Arial',
                    },
                },
                yaxis: {
                    autorange: true,
                    showgrid: true,
                    zeroline: true,
                    title: 'log<sub>2</sub> ( RPKM + 1 )',
                    titlefont:
                        {
                            family: 'Arial',
                        }
                },
                margin: {
                    l: 50,
                    r: 10,
                    t: 30,
                    b: 100
                },
                showlegend: true
            }
            Plotly.plot('Transcript_DNM_box', trace_coding, layout)
        },
        error: function (err) {
            console.log("错误！");
        }
    })
    ;

}

getData();