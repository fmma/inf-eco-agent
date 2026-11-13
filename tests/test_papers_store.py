#!/usr/bin/env python3
"""Tests for src/papers_store.py. Run: python3 -m unittest discover -s tests"""

import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import papers_store


def paper(arxiv_id, published):
    return {"id": arxiv_id, "published": f"{published}T00:00:00+00:00", "score": 50}


class PapersStoreTest(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.dir = Path(tmp.name) / "papers"
        patcher = mock.patch.object(papers_store, "PAPERS_DIR", self.dir)
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_load_without_database_is_empty(self):
        self.assertEqual(papers_store.load_papers(), [])

    def test_save_splits_by_publication_month(self):
        papers_store.save_papers([paper("a", "2026-03-01"), paper("b", "2026-01-15"), paper("c", "2026-03-31")])

        self.assertEqual(sorted(p.name for p in self.dir.iterdir()), ["2026-01.json", "2026-03.json"])
        self.assertEqual([p["id"] for p in papers_store.load_papers()], ["b", "a", "c"])

    def test_save_keeps_every_paper_and_field(self):
        papers = [paper("b", "2026-01-15"), paper("a", "2026-03-01")]
        papers[0]["hype_signal_history"] = [{"date": "2026-01-16", "citations": 1}]

        papers_store.save_papers(papers)

        self.assertEqual(papers_store.load_papers(), papers)

    def test_save_leaves_unchanged_month_untouched(self):
        papers = [paper("a", "2026-01-15"), paper("b", "2026-03-01")]
        papers_store.save_papers(papers)
        january = self.dir / "2026-01.json"
        before = january.stat().st_mtime_ns

        papers[1]["score"] = 90
        with mock.patch.object(Path, "write_text", autospec=True, side_effect=Path.write_text) as write:
            papers_store.save_papers(papers)

        self.assertEqual([call.args[0].name for call in write.call_args_list], ["2026-03.json"])
        self.assertEqual(january.stat().st_mtime_ns, before)
        self.assertEqual(papers_store.load_papers()[1]["score"], 90)


if __name__ == "__main__":
    unittest.main()
