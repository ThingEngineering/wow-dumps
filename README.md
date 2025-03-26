# wow-data

World of Warcraft data dumps. This repository exists mostly to be used by [WoWthing](https://github.com/ThingEngineering/wowthing-again) and will:

- Generally only have dumps for a current-ish Live build
- Only have hotfixed data for `enUS` as that's my region

## Updating dumps

1. Install [wow.tools.local](https://github.com/Marlamin/wow.tools.local) and configure it to point at your WoW directory.
2. Run it (make sure WoW isn't running!)
3. Navigate to http://localhost:5000
4. `Tables` -> `Browse`
5. Pick a random table to look at
6. Tick `Use hotfixes?`
7. Hit the down arrow next to the `CSV` button -> `Download ZIP of all DB2s`
8. Extract the downloaded zip over files in the relevant region folder
