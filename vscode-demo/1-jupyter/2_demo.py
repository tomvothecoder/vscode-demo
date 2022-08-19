# %% [markdown]
# # VS Code Jupyter Demo with Climate Data Analysis
#
# This notebook is a demo of Jupyter Support in VS Code with a climate data analysis.

# %%
%matplotlib inline

import xcdat
import xmovie
import tqdm

# %% [markdown]
# ## Open a Dataset
#
# We are using xarray's OPeNDAP support to open a file directly from ESGF.

# %%
filepath = "http://esgf.nci.org.au/thredds/dodsC/master/CMIP6/CMIP/CSIRO/ACCESS-ESM1-5/historical/r10i1p1f1/Amon/tas/gn/v20200605/tas_Amon_ACCESS-ESM1-5_historical_r10i1p1f1_gn_185001-201412.nc"
ds = xcdat.open_dataset(filepath, chunks={"time": "auto"})


# Unit adjust (-273.15, K to C)
ds["tas"] = ds.tas - 273.15

ds

# %% [markdown]
# ## Global Area Average

# %%
ds_global_avg = ds.spatial.average("tas")

# %%
ds_global_avg.tas

# %% [markdown]
# ### Plot the first 100 time steps

# %%

ds_global_avg.tas.isel(time=slice(0, 100)).plot()

# %% [markdown]
# ## Temporal Average (Yearly)

# %%
ds_yearly_avg = ds.temporal.group_average("tas", freq="year", weighted=True)

# %% [markdown]
# ### Visualization using xmovie

# %% [markdown]
# ![tas yearly averages](./temporal-average-yearly.gif)
#
# *This GIF was created using [xmovie](https://github.com/jbusecke/xmovie).*
#
# Sample ``xmovie`` code:
# ```python
# import xmovie
# mov = xmovie.Movie(ds_yearly_avg.tas)
# mov.save("temporal-average-yearly.gif")
# ```


