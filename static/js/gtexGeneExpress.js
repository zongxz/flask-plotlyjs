function get_col_color_dict(col_list) {
    var colors_list = ['rgb(255,255,0)', 'rgb(31,119,180)', 'rgb(215,42,43)', 'rgb(140,140,140)', 'rgb(44,160,44)',
        'rgb(0,0,0)', 'rgb(188,188,34)', 'rgb(144,238,144)', 'rgb(140,86,75)', 'rgb(255,127,14)',
        'rgb(188,189,34)', 'rgb(255,193,193)', 'rgb(238,16,118)', 'rgb(0,245,255)', 'rgb(139,0,0)',
        'rgb(122,197,205)', 'rgb(255,218,185)', 'rgb(84,255,159)', 'rgb(154,205,50)', 'rgb(238,180,34)',
        'rgb(139,115,85)', 'rgb(153,50,204)', 'rgb(205,197,191)', 'rgb(131,139,131)', 'rgb(255,222,173)',
        'rgb(0, 0,139 )', 'rgb(155, 48, 255)', 'rgb(79, 48, 205)', 'rgb(139, 102, 139)',
        'rgb(139, 34, 82)', 'rgb(131, 139, 131)', 'rgb(139,99 ,108 )', 'rgb(205, 0, 0)',
        'rgb(238, 207, 161)', 'rgb(139, 134, 130)', 'rgb(139, 90, 0)', 'rgb(16, 78, 139)',
        'rgb(139, 76, 57)', 'rgb(238, 44, 44)', 'rgb(255, 20, 147)', 'rgb(255, 99, 71)',
        'rgb(255, 140, 0)', 'rgb(210, 105, 30)', 'rgb(139, 105, 105)', 'rgb(34, 139, 34)',
        'rgb(124, 252, 0)', 'rgb(205, 190, 112)', 'rgb(162, 205, 90)', 'rgb(0, 139, 69)',
        'rgb(100, 149, 237)', 'rgb(47, 79, 79)', 'rgb(255, 218, 185)', 'rgb(0, 134, 139)',
        'rgb(155, 205, 155)', 'rgb(205, 255, 112)', 'rgb(102, 205, 170)'];
    var col_color_dict = {};
    var l = [];
    for (let i = 0; i < col_list.length; i++) {
        l.push(col_list[i].split("-")[0]);
    }
    var set = new Set(l)
    var col_prex;
    col_prex = [...set].sort();
    for (let i = 0; i < col_prex.length; i++) {
        var key = col_prex[i];
        col_color_dict[key] = colors_list[i];
    }
    return col_color_dict
}

function normalized(alist) {
    var l = [];
    for (let i = 0; i < alist.length; i++) {
        if (alist[i] !== 0) {
            l.push(Math.log2(alist[i] + 1.0).toFixed(2));
        } else {
            l.push(0);
        }
    }
    return l;
}


function get_x_col(alist) {
    var l = [];
    for (let i = 0; i < alist.length; i++) {
        if (!['gencode_id', 'gene_symbol'].includes(alist[i])) {
            l.push(alist[i])
        }
    }
    return l.sort()
}

function getData() {

    $.ajax({
        url: "http://127.0.0.1:5000/gtexGeneExpressData",
        type: "GET",
        dataType: "json",
        data: {},
        success: function (data) {
            var tarces = [];
            var x_col = get_x_col(Object.keys(data));
            var col_color_dict = get_col_color_dict(x_col);
            var y_data = [];
            var color_data = [];
            var y_normalized_data = [];
            for (let i = 0; i < x_col.length; i++) {
                var item = x_col[i];
                y_data.push(data[item]);
                var key = item.split("-")[0];
                color_data.push(col_color_dict[key]);
                y_normalized_data.push(normalized(data[item]));
            }
            for (let i = 0; i < x_col.length; i++) {
                tarces.push({
                    y: y_data[i],
                    name: x_col[i],
                    boxpoints: 'outliers',
                    marker: {
                        color: color_data[i]
                    },
                    line: {
                        width: 1
                    },
                    type: "box"
                });
            }
            for (let i = 0; i < x_col.length; i++) {
                tarces.push({
                    y: y_normalized_data[i],
                    name: x_col[i],
                    boxpoints: 'outliers',
                    visible : false,
                    marker: {
                        color: color_data[i]
                    },
                    line: {
                        width: 1
                    },
                    type: "box"
                });
            }
            console.log(tarces)
            var visible_list_original = [];
            var visible_list_normalized =[];
            for (let i = 0; i < x_col.length; i++) {
                visible_list_original.push(true);
                visible_list_normalized.push(false);
            }
            for (let i = 0; i < x_col.length; i++) {
                visible_list_original.push(false);
                visible_list_normalized.push(true);
            }
            console.log(visible_list_original);
            console.log(visible_list_normalized);
            var updatemenus = [{
                type: "buttons",
                active: -1,
                pad: {
                    r: 30,
                    t: 20,
                },
                buttons: [{
                    label: "original TPM",
                    method: "update",
                    args: [{"visible": visible_list_original},
                        {
                            "title": 'TPM without normalization',
                        }]
                },
                    {
                        label: "log<sub>2</sub> ( TPM + 1 )",
                        method: "update",
                        args: [{"visible": visible_list_normalized},
                            {
                                "title": "Normalized TPM",
                            }]
                    }],
            }]
            var layout = {
                updatemenus: updatemenus,
                paper_bgcolor: "rgb(249, 249, 249)",
                plot_bgcolor: "rgb(249, 249, 249)",
                height: 500,
                width: 1000,
                hovermode: "closest",
                xaxis: {
                    showgrid: true,
                    zeroline: false,
                    showline: false,
                    showticklabels: true,
                    tickangle: 70,
                    titlefont: {
                        family: "Arial",
                    },
                },
                yaxis: {
                    autorange:true,
                    showgrid:true,
                    zeroline:false,
                    titlefont: {
                        family: "Arial",
                    }

                },
                margin: {
                    l: 20,
                    r: 20,
                    b: 230,
                    t: 60,
                },
                showlegend: false
            }
            Plotly.plot('gtexGeneExpress_box', tarces, layout)

        },
        error: function (err) {
            var msg = '<div> There is no corresponding data published yet, ' +
                        'we will update it when such data available.  </div>';
            $("#gtexGeneExpress_box").html(msg);
        }
    });

}

getData();