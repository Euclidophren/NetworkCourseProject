from plotly.subplots import make_subplots
import plotly.graph_objects as go

def make_plot(labels, values):
    fig = make_subplots(rows=2, cols=2,
                        subplot_titles=("OS", "Processor", "Memory", "Video"))

    fig.add_trace(
        go.Pie(labels=labels[0], values=values[0]),
        row=1, col=1
    )

    fig.add_trace(
        go.Pie(labels=labels[1], values=values[1]),
        row=1, col=2
    )

    fig.add_trace(
        go.Pie(labels=labels[2], values=values[2]),
        row=2, col=1
    )

    fig.add_trace(
        go.Pie(labels=labels[3], values=values[3]),
        row=2, col=2
    )

    fig.update_layout(height=600, width=800, title_text= "Stats")
    fig.show()
