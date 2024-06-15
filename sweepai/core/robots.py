import traceback
from robotexclusionrulesparser import RobotExclusionRulesParser
from security import safe_requests


def is_url_allowed(url, user_agent="*"):
    robots_url = "/".join(url.split("/")[:3]) + "/robots.txt"
    try:
        response = safe_requests.get(robots_url)
        robots_txt = response.text

        rerp = RobotExclusionRulesParser()
        rerp.parse(robots_txt)
        return rerp.is_allowed(user_agent, url)
    except SystemExit:
        raise SystemExit
    except Exception:
        traceback.print_exc()
        return False
