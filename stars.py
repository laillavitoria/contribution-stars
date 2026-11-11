import os           
import requests

URL = "https://api.github.com/graphql"

QUERY = """
query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks {
          contributionDays {
            date
            contributionCount
          }
        }
      }
    }
  }
}
"""

def fetch_calendar(login, token):
    response = requests.post(
        URL,
        json={"query": QUERY, "variables": {"login": login}},
        headers={"Authorization": "bearer " + token},
    )
    response.raise_for_status()
    data = response.json()
    return data["data"]["user"]["contributionsCollection"]["contributionCalendar"]


if __name__ == "__main__":
    token = os.environ["GITHUB_TOKEN"]
    calendar = fetch_calendar("laillavitoria", token)
    print(calendar["totalContributions"])
    print(len(calendar["weeks"]))
    print(calendar["weeks"][-1])