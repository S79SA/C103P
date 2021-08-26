import pandas as pd
import plotly.express as px


fig = px.scatter(df, x="Cases", y="Per Country",
	          size="Percentage",color="Country",
                   size_max=60)
fig.show()
