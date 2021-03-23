function getData() {

    $.ajax({
        url: "http://127.0.0.1:5000/brainSpanData",
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
                    if (list_special_striatum[j].length !== 0) {

                        for (let k = 0; k < list_special_striatum[j].length; k++) {
                            var item = list_special_striatum[j][k];

                            list_tmp_striatum_ave[j] += item;
                            list_tmp_striatum_num[j] += 1;
                        }
                    }
                    if (list_special_striatum[j].length === 0) {
                        list_tmp_striatum_ave[j] = '';

                    }
                }

                for (let j = 0; j < 13; j++) {
                    if (list_tmp_striatum_ave[j] !== '') {
                        list_tmp_striatum_ave[j] = list_tmp_striatum_ave[j] / list_tmp_striatum_num[j];

                    }
                }
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
                    if (list_special_cortex[j].length !== 0) {
                        for (let k = 0; k < list_special_cortex[j].length; k++) {
                            var item = list_special_cortex[j][k];
                            list_tmp_cortex_ave[j] += item;
                            list_tmp_cortex_num[j] += 1;

                        }
                    }
                    if (list_special_cortex[j].length === 0) {
                        list_tmp_cortex_ave[j] = '';
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
                // line_special.push({
                //     series: [{
                //         type: 'line',
                //         data: list_tmp_cortex_ave,
                //     }],
                //     title: {
                //         text: "cortex"
                //     },
                //     xAxis: {
                //         data: attr,
                //         type: "category",
                //         interval: 0,
                //         label_textsize: 9,
                //         rotate: -30,
                //     },
                //     yAxis: {
                //         type: 'value',
                //         max: Math.ceil(max),
                //         name:'LOG2(RPKM+1)',
                //         name_pos: "middle",
                //     },
                //     legend: {
                //         selectedmode: false,
                //         pos: '10%',
                //         orient: "horizontal"
                //     },
                //     is_smooth: true,
                // });
                var max_length_striatum = 0;
                for (let j = 0; j < list_special_striatum.length; j++) {
                    var item = list_special_striatum[j];
                    if (item.length >= max_length_striatum) {
                        max_length_striatum = item.length;

                    }
                }

                for (let j = 0; j < 13; j++) {
                    var len = list_special_striatum[j].length;
                    if (len < max_length_striatum) {
                        var l = max_length_striatum - len;
                        for (let k = 0; k < l; k++) {
                            list_special_striatum[j].push('');
                        }
                    }
                }
                var max_length_cortex = 0;
                for (let j = 0; j < list_special_cortex.length; j++) {
                    var item = list_special_cortex[j];
                    if (item.length >= max_length_cortex) {
                        max_length_cortex = item.length;

                    }
                }

                for (let j = 0; j < 13; j++) {
                    var len = list_special_cortex[j].length;
                    if (len < max_length_cortex) {
                        var l = max_length_cortex - len;
                        for (let k = 0; k < l; k++) {
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
                for (let j = 0; j < others_type.length; j++) {
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
                width: 1000,
                height: 400,
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
            Plotly.plot('BrainSpanExpress_box', traces, layout)
        },
        error: function (err) {
            console.log("错误！");
        }
    })
    ;

}

getData();