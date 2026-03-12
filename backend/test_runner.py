import os
import subprocess
import json
import sys

WORKSPACE_ROOT = os.path.join(os.path.dirname(__file__), "..", "workspace")


def ensure_frontend_setup():
    """Ensure frontend has package.json and node_modules."""

    frontend_dir = os.path.join(WORKSPACE_ROOT, "frontend")

    if not os.path.exists(frontend_dir):
        print("⚠️ Frontend folder not found.")
        return False

    package_json_path = os.path.join(frontend_dir, "package.json")

    if not os.path.exists(package_json_path):

        print("⚠️ No package.json found. Creating minimal one.")

        minimal_package = {
            "name": "generated-frontend",
            "version": "1.0.0",
            "private": True,
            "dependencies": {
                "react": "^18.2.0",
                "react-dom": "^18.2.0",
                "react-scripts": "5.0.1"
            },
            "scripts": {
                "test": "react-scripts test --watchAll=false"
            }
        }

        with open(package_json_path, "w") as f:
            json.dump(minimal_package, f, indent=2)

    if not os.path.exists(os.path.join(frontend_dir, "node_modules")):

        print("📦 Running npm install...")

        subprocess.run(
            ["npm", "install"],
            cwd=frontend_dir,
            check=False
        )

    return True


def run_pytest():
    """Run backend tests with pytest."""

    test_file = os.path.join(WORKSPACE_ROOT, "tests", "test_backend.py")

    if not os.path.exists(test_file):
        return {"passed": 0, "failed": 1, "coverage": "N/A", "error": "Test file missing"}

    cmd = [
        sys.executable,
        "-m",
        "pytest",
        test_file,
        "--json-report",
        "--json-report-file=backend_report.json",
        "--tb=no",
        "--disable-warnings"
    ]

    try:

        subprocess.run(cmd, cwd=WORKSPACE_ROOT, capture_output=True, text=True)

        report_path = os.path.join(WORKSPACE_ROOT, "backend_report.json")

        if os.path.exists(report_path):

            with open(report_path) as f:
                report = json.load(f)

            passed = report.get("summary", {}).get("passed", 0)
            failed = report.get("summary", {}).get("failed", 0)

            return {
                "passed": passed,
                "failed": failed,
                "coverage": "N/A"
            }

        return {"passed": 0, "failed": 1, "coverage": "N/A", "error": "pytest report missing"}

    except Exception as e:
        return {"passed": 0, "failed": 1, "coverage": "N/A", "error": str(e)}


def run_frontend_tests():
    """Run frontend tests."""

    frontend_dir = os.path.join(WORKSPACE_ROOT, "frontend")

    if not ensure_frontend_setup():
        return {"passed": 0, "failed": 1, "coverage": "N/A", "error": "frontend missing"}

    env = os.environ.copy()
    env["CI"] = "true"

    cmd = ["npm", "test", "--", "--watchAll=false"]

    try:

        result = subprocess.run(
            cmd,
            cwd=frontend_dir,
            env=env,
            capture_output=True,
            text=True
        )

        passed = 0
        failed = 0

        if "PASS" in result.stdout:
            passed = 1

        if "FAIL" in result.stdout:
            failed = 1

        return {
            "passed": passed,
            "failed": failed,
            "coverage": "N/A"
        }

    except Exception as e:

        return {
            "passed": 0,
            "failed": 1,
            "coverage": "N/A",
            "error": str(e)
        }


def run_tests():

    backend_results = run_pytest()
    frontend_results = run_frontend_tests()

    return {
        "backend": backend_results,
        "frontend": frontend_results
    }