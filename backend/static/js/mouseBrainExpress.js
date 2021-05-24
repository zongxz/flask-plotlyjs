function dropx(alist) {
    var l = [];
    for (let i = 0; i < alist.length; i++) {
        if (alist[i] === "") {
            l.push(0);
        } else {
            l.push(alist[i]);
        }
    }
    return l;
}

function normalized(alist) {
    var l = [];
    for (let i = 0; i < alist.length; i++) {
        if ([0, ""].includes(alist[i])) {
            l.push(0);
        } else {
            l.push(Math.log10(alist[i] + 1.0).toFixed(2));
        }
    }
    return l;
}

function get_x(type, alist) {
    var l = [];
    for (let i = 0; i < alist.length; i++) {
        l.push('<b>' + alist[i] + '</b> (' + capitalize(type) + ')');
    }
    return l;
}

function capitalize(str) {
    var s = str.toLowerCase();
    s = s.charAt(0).toUpperCase() + s.slice(1);
    return s
}

function getData() {

    $.ajax({
        url: "http://127.0.0.1:5000/mouseBrainExpressData",
        type: "GET",
        dataType: "json",
        data: {},
        success: function (data) {
            if (data === null) {
                var msg = '<div> There is no corresponding data published yet, ' +
                        'we will update it when such data available.  </div>';
                $("#MouseBrainExpress_box").html(msg);
            } else {

                var tarces = [];
                for (let i = 0; i < data.length; i++) {
                    var item = data[i];
                    var type = '';
                    var datas = [];
                    var period = [];
                    for (var k in item) {
                        type = k;
                        datas = dropx(item[k]['data']);
                        period = item[k]['period']
                    }

                    tarces.push({
                        y: datas,
                        x: get_x(type, period),
                        name: type,
                        boxpoints: 'outliers',
                        line: {width: 1},
                        type: 'box'
                    })
                }

                var len = tarces.length;
                for (let i = 0; i < data.length; i++) {
                    var item = data[i];
                    var type = '';
                    var datas = [];
                    var period = [];
                    for (var k in item) {
                        type = k;
                        datas = normalized(item[k]['data']);
                        period = item[k]['period']

                    }
                    tarces.push({
                        y: datas,
                        x: get_x(type, period),
                        name: type,
                        boxpoints: 'outliers',
                        line: {width: 1},
                        type: 'box',
                        visible: false
                    })
                }


                var visible_list_1 = [];
                var visible_list_2 = [];
                for (let i = 0; i < len; i++) {
                    visible_list_1.push(true);
                    visible_list_2.push(false);
                }
                for (let i = 0; i < len; i++) {
                    visible_list_1.push(false);
                    visible_list_2.push(true);
                }
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
                        args: [{"visible": visible_list_1},
                            {
                                "title": 'TPM without normalization',
                            }]
                    },
                        {
                            label: "log<sub>10</sub> ( TPM + 1 )",
                            method: "update",
                            args: [{"visible": visible_list_2},
                                {
                                    "title": "Normalized TPM",
                                }]
                        }],
                }]
                var layout = {
                    updatemenus: updatemenus,
                    paper_bgcolor: "rgb(249, 249, 249)",
                    plot_bgcolor: "rgb(249, 249, 249)",
                    height: 600,
                    width: 1300,
                    hovermode: "closest",
                    xaxis: {
                        showgrid: true,
                        zeroline: false,
                        showline: false,
                        showticklabels: true,
                        tickangle: 50,
                        titlefont: {
                            size: 8,
                            family: "Arial",
                        },
                    },
                    yaxis: {
                        autorange: true,
                        showgrid: true,
                        zeroline: false,
                        titlefont: {
                            family: "Arial",
                        }

                    },
                    margin: {
                        l: 30,
                        r: 10,
                        b: 250,
                        t: 30,
                    },
                    // showlegend: false
                }   
                console.log(tarces);
                Plotly.plot('MouseBrainExpress_box', tarces, layout);
            }
        },
        error: function (err) {
            var msg = '<div> There is no corresponding data published yet, ' +
                        'we will update it when such data available.  </div>';
            $("#MouseBrainExpress_box").html(msg);
        }
    });

}

getData();