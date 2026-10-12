import json
import tempfile
import unittest
from pathlib import Path

from workbench import SPACES, initialize, inspect


class WorkbenchTests(unittest.TestCase):
    def test_initialize_creates_each_space_and_starter_artifacts(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)

            directories, files = initialize(root)

            self.assertEqual(directories, len(SPACES))
            self.assertGreaterEqual(files, len(SPACES))
            for space, details in SPACES.items():
                directory = root / "submissions" / space
                self.assertTrue(directory.is_dir())
                self.assertTrue((directory / "README.md").is_file())
                for filename in details["files"]:
                    self.assertTrue((directory / filename).is_file())

            probes = json.loads(
                (root / "submissions" / "test-cases" / "starter-probes.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertEqual(len(probes), 4)
            self.assertTrue(all("expected_behavior" in probe for probe in probes))

    def test_initialize_is_idempotent_and_preserves_existing_files(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            initialize(root)
            readme = root / "submissions" / "source-files" / "README.md"
            readme.write_text("user content\n", encoding="utf-8")

            directories, files = initialize(root)

            self.assertEqual((directories, files), (0, 0))
            self.assertEqual(readme.read_text(encoding="utf-8"), "user content\n")

    def test_inspect_reports_spaces_and_file_counts(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            initialize(root)

            spaces, total_files = inspect(root)

            self.assertEqual(len(spaces), len(SPACES))
            self.assertTrue(all(exists for _, exists, _ in spaces))
            self.assertEqual(total_files, sum(count for _, _, count in spaces))

    def test_inspect_handles_uninitialized_root(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            spaces, total_files = inspect(Path(temporary_directory))

            self.assertTrue(all(not exists for _, exists, _ in spaces))
            self.assertEqual(total_files, 0)

    def test_submission_documents_are_populated(self):
        project_root = Path(__file__).resolve().parent
        documents = list((project_root / "submissions").rglob("*.md"))

        self.assertGreaterEqual(len(documents), 10)
        for document in documents:
            with self.subTest(document=document.relative_to(project_root)):
                content = document.read_text(encoding="utf-8").strip()
                self.assertGreaterEqual(len(content), 40)
                lines = content.splitlines()
                for index, line in enumerate(lines):
                    if not line.startswith("#"):
                        continue
                    next_content = next(
                        (candidate for candidate in lines[index + 1 :] if candidate.strip()),
                        None,
                    )
                    if next_content is None:
                        self.fail(f"Empty section heading in {document}: {line}")
                    self.assertFalse(
                        next_content.startswith("#"),
                        f"Empty section heading in {document}: {line}",
                    )


if __name__ == "__main__":
    unittest.main()
import json
import tempfile
import unittest
from pathlib import Path

from workbench import SPACES, initialize, inspect


class WorkbenchTests(unittest.TestCase):
    def test_initialize_creates_each_space_and_starter_artifacts(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)

            directories, files = initialize(root)

            self.assertEqual(directories, len(SPACES))
            self.assertGreaterEqual(files, len(SPACES))
            for space, details in SPACES.items():
                directory = root / "submissions" / space
                self.assertTrue(directory.is_dir())
                self.assertTrue((directory / "README.md").is_file())
                for filename in details["files"]:
                    self.assertTrue((directory / filename).is_file())

            probes = json.loads(
                (root / "submissions" / "test-cases" / "starter-probes.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertEqual(len(probes), 4)
            self.assertTrue(all("expected_behavior" in probe for probe in probes))

    def test_initialize_is_idempotent_and_preserves_existing_files(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            initialize(root)
            readme = root / "submissions" / "source-files" / "README.md"
            readme.write_text("user content\n", encoding="utf-8")

            directories, files = initialize(root)

            self.assertEqual((directories, files), (0, 0))
            self.assertEqual(readme.read_text(encoding="utf-8"), "user content\n")

    def test_inspect_reports_spaces_and_file_counts(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            initialize(root)

            spaces, total_files = inspect(root)

            self.assertEqual(len(spaces), len(SPACES))
            self.assertTrue(all(exists for _, exists, _ in spaces))
            self.assertEqual(total_files, sum(count for _, _, count in spaces))

    def test_inspect_handles_uninitialized_root(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            spaces, total_files = inspect(Path(temporary_directory))

            self.assertTrue(all(not exists for _, exists, _ in spaces))
            self.assertEqual(total_files, 0)


if __name__ == "__main__":
    unittest.main()
