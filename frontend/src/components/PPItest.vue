<template>
  <div id="box">
    <h1>demo</h1>
    <div id="cy"></div>
  </div>
</template>

<script>
import cytoscape from 'cytoscape'

export default {
  name: 'cytoscape',
  components: {},
  data () {
    return {
      nodes: [{
        data: {
          id: 'n0'
        }
      },
      {
        data: {
          id: 'n1'
        }
      },
      {
        data: {
          id: 'n2'
        }
      },
      {
        data: {
          id: 'n3'
        }
      }

      ],
      edges: [{
        data: {
          source: 'n2',
          target: 'n1'
        }
      },
      {
        data: {
          source: 'n2',
          target: 'n3'
        }
      },
      {
        data: {
          source: 'n2',
          target: 'n0'
        }
      },
      {
        data: {
          source: 'n1',
          target: 'n0'
        }
      },
      {
        data: {
          source: 'n0',
          target: 'n1'
        }
      }
      ]
    }
  },
  methods: {
    createCytoscape () {
      cytoscape.warnings(false)
      // eslint-disable-next-line no-unused-vars
      const cy = cytoscape({
        container: document.getElementById('cy'),
        boxSelectionEnabled: false,
        userZoomingEnabled: true, // 滚轮缩放
        wheelSensitivity: 0.1,
        autounselectify: false,
        autoungrabify: true,
        layout: {
          // name: 'breadthfirst',
        },
        minZoom: 0.3,
        style: [{
          selector: 'node',
          style: {
            'content': 'data(id)',
            'text-opacity': 0.5,
            'height': 40,
            'width': 40,
            'pie-size': '100%',
            'text-valign': 'center',
            'text-halign': 'left'

            // 'pie-1-background-color': '#E8747C',
            // 'pie-1-background-size': 'mapData(occupy, 0, 10, 0, 100)',
          }
        },
        {
          selector: ':parent',
          css: {
            'text-valign': 'top',
            'text-halign': 'center'
            // 'text-halign': 'right',
            // 'text-rotation': '90deg', //文字旋转
          }
        },
        {
          selector: 'edge',
          style: {
            width: 3,
            label: 'data(label)',
            'target-arrow-shape': 'triangle',
            // "target-arrow-fill": "hollow", //箭头填充 空心
            'line-color': '#9dbaea',
            'target-arrow-color': '#9dbaea',
            'curve-style': 'bezier'
          }
        }

        ],
        elements: {
          // 节点数据
          nodes: this.nodes,
          //
          edges: this.edges
        }
      })
    }
  },
  mounted () {
    this.createCytoscape()
  }
}

</script>

<style>

  #box {
    width: 500px;
    height: 300px;
  }

  #cy {
    width: 100%;
    height: 100%;
  }

  h1 {
    opacity: 0.5;
    font-size: 1em;
  }

</style>
