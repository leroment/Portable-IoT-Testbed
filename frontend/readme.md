# Web Dashboard

## Setup

Follow the installation instructions for the following required tools:
- [Nodejs](https://nodejs.org/en/download)
- [Yarn](https://classic.yarnpkg.com/en/docs/install)

### Installation

To install the dependencies for the project, run

```
yarn install
```

### Grafana

The dashboard uses [Grafana](https://grafana.com/) to display the real-time data from InfluxDB. Please follow the instructions in [grafana/README.md](../grafana/README.md) to set it up.

Once this is done, get the share url by:

1. Open the dashboard of each sensor
2. Press the down arrow next to the name of the panel
3. Press `Share`
4. Select `Embed`
5. Change settings as you wish (see Notes below for more info)
6. Copy the embed code into the `iframes` inside [src/dashboard/pages/Dashboard.js](src/dashboard/pages/Dashboard.js)

**Notes:**
- Use `from` and `to` query parameters of `now-5m` and `now` for recent data
- Use `refresh=5s` or similar for live updating graphs
- Ensure the `var-token` query parameter is set to the users relevant data-token.
- Use `light` theme to match the style of the dashboard

## Running

After the installation is completed, the dashboard development server can be ran using

```
yarn start
```

If dependencies have changed since the last time `yarn install` was run, you will need to run it again to install new dependencies.
