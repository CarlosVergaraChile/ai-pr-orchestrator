import unittest
from scripts.issue_router import normalize_issue

REPO = "CarlosVergaraChile/ai-pr-orchestrator"


def issue(**changes):
    v = {
        "state": "open",
        "author_association": "OWNER",
        "number": 21,
        "html_url": f"https://github.com/{REPO}/issues/21",
        "title": "Investigar escenario sintético",
        "labels": [{"name": "agent-approved"}, {"name": "agent:gemini"}],
    }
    v.update(changes)
    return v


class TestIssueRouter(unittest.TestCase):
    def test_approved(self):
        task = normalize_issue(issue(body="NEVER EXPORT THIS PRIVATE DETAIL"), REPO)
        self.assertEqual(task["agent"], "gemini")
        self.assertEqual(task["execution"], "dry-run")
        self.assertNotIn("body", task)
        self.assertNotIn("NEVER EXPORT", str(task))
        self.assertFalse(task["dispatch_to_external_provider"])

    def test_untrusted_author(self):
        with self.assertRaises(ValueError):
            normalize_issue(issue(author_association="NONE"), REPO)

    def test_missing_approval(self):
        with self.assertRaises(ValueError):
            normalize_issue(issue(labels=[{"name": "agent:gemini"}]), REPO)

    def test_multiple_agents(self):
        with self.assertRaises(ValueError):
            normalize_issue(issue(labels=[{"name": "agent-approved"}, {"name": "agent:gemini"}, {"name": "agent:grok"}]), REPO)

    def test_invalid_agent(self):
        with self.assertRaises(ValueError):
            normalize_issue(issue(labels=[{"name": "agent-approved"}, {"name": "agent:unknown"}]), REPO)

    def test_wrong_repository(self):
        with self.assertRaises(ValueError):
            normalize_issue(issue(), "OtherOwner/other")

    def test_pull_request_rejected(self):
        with self.assertRaises(ValueError):
            normalize_issue(issue(pull_request={"url": "x"}), REPO)

    def test_closed_rejected(self):
        with self.assertRaises(ValueError):
            normalize_issue(issue(state="closed"), REPO)

    def test_bad_issue_number(self):
        with self.assertRaises(ValueError):
            normalize_issue(issue(number=0), REPO)

    def test_title_oversized(self):
        with self.assertRaises(ValueError):
            normalize_issue(issue(title="x" * 161), REPO)


if __name__ == "__main__":
    unittest.main()
