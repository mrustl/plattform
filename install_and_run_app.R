################################################################################
### Improve Reproducibility ("environment.yml") and Automate Django Server Startup
### *** Note: Works Only on Windows! ***
################################################################################

install.packages("remotes", repos = "https://cloud.r-project.org")
remotes::install_github("kwb-r/kwb.python")

## Define dependencies (from "requirements.txt")
pkgs <- list(conda = c("django",
                       "django-crispy-forms",
                       "django-import-export",
                       "django-leaflet",
                       "django-pandas",
                       "jsonfield",
                       "numpy",
                       "pandas",
                       "plotly",
                       "python-decouple",
                       "requests",
                       "tablib"
                       ),
             py = c("django-geojson",
                    "sklearn",
                    "requests_oauthlib"
                    )
             )


### Define name of conda environment
env_name <- "plattform"

### Create conda environment and install conda/py packages in one call
kwb.python::conda_py_install(env_name = env_name,
                             pkgs = pkgs)

## Export python dependencies in yml
kwb.python::conda_export(condaenv = env_name, export_dir = ".")

## Opens default browser on windows and start webserver
kwb.python::run_django(condaenv = env_name,
                       cmd = "runserver",
                       path_manage.py = "manage.py")
