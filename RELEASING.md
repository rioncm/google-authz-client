# Releasing google-authz-client

This library is published to [PyPI](https://pypi.org/project/google-authz-client/) via GitHub Actions. Follow the steps below to cut a new release.

## 1. Prep work
1. Create a branch for the release (e.g., `release/v0.6.0`).
2. Update the version in `pyproject.toml`.
3. Add a section to `CHANGELOG.md` describing new changes.
4. Commit and open a pull request. Ensure the **CI** workflow is green.

## 2. Tag and publish
1. Merge the PR.
2. Create a Git tag that matches the version (ex: `git tag v0.6.0 && git push origin v0.6.0`).
3. Draft a GitHub Release for the new tag. Include highlights and link to the changelog.
4. When the release is published, the `Publish` workflow builds wheels/sdist and uploads to PyPI.

You can also trigger the workflow manually from the Actions tab via `workflow_dispatch`. Provide the tag name if you want to republish a prior build.

## 3. Secrets & access
Configure the following repository secrets before running the Publish workflow:

| Secret | Description |
| --- | --- |
| `PYPI_API_TOKEN` | API token scoped to the `google-authz-client` project on PyPI. |
| `TEST_PYPI_API_TOKEN` | Optional token for pushing prereleases to TestPyPI. |

Tokens should be created from your PyPI account under *Account settings → API tokens*. Use project-scoped tokens when possible.

## 4. Verifying artifacts
After the workflow completes:
1. Download the build artifacts from the Actions run (optional) and inspect the metadata.
2. Install from PyPI using `pip install google-authz-client==X.Y.Z` in a clean virtualenv.
3. Run the quick-start from the README to make sure dependencies install cleanly.
