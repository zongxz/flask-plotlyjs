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
    console.log(l);
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

function all_tissue() {
    return ['adipocyte', 'adrenal gland', 'amniocyte', 'arachnoid cyst', 'ascites', 'blood',
        'blood platelet',
        'bone', 'bone marrow stromal cell', 'brain', 'breast', 'cardia', 'cerebral cortex',
        'B-lymphocyte',
        'cerebrospinal fluid', 'cerumen', 'cervical mucosa', 'colon', 'colon muscle',
        'colonic epithelial cell',
        'cytotoxic T-lymphocyte', 'esophagus', 'gall bladder', 'gut', 'hair follicle', 'heart',
        'helper T-lymphocyte', 'ileum epithelial cell', 'kidney', 'liver', 'lung', 'lymph node',
        'mesenchymal stem cell', 'milk', 'monocyte', 'myometrium', 'nasopharynx',
        'natural killer cell',
        'oral epithelium', 'osteosarcoma cell', 'ovary', 'pancreas', 'pancreatic islet',
        'pancreatic juice',
        'placenta', 'prefrontal cortex', 'prostate gland', 'proximal fluid (coronary sinus)',
        'rectum',
        'renal cell carcinoma cell', 'retina', 'saliva', 'salivary gland', 'seminal plasma',
        'seminal vesicle',
        'skin', 'spermatozoon', 'spinal cord', 'spleen', 'stomach', 'synovial fluid', 'testis',
        'thyroid gland',
        'tonsil', 'urinary bladder', 'urine', 'uterine cervix', 'uterus', 'vitreous humor'];
}

function getData() {

    $.ajax({
        url: "http://127.0.0.1:5000/proteinExpressData",
        type: "GET",
        dataType: "json",
        data: {},
        success: function (data) {
            if (data instanceof Array) {
                var all_tissues = all_tissue()
                var result_list = [];
                var x_list = [];
                var y_list = [];
                var array_list = [];
                var id_list = [];
                for (let i = 0; i < data.length; i++) {
                    var item_protein_exp = data[i];
                    var express_value = new Array(all_tissues.length);
                    var error_value = new Array(all_tissues.length);
                    var x = [];
                    var y = [];
                    var array = [];
                    var item_express_data = item_protein_exp['express_data']
                    result_list.push(item_express_data);
                    for (let j = 0; j < item_express_data.length; j++) {
                        var item_item = item_express_data[j];
                        for (let k = 0; k < all_tissues.length; k++) {
                            if (item_item['TISSUE_NAME'] === all_tissues[k]) {
                                express_value[k] = item_item['NORMALIZED_INTENSITY'];
                                error_value[k] = (parseFloat(item_item['MAX_NORMALIZED_INTENSITY']) -
                                    parseFloat(item_item['MIN_NORMALIZED_INTENSITY'])) / 2
                            }
                        }
                    }

                    for (let j = 0; j < all_tissues.length; j++) {
                        x.push(all_tissues[j]);
                        y.push(express_value[j]);
                        array.push(error_value[j])
                    }
                    id_list.push(item_protein_exp['uniprotkb_ac']);
                    x_list.push(x);
                    y_list.push(y);
                    array_list.push(array);
                }
                if ((x_list.length === y_list.length) && (x_list.length !== 0)) {
                    var trace = [];
                    for (let i = 0; i < x_list.length; i++) {
                        var x_item = x_list[i];
                        var y_item = y_list[i];
                        var array_item = array_list[i];
                        var id_item = id_list[i];
                        for (let j = 0; j < x_item.length; j++) {
                            if (["brain", 'arachnoid cyst', 'cerebral cortex', 'cerebrospinal fluid',
                                'prefrontal cortex', 'spinal cord'].includes(x_item[j])) {
                                x_item[j] = "<b>" + capitalize(x_item[j]) + "</b>";
                            } else {
                                x_item[j] = capitalize(x_item[j]);
                            }
                        }
                        trace.push({
                            x: x_item,
                            y: y_item,
                            name: id_item,
                            type: 'bar',
                            hoverinfo: 'all',
                            error_y: {
                                type: 'data',
                                array: array_item,
                                visible: true,
                            }
                        });
                    }
                    var layout = {
                        paper_bgcolor: 'rgb(249, 249, 249)',
                        plot_bgcolor: 'rgb(249, 249, 249)',
                        barmode: 'stack',
                        height: 400,
                        width: 1300,
                        title: '<br>Median protein expression</br>',
                        hovermode: "closest",
                        xaxis: {
                            showgrid: true,
                            zeroline: true,
                            showline: true,
                            showticklabels: true,
                            tickangle: 50,
                            titlefont: {
                                size: 8
                            },
                        },
                        yaxis: {
                            title: 'log <sub>10</sub> normalized iBAQ intensity',
                            autorange: true,
                            showgrid: true,
                            showticklabels: true,
                            exponentformat: 'e',
                            showexponent: 'ALL',
                        },
                        margin: {
                            l: 50,
                            r: 20,
                            b: 150,
                            t: 40,
                            pad: 0
                        },
                        // showlegend: false
                    }
                }
                Plotly.plot('ProteinExpress_box', trace, layout);
            }
            else {
                var msg = '<p>There is no corresponding data published yet, we will update it when such data available.</p>';
                console.log("wwww");
                $("#ProteinExpress_box").html(msg);
            }
        },
        error: function (err) {
            console.log("错误！");
        }
    });

}

getData();