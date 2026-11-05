#!/usr/bin/env python3
"""Tests for src/build_hype_prompt.py. Run: python3 -m unittest discover -s tests"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import build_hype_prompt as bhp


def obs(day, citations=0, hf_upvotes=0, github_stars=0):
    return {
        "date": f"2026-01-{day:02d}",
        "citations": citations,
        "influential_citations": 0,
        "hf_upvotes": hf_upvotes,
        "github_stars": github_stars,
    }


def window(first, last):
    """A full-length history that holds `first` until the last observation."""
    return [obs(day, **first) for day in range(1, bhp.HISTORY_CAP)] + [obs(bhp.HISTORY_CAP, **last)]


def paper(name, history):
    return {"id": f"http://arxiv.org/abs/{name}", "title": name, "score": 80, "hype_signal_history": history}


class CleanHistoryTest(unittest.TestCase):
    def test_failed_fetch_keeps_last_value(self):
        history = [obs(1, citations=5, hf_upvotes=2), obs(2, hf_upvotes=3), obs(3, citations=6, hf_upvotes=3)]
        cleaned = bhp.clean_history(history)
        self.assertEqual([e["citations"] for e in cleaned], [5, 5, 6])
        self.assertEqual([e["hf_upvotes"] for e in cleaned], [2, 3, 3])

    def test_missing_key_counts_as_zero(self):
        cleaned = bhp.clean_history([{"date": "2026-01-01", "hf_upvotes": 4}])
        self.assertEqual(cleaned, [{"date": "2026-01-01", "citations": 0, "influential_citations": 0, "hf_upvotes": 4, "github_stars": 0}])


class GainTest(unittest.TestCase):
    def test_full_history_counts_from_its_first_entry(self):
        self.assertEqual(bhp.gain(window({"citations": 7}, {"citations": 9})), 2)

    def test_short_history_counts_from_zero(self):
        self.assertEqual(bhp.gain([obs(1, hf_upvotes=65), obs(2, hf_upvotes=65)]), 65)

    def test_falling_signal_does_not_cancel_rising_one(self):
        history = window({"citations": 6, "hf_upvotes": 152}, {"citations": 31, "hf_upvotes": 94})
        self.assertEqual(bhp.gain(history), 25)


class FormatPaperTest(unittest.TestCase):
    def test_unchanged_observations_share_one_line(self):
        history = bhp.clean_history([obs(1, hf_upvotes=5), obs(2, hf_upvotes=5), obs(3, hf_upvotes=5), obs(4, hf_upvotes=20)])
        text = bhp.format_paper(paper("a", history), history)
        self.assertIn("  - 2026-01-01 to 2026-01-03: hf upvotes: 5\n", text)
        self.assertTrue(text.endswith("  - 2026-01-04: hf upvotes: 20"))
        self.assertEqual(text.count("  - "), 2)


class SelectPapersTest(unittest.TestCase):
    def test_papers_without_growth_are_left_out(self):
        gap = window({"citations": 7}, {"citations": 7})
        gap[3] = obs(4)
        papers = [
            paper("flat", window({"citations": 7}, {"citations": 7})),
            paper("gap", gap),
            paper("single", [obs(1, citations=7)]),
            paper("grew", window({"citations": 7}, {"citations": 8})),
        ]
        blocks, grew = bhp.select_papers(papers, 100_000)
        self.assertEqual(grew, 1)
        self.assertEqual([b.splitlines()[0] for b in blocks], ["### grew"])

    def test_largest_gain_comes_first(self):
        papers = [
            paper("big-but-slow", window({"github_stars": 9000}, {"github_stars": 9001})),
            paper("surging", window({"hf_upvotes": 2}, {"hf_upvotes": 40})),
        ]
        blocks, _ = bhp.select_papers(papers, 100_000)
        self.assertEqual([b.splitlines()[0] for b in blocks], ["### surging", "### big-but-slow"])

    def test_output_stops_at_the_size_limit(self):
        papers = [paper(f"p{n:02d}", [obs(1, hf_upvotes=1), obs(2, hf_upvotes=1 + n)]) for n in range(1, 51)]
        one = len(bhp.select_papers(papers[-1:], 100_000)[0][0])
        blocks, grew = bhp.select_papers(papers, 3 * one)
        self.assertEqual(grew, 50)
        self.assertEqual([b.splitlines()[0] for b in blocks], ["### p50", "### p49", "### p48"])
        blocks, _ = bhp.select_papers(papers, 3 * one - 1)
        self.assertEqual(len(blocks), 2)


if __name__ == "__main__":
    unittest.main()
