# webgl-globe-covid19
Visualize global confirmed cases of COVID-19. Updated daily at [earth.fightingcovid.net](https://earth.fightingcovid.net/#dashboard).

![screenshot](screenshot.png)

### Usage:

Use this code for rapid prototyping. Dependencies: Python 3 and `wget`. Clone the repository and run `./get_updates.sh` to pull the latest data from the Johns Hopkins CSSE repo. Data processing occurs automatically. Currently, the scripts `process_confirmed.py` and `process_deaths.py` use a "quasi-logarithmic" normalization function <img src="https://render.githubusercontent.com/render/math?math=x^nln(x), n\in(0,1)"> to achieve a more idiomatic scaling of values. Experiment with other root functions, logarithmic techniques, etc. to try and improve the balance between accuracy and viewability.

Change the JSON source and title in `index.html` to see deaths instead of cases. You can view the globe locally by running `python -m http.server` from the project directory and opening `localhost:8000`. Note that this globe uses time series data, so values are cumulative.