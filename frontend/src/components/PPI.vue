<template>
  <div id="box" style="width: 1200px; height: 850px;">
    <div id="cy" style="width: 1200px; height: 850px;"></div>
  </div>
</template>

<script>
import cytoscape from 'cytoscape'
import axios from 'axios'

export default {
  name: 'cytoscape',
  components: {},
  methods: {
    createCytoscape () {
      axios.get('http://127.0.0.1:5000/PPI')
        .then((res) => {
          let network = res.data
          let len = network['nodes'].length
          let t = []
          let d = {
            'data': {'group': 'attr_both'},
            'group': 'nodes',
            'grabbable': true
          }
          for (let i = 0; i < len; i++) {
            d['data']['id'] = network['nodes_id'][i]
            d['data']['name'] = network['nodes'][i]
            // d['data']['position']['x'] += i * 20
            // d['data']['position']['y'] += i * 20
            t.push(d)
            d = {
              'data': {'group': 'attr_both'},
              'group': 'nodes',
              'grabbable': true
            }
          }
          let len1 = network['edge_list'].length
          let d1 = {
            'data': {'faveColor': '#BEBEBE', 'width': '1'},
            'group': 'edges'
          }
          for (let i = 0; i < len1; i++) {
            d1['data']['source'] = network['edge_list'][i]['edge'][0]
            d1['data']['target'] = network['edge_list'][i]['edge'][1]
            d1['data']['width'] = network['edge_list'][i]['evidence']
            d1['data']['id'] = i
            // d['data']['position']['x'] += i * 20
            // d['data']['position']['y'] += i * 20
            t.push(d1)
            d1 = {
              'data': {'faveColor': '#BEBEBE', 'width': '1'},
              'group': 'edges'
            }
          }
          console.log(t)
          const cy = window.cy = cytoscape({
            container: document.getElementById('cy'),
            boxSelectionEnabled: false,
            autounselectify: true,
            wheelSensitivity: 1,
            style: [
              {
                selector: 'node',
                style: {
                  'content': 'data(name)',
                  'width': '80px',
                  'height': '80px',
                  'font-size': '40px',
                  'text-valign': 'center',
                  'text-halign': 'center',
                  'background-color': '#A57079',
                  'text-outline-color': '#A57079',
                  'text-outline-width': '6px',
                  'color': '#fff',
                  'overlay-padding': '6px',
                  'z-index': '10'
                }
              },
              {
                selector: 'core',
                style: {
                  'content': 'data(name)',
                  'width': '160px',
                  'height': '160px',
                  'font-size': '60px',
                  'text-valign': 'center',
                  'text-halign': 'center',
                  'background-color': '#D2691E',
                  'text-outline-color': '#D2691E',
                  'text-outline-width': '6px',
                  'color': '#fff',
                  'overlay-padding': '6px',
                  'z-index': '10'
                }
              },
              {
                'selector': 'edge',
                'style': {
                  'curve-style': 'haystack',
                  'haystack-radius': 0,
                  'width': 'data(width)',
                  'line-color': 'data(faveColor)'
                }
              }
            ],
            elements: t
          })
          var layout = cy.layout({
            name: 'concentric',
            fit: true, // whether to fit the viewport to the graph
            padding: 5, // the padding on fit
            startAngle: 3 / 2 * Math.PI, // where nodes start in radians
            sweep: undefined, // how many radians should be between the first and last node (defaults to full circle)
            clockwise: true, // whether the layout should go clockwise (true) or counterclockwise/anticlockwise (false)
            equidistant: false, // whether levels have an equal radial distance betwen them, may cause bounding box overflow
            minNodeSpacing: 10, // min spacing between outside of nodes (used for radius adjustment)
            boundingBox: undefined, // constrain layout bounds; { x1, y1, x2, y2 } or { x1, y1, w, h }
            avoidOverlap: true, // prevents node overlap, may overflow boundingBox if not enough space
            nodeDimensionsIncludeLabels: false, // Excludes the label when calculating node bounding boxes for the layout algorithm
            height: undefined, // height of layout area (overrides container height)
            width: undefined, // width of layout area (overrides container width)
            spacingFactor: undefined
          })
          layout.run()
        })
    }
  },
  mounted () {
    this.createCytoscape()
  }
}

</script>
