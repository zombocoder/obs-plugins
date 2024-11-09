# GitHub Stars Plugin

Displays the star count of a specified GitHub repository in an OBS text source, with periodic updates to show the latest count.

#### Features

- Shows the current star count for any public GitHub repository.
- Configurable update interval.
- Uses authenticated GitHub requests for higher API rate limits.

#### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/zombocoder/obs-plugins.git
   ```

2. Navigate to the `github_stars_plugin` directory:
   ```bash
   cd obs-plugins/github_stars_plugin
   ```
3. Install the required Python libraries:

   ```bash
   /path/to/python3.12 -m pip install requests --user
   ```

   _(Replace `/path/to/python3.12` with the path to the Python interpreter used by OBS)_

4. Open **OBS Studio**, go to **Tools > Scripts**, and add `github_stars.py`.

#### Configuration

- **Repository Owner**: GitHub username.
- **Repository Name**: GitHub repository name.
- **Update Interval**: Interval in seconds for refreshing the star count.
- **Text Source Name**: The name of the OBS text source where the star count will display.
- **GitHub Access Token**: For authenticated requests to avoid rate limits. [Generate a token](https://github.com/settings/tokens).

### Future Plugins

This repository will be updated with additional OBS plugins. Check back for new features!

## Contributing

Feel free to contribute by submitting issues or pull requests for new plugins or enhancements to existing ones.

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
