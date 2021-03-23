import numpy as np
import plotly
import plotly.graph_objs as go

# Generate a random signal
np.random.seed(42)
random_signal = np.random.normal(size=100)
print(list(range(len(random_signal))))
print(random_signal)

# Offset the line length by the marker size to avoid overlapping
marker_offset = 0.04


def offset_signal(signal, marker_offset):
    if abs(signal) <= marker_offset:
        return 0
    return signal - marker_offset if signal > 0 else signal + marker_offset


data = []
data.append(go.Scatter(
    x=list(range(len(random_signal))),
    y=random_signal,
    mode='markers',
    marker=dict(
        color='red',
        size=15
    )
))
data.append(go.Bar(
    x=[1, 2, 3, 4, 5],
    y=[0.5, 0.5, 0.5, 0.5],
    # mode='markers',
    marker=dict(
        color='yellow',
        line=dict(
            color='rgb(0,0,0)',
            width=5,
        )),
))
# Use the 'shapes' attribute from the layout to draw the vertical lines
layout = go.Layout(
    shapes=[dict(
        type='line',
        xref='x',
        yref='y',
        x0=i,
        y0=0,
        x1=i,
        y1=offset_signal(random_signal[i], marker_offset),
        line=dict(
            color='grey',
            width=3
        )
    ) for i in range(len(random_signal))],
    title='Lollipop Chart'
)

# Plot the chart
fig = go.Figure(data, layout)

# pyo.iplot(fig)
plotly.offline.plot(fig)
