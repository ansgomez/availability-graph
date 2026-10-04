# availability-graph

Interactive plot of the availability A(t) of a two-state repairable system:

A(t) = μ/(λ+μ) + λ/(λ+μ) · e^(−(λ+μ)t)

with a slider over the failure rate λ (failures per hour) and a fixed repair rate μ = 1 per hour.
The plot title shows the steady-state availability A(∞) = μ/(λ+μ).

**Live:** <https://ansgomez.github.io/availability-graph/>

## How it works

`app.py` builds a single Plotly figure. The λ slider is part of the figure itself, so no
server is needed: `build_static.py` exports it to `docs/index.html`, which GitHub Pages serves.

```bash
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
python build_static.py   # regenerate docs/index.html after changing app.py
python app.py            # optional: run as a Dash app on http://127.0.0.1:8050
```

The app was originally deployed on Heroku (`availability-graph.herokuapp.com`), which ended
its free tier in 2022.

## Contributors

* [Denys Harshanov](https://github.com/dflymegold) (original Dash app and Heroku deployment)
* Andres Gomez
