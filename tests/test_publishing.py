import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from publish_assets import publish


class DownloadPreservationTest(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / "repository"
        self.site = Path(self.temporary.name) / "site"
        self.manifest = {
            "files": {"memos/old-r1.pdf": "memos/history/memo-001-r1.pdf",
                      "memos/old-r2.pdf": "memos/memo-001-r2.pdf"},
            "published_files": ["memos/old-r1.pdf", "memos/old-r2.pdf"],
            "generated_assets": {"css/style.css": "assets/css/style.css"},
        }
        self.write(self.root / "docs/file-map.json", json.dumps(self.manifest).encode())
        self.write(self.root / "memos/history/memo-001-r1.pdf", b"earlier revision\r\n")
        self.write(self.root / "memos/memo-001-r2.pdf", b"current revision\n")
        self.write(self.site / "assets/css/style.css", b"body{color:black}")

    @staticmethod
    def write(path, data):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)

    def test_each_old_link_keeps_its_exact_revision(self):
        publish(self.site, self.root)
        publish(self.site, self.root)
        self.assertEqual((self.site / "memos/old-r1.pdf").read_bytes(), b"earlier revision\r\n")
        self.assertEqual((self.site / "memos/old-r2.pdf").read_bytes(), b"current revision\n")
        self.assertEqual((self.site / "css/style.css").read_bytes(), b"body{color:black}")

    def test_missing_source_fails_before_any_alias_is_written(self):
        (self.root / "memos/memo-001-r2.pdf").unlink()
        with self.assertRaises(FileNotFoundError):
            publish(self.site, self.root)
        self.assertFalse((self.site / "memos/old-r1.pdf").exists())

    def test_conflicting_existing_download_is_not_overwritten(self):
        target = self.site / "memos/old-r1.pdf"
        self.write(target, b"different document")
        with self.assertRaises(ValueError):
            publish(self.site, self.root)
        self.assertEqual(target.read_bytes(), b"different document")

    def test_manifest_cannot_write_outside_the_site(self):
        self.manifest["files"]["../outside.pdf"] = "memos/memo-001-r2.pdf"
        self.manifest["published_files"].append("../outside.pdf")
        self.write(self.root / "docs/file-map.json", json.dumps(self.manifest).encode())
        with self.assertRaises(ValueError):
            publish(self.site, self.root)
        self.assertFalse((self.site.parent / "outside.pdf").exists())


if __name__ == "__main__":
    unittest.main()
