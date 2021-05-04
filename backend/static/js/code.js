function show(array)
{
    const cy = window.cy = cytoscape({
        container: document.getElementById('cy'),
        boxSelectionEnabled: false,
        autounselectify: true,
        wheelSensitivity : 1,
        style: [
        {
          selector: 'node[group=\"attr_gene\"]',
          style: {
            'content': 'data(name)',
			"width": "80px",
			"height": "80px",
			"font-size": "40px",
			"text-valign": "center",
			"text-halign": "center",
             "background-color": "#EDCFB8",
			"text-outline-color": "#EDCFB8",
			"text-outline-width": "6px",
			"color": "#fff",
			"overlay-padding": "6px",
			"z-index": "10",
          }
        },
        {
          selector: 'node[group=\"attr_protein\"]',
          style: {
            'content': 'data(name)',
			"width": "80px",
			"height": "80px",
			"font-size": "40px",
			"text-valign": "center",
			"text-halign": "center",
             "background-color": "#D9A9A8",
			"text-outline-color": "#D9A9A8",
			"text-outline-width": "6px",
			"color": "#fff",
			"overlay-padding": "6px",
			"z-index": "10"
          }
        },
        {
          selector: 'node[group=\"attr_both\"]',
          style: {
            'content': 'data(name)',
			"width": "80px",
			"height": "80px",
			"font-size": "40px",
			"text-valign": "center",
			"text-halign": "center",
             "background-color": "#A57079",
			"text-outline-color": "#A57079",
			"text-outline-width": "6px",
			"color": "#fff",
			"overlay-padding": "6px",
			"z-index": "10"
          }
        },
        {
          selector: 'node[group=\"attr\"]',
          style: {
            'content': 'data(name)',
			"width": "80px",
			"height": "80px",
			"font-size": "40px",
			"text-valign": "center",
			"text-halign": "center",
            "background-color": "#669999",
			"text-outline-color": "#669999",
			"text-outline-width": "6px",
			"color": "#fff",
			"overlay-padding": "6px",
			"z-index": "10"
          }
        },
		  {
          selector: 'node[group=\"core\"]',
          style: {
            'content': 'data(name)',
			"width": "160px",
			"height": "160px",
			"font-size": "60px",
			"text-valign": "center",
			"text-halign": "center",
             "background-color": "#D2691E",
			"text-outline-color": "#D2691E",
			"text-outline-width": "6px",
			"color": "#fff",
			"overlay-padding": "6px",
			"z-index": "10"
          }
        },

        {
          selector: 'edge',
          style: {
            'curve-style': 'haystack',
            'haystack-radius': 0,
            'width':  'data(width)',
            'line-color': 'data(faveColor)'
          }
        }

      ],
    });
    for (var i=0; i < array.length; i++)
    {
        cy.add(array[i]);
    }
    cy.panzoom({
					// options here...
                    zoomFactor: 0.05, // zoom factor per zoom tick
                    zoomDelay: 45, // how many ms between zoom ticks
                    minZoom: 0.1, // min zoom level
                    maxZoom: 10, // max zoom level
                    fitPadding: 50, // padding when fitting
                    panSpeed: 10, // how many ms in between pan ticks
                    panDistance: 10, // max pan distance per tick
                    panDragAreaSize: 75, // the length of the pan drag box in which the vector for panning is calculated (bigger = finer control of pan speed and direction)
                    panMinPercentSpeed: 0.25, // the slowest speed we can pan by (as a percent of panSpeed)
                    panInactiveArea: 8, // radius of inactive area in pan drag box
                    panIndicatorMinOpacity: 0.5, // min opacity of pan indicator (the draggable nib); scales from this to 1.0
                    autodisableForMobile: true, // disable the panzoom completely for mobile (since we don't really need it with gestures like pinch to zoom)

                    // icon class names
                    sliderHandleIcon: 'fa fa-minus',
                    zoomInIcon: 'fa fa-plus',
                    zoomOutIcon: 'fa fa-minus',
                    resetIcon: 'fa fa-expand'
				});
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
      spacingFactor: undefined, // Applies a multiplicative factor (>0) to expand or compress the overall area that the nodes take up
      concentric: function( node ){ // returns numeric value for each node, placing higher nodes in levels towards the centre
      return node.degree();
      },
      levelWidth: function( nodes ){ // the letiation of concentric values in each level
      // return nodes.maxDegree() / 4;
          return 5;
      },
      animate: false, // whether to transition the node positions
      animationDuration: 500, // duration of animation in ms if enabled
      animationEasing: undefined, // easing of animation if enabled
      animateFilter: function ( node, i ){ return true; }, // a function that determines whether the node should be animated.  All nodes animated by default on animate enabled.  Non-animated nodes are positioned immediately when the layout starts
      ready: undefined, // callback on layoutready
      stop: undefined, // callback on layoutstop
      transform: function (node, position ){ return position; }


     });

    layout.run();
    cy.on('tap', 'node', function(){
      try { // your browser may block popups
        window.open( this.data('href') );
      } catch(e){ // fall back on url change
        window.location.href = this.data('href');
      }
    });
    // cy.panningEnabled(false);
    // cy.userZoomingEnabled(false);
    cy.minZoom(0.08);
    }


