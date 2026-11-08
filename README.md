![The points of the marshalling yard close up at dusk, the fan of tracks opening toward the sorted rust brown wagons, a green signal lantern lit beside the rails and its light reflected on the steel](intro-banner.png)

# analyze-ioc-triage

![Gravel marshalling yard at dusk, one arriving line of rust brown wagons split across a fan of separate tracks, each wagon standing alone on its own rail, steel points gleaming between the tracks and one green signal lantern lit over the first lane](banner.png)

<p align="center"><img src="logo.png" alt="Fan of railway tracks from directly above spreading across pale gravel, three rust brown wagons standing one to a track and one green signal lantern lit beside the nearest rails" width="180"></p>

![Kelp bed cross section scene: light shafts sway, the otter rocks at its anchor, octopus arms curl around stems, and fish cross still coral](scene.svg)

# analyze-ioc-triage
Quickly triages multiple IOCs (IP addresses, domains, hashes) against public threat intelligence feeds (e.g., VirusTotal, AbuseIPDB) to prioritize investigation. - Focused on Data analysis and reporting

## Install
`git clone https://github.com/ShadowGuardAI/analyze-ioc-triage`


![Major section divider](sep-heavy.svg)

## Usage
`./analyze-ioc-triage [params]`


![Minor section divider](sep-light.svg)

## Parameters
- `-h`: Show help message and exit
- `--output`: Path to the output CSV file. Defaults to ioc_report.csv
- `--virustotal_api_key`: Your VirusTotal API key. The documented route is the VIRUSTOTAL_API_KEY environment variable. This command line option is kept as a fallback, but a key given here is visible in shell history and process listings, and the tool logs a warning when it is used.
- `--abuseipdb_api_key`: Your AbuseIPDB API key. The documented route is the ABUSEIPDB_API_KEY environment variable. This command line option is kept as a fallback, but a key given here is visible in shell history and process listings, and the tool logs a warning when it is used.

At least one API key is required: a run with no key performs no lookups, writes no report, and exits 1. Each row of the report carries a Lookup Status field with a per service status of not run, failed, no data, or completed, so a blank verdict column can be told apart from a lookup that never ran or one that failed.


![Major section divider](sep-heavy.svg)

## License
Copyright (c) ShadowGuardAI

> Holdfast pocket: a key given on the command line is visible in shell history and in process listings, and the tool logs a warning when one is used that way. The documented route for each key is its environment variable.
> Holdfast pocket: no parameter in this README states how the IOCs themselves are supplied, by file, by argument, or by standard input, so how the indicators are handed to the tool is undocumented.
