import os
import git
import time
from dotenv import load_dotenv
from urllib.parse import quote

load_dotenv()

def commit_and_push(repo_path, commit_message, max_retries=3):
    try:
        repo_url = os.getenv("GITHUB_REPO_URL")
        token = os.getenv("GITHUB_TOKEN")
        if not repo_url or not token:
            print("❌ Missing GITHUB_REPO_URL or GITHUB_TOKEN in .env")
            return False, "Missing credentials"

        # Remove any trailing slash
        repo_url = repo_url.rstrip('/')
        encoded_token = quote(token, safe='')

        # If repo folder doesn't exist → initialize
        if not os.path.exists(os.path.join(repo_path, ".git")):
            print("⚠️  Not a git repository. Initializing...")
            repo = git.Repo.init(repo_path)
            repo.create_remote('origin', repo_url)
        else:
            repo = git.Repo(repo_path)

        # Stage all changes
        repo.git.add(A=True)
        if repo.is_dirty(untracked_files=True):
            repo.index.commit(commit_message)
            print(f"✅ Committed: {commit_message}")
        else:
            print("ℹ️  No changes to commit.")
            return True, "No changes"

        authed_url = repo_url.replace("https://", f"https://{encoded_token}@")
        print(f"🔐 Pushing to: {authed_url.replace(encoded_token, '***')}")

        origin = repo.remote(name='origin')
        origin.set_url(authed_url)

        # Retry loop
        for attempt in range(1, max_retries+1):
            try:
                push_info = origin.push()
                for info in push_info:
                    if info.flags & info.ERROR:
                        print(f"❌ Push error: {info.summary}")
                        if attempt == max_retries:
                            return False, f"Push failed: {info.summary}"
                    else:
                        print("✅ Push successful")
                        return True, "Pushed successfully"
            except Exception as e:
                print(f"⚠️ Push attempt {attempt} failed: {e}")
                if attempt < max_retries:
                    time.sleep(2 ** attempt)  # exponential backoff
                else:
                    raise
        return False, "Push failed after retries"

    except Exception as e:
        print(f"❌ Exception in commit_and_push: {e}")
        return False, str(e)