import argparse, json, time
import requests, certifi

GITHUB_API = "https://api.github.com/repos/{owner}/{repo}"

def fetch_repo(owner: str, repo: str, retries: int = 2, timeout: int = 10):
    url = GITHUB_API.format(owner=owner, repo=repo)
    last_exc = None
    for attempt in range(retries + 1):
        try:
            r = requests.get(url, verify=certifi.where(), timeout=timeout,
                             headers={"Accept": "application/vnd.github+json",
                                      "User-Agent": "notion-sync-cli"})
            r.raise_for_status()
            return r.json()
        except requests.RequestException as e:
            last_exc = e
            if attempt < retries:
                time.sleep(1.5)
            else:
                raise
    raise last_exc

def main():
    p = argparse.ArgumentParser(description="Fetch GitHub repo info (no auth)")
    p.add_argument("--owner", default="benjaminhoang760", help="GitHub owner/user")
    p.add_argument("--repo",  default="notion-sync", help="Repository name")
    p.add_argument("--save",  metavar="OUT.json", help="Save full JSON to file")
    p.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    args = p.parse_args()

    data = fetch_repo(args.owner, args.repo)

    # Useful summary for quick wins:
    summary = {
        "full_name": data.get("full_name"),
        "description": data.get("description"),
        "default_branch": data.get("default_branch"),
        "stars": data.get("stargazers_count"),
        "forks": data.get("forks_count"),
        "open_issues": data.get("open_issues_count"),
        "visibility": data.get("visibility"),
        "created_at": data.get("created_at"),
        "pushed_at": data.get("pushed_at"),
    }

    if args.pretty:
        print(json.dumps(summary, indent=2, ensure_ascii=False))
    else:
        print(summary)

    if args.save:
        with open(args.save, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Saved full JSON to {args.save}")

if __name__ == "__main__":
    main()
