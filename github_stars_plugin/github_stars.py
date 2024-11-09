import obspython as obs
import requests

# Plugin settings
repo_owner = "repo owner"  # GitHub username
repo_name = "repo name"  # GitHub repository name
update_interval = 60 * 1000  # Interval in milliseconds (OBS timer uses ms)
text_source_name = "GitHub Stars"  # OBS text source name
access_token = "your_personal_access_token"  # Replace with your GitHub token


def fetch_star_count():
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}"
    headers = {"Authorization": f"token {access_token}"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data.get("stargazers_count", 0)
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return 0


def update_text_source():
    star_count = fetch_star_count()
    text = f"{repo_name} Stars: {star_count}"
    source = obs.obs_get_source_by_name(text_source_name)
    if source:
        settings = obs.obs_data_create()
        obs.obs_data_set_string(settings, "text", text)
        obs.obs_source_update(source, settings)
        obs.obs_data_release(settings)
        obs.obs_source_release(source)


def update_star_count_timer():
    update_text_source()


def script_description():
    return "Displays GitHub star count for a repository in an OBS text source."


def script_update(settings):
    global repo_owner, repo_name, update_interval, text_source_name, access_token
    repo_owner = obs.obs_data_get_string(settings, "repo_owner")
    repo_name = obs.obs_data_get_string(settings, "repo_name")
    update_interval = obs.obs_data_get_int(settings, "update_interval") * 1000
    text_source_name = obs.obs_data_get_string(settings, "text_source_name")
    access_token = obs.obs_data_get_string(settings, "access_token")

    obs.timer_remove(update_star_count_timer)
    obs.timer_add(update_star_count_timer, update_interval)


def script_defaults(settings):
    obs.obs_data_set_default_string(settings, "repo_owner", "username")
    obs.obs_data_set_default_string(settings, "repo_name", "repository")
    obs.obs_data_set_default_int(settings, "update_interval", 60)  # in seconds
    obs.obs_data_set_default_string(settings, "text_source_name", "GitHub Stars")


def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_text(
        props, "repo_owner", "Repository Owner", obs.OBS_TEXT_DEFAULT
    )
    obs.obs_properties_add_text(
        props, "repo_name", "Repository Name", obs.OBS_TEXT_DEFAULT
    )
    obs.obs_properties_add_int(
        props, "update_interval", "Update Interval (seconds)", 10, 3600, 10
    )
    obs.obs_properties_add_text(
        props, "text_source_name", "OBS Text Source", obs.OBS_TEXT_DEFAULT
    )
    obs.obs_properties_add_text(
        props, "access_token", "GitHub Access Token", obs.OBS_TEXT_PASSWORD
    )
    return props


def script_unload():
    obs.timer_remove(update_star_count_timer)
