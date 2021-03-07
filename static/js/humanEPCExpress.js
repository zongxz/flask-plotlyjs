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
            console.log(alist[i])
            l.push(Math.log10(alist[i] + 1.0).toFixed(2));
        }
    }
    console.log(l)
    return l;
}

function get_averge(alist, normaliaze = false) {
    var float_alist = [];
    for (let i = 0; i < alist.length; i++) {
        if (alist[i] !== "") {
            float_alist.push(Number(alist[i]));
        } else {
            float_alist.push(Number(0))
        }
    }
    var result = sum(float_alist) / float_alist.length;
    if (normaliaze) {
        return Math.log10(result + 1).toFixed(3);
    } else {
        return result.toFixed(2);
    }
}


function get_x(dataType, alist) {
    var l = [];
    for (let i = 0; i < alist.length; i++) {
        l.push(dataType + " - " + alist[i])
    }
    return l;
}

function getData() {

    $.ajax({
        url: "http://127.0.0.1:5000/humanEPCExpressData",
        type: "GET",
        dataType: "json",
        data: {},
        success: function (data) {
            var tarces = [];
            for (let i = 0; i < data.length; i++) {
                var item_1 = data[i];
                var dataType = item_1['type'];
                var datas = dropx(item_1['data']);
                var period = item_1['period'];
                tarces.push({
                    y: datas,
                    x: get_x(dataType, period),
                    name: dataType,
                    boxpoints: "outliers",
                    line: {
                        width: 1
                    },
                    type: "box"
                })
            }
            var len = tarces.length;
            for (let i = 0; i < data.length; i++) {
                var item_2 = data[i];
                var dataType_2 = item_2['type'];
                var datas_2 = normalized(item_2['data']);
                var period_2 = item_2['period'];
                tarces.push({
                    y: datas_2,
                    x: get_x(dataType_2, period_2),
                    visible: false,
                    name: dataType_2,
                    boxpoints: "outliers",
                    line: {
                        width: 1
                    },
                    type: "box"
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
            for (let i = 0; i < 2; i++) {
                visible_list_1.push(false);
                visible_list_2.push(false);
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
                height: 400,
                width: 1000,
                hovermode: "closest",
                xaxis: {
                    showgrid: true,
                    zeroline: false,
                    showline: false,
                    showticklabels: true,
                    tickangle: 60,
                    titlefont: {
                        family: "Arial",
                    },
                },
                yaxis: {
                    titlefont: {
                        family: "Arial",
                    }

                },
                margin: {
                    l: 150,
                    r: 10,
                    b: 180,
                    t: 30,
                }
            }
            Plotly.plot('humanEPCExpress_box', tarces, layout)

        },
        error: function (err) {
            console.log("错误！");
        }
    });

}

getData();