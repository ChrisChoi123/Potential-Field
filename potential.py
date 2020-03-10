from plotly import graph_objects as go

import pandas as pd

z_data = pd.read_csv("equipotential.csv")

fig = go.Figure(data = [go.Surface(z = z_data.values)])

fig.update_traces(contours_z = dict(show = True, usecolormap = True,highlightcolor = "forestgreen", project_z=True))


fig.update_layout(title='3-D Potential Field',autosize=False, scene_camera_eye=dict(x=2.50,y=1.50,z=-0.64),width=700,height=700,scene = dict(
                    xaxis_title='x position (cm)',
                    yaxis_title='y position (cm)',
                    xaxis = dict(ticktext = [(2.00*i)for i in range(12)],tickvals = [i for i in range(12)]),
                    yaxis = dict(ticktext = [(2.00*i)for i in range(12)],tickvals = [i for i in range(12)]),
                    zaxis_title='Potential Difference (V)'), margin=dict(r=20, b=10, l=10, t=50))

fig.show()
