# %% [markdown]
# # VS Code Debugging Example

import xarray as xr
import xcdat


def plot_10_timesteps(ds: xr.Dataset, var: str):
    """Plot the first 10 timesteps of a variable.

    Parameters
    ----------
    ds : xr.Dataset
        The dataset.
    var : str
        The name of the variable.
    """
    if var == "tas":
        ds[var].isel(time=slice(0, 10)).plot()
    else:
        raise ValueError(f"The variable, '{var}' does not exist in the dataset.")


# %% [markdown]
# ## Open a Dataset

filepath = "http://esgf.nci.org.au/thredds/dodsC/master/CMIP6/CMIP/CSIRO/ACCESS-ESM1-5/historical/r10i1p1f1/Amon/tas/gn/v20200605/tas_Amon_ACCESS-ESM1-5_historical_r10i1p1f1_gn_185001-201412.nc"
ds = xcdat.open_dataset(filepath, chunks={"time": "auto"})

ds

# %% [markdown]
# ## Global Spatial Average
ds_global_avg = ds.spatial.average("tas")

ds_global_avg

# %% [markdown]
# ## Plot an existing variable ("tas")
#%%
plot_10_timesteps(ds_global_avg, "tas")

# %% [markdown]
# ## Plot an invalid variable ("not_tas")
#%%
plot_10_timesteps(ds_global_avg, "not_tas")
