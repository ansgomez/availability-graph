import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np


########### Define your variables
X_MAX = 10
X_STEP = 0.1
tabtitle = "Availability Graph"

########### Set up the chart

fig = go.Figure()

def lambda_arg (step_):
    return (step_)
def mu_arg (step_):
    return (1)

for step in np.arange(0,X_MAX, X_STEP):
    coeff1 = (mu_arg(step)/(lambda_arg(step)+mu_arg(step)))
    coeff2 = (lambda_arg(step)/(lambda_arg(step)+mu_arg(step)))
    coeff3 = (lambda_arg(step)+mu_arg(step))
    fig.add_trace(
        go.Scatter(
            visible=False,
            line=dict(color="#027D3F", width=6),
            name="λ = " + str(step),
            x=np.arange(0,X_MAX, X_STEP),
            y = ( coeff1 + coeff2 * np.exp( -coeff3 * np.arange(0,X_MAX, X_STEP) ) )
            )
        )

#visualize first plot
fig.data[0].visible = True

steps = []
for i in range(len(fig.data)):
    i2 = 0.1*i
    steady_state = mu_arg(i2) / (mu_arg(i2)+lambda_arg(i2))
    mu_str = '<b>µ</b>= {} /h'.format(mu_arg(i2))
    lamba_str = '<b>λ</b>= {} /h'.format(lambda_arg(i2))
    ss_str = '<b>A(∞)</b>= {0:.2f}'.format(steady_state)
    title_str = " "+mu_str+"     "+lamba_str+"     "+ss_str+"<br> "
    step = dict(
        method="update",
        args=[{"visible": [False] * len(fig.data)},
                { "title": title_str }],
                label = str("%.2f" %(0.1*i))
    )
    step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
    steps.append(step)

sliders = [dict(
    active=0,
    currentvalue={"prefix": " λ Failure rate (failures per hour): "},
    pad={"t": 50},
    steps = steps[::10]
)]

fig.update_layout(
    sliders=sliders,
    xaxis_title="Hours",
    yaxis_title="Availability",
)

fig.update_yaxes(range=[0,1])

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title = tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    dcc.Graph(
        id='graph',
        figure=fig),
])

if __name__ == '__main__':
    app.run_server()
