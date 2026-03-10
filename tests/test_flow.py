import unittest
from scripts.content_radar import scan_hot_content

class TestContentHunter(unittest.TestCase):
    def test_scan_xhs(self):
        """测试小红书抓取逻辑"""
        results = scan_hot_content(platform="xhs", keyword="AI副业")
        self.assertTrue(len(results) > 0)
        self.assertEqual(results[0]['platform'], "xhs")

    def test_scan_x(self):
        """测试 Twitter (X) 抓取逻辑"""
        results = scan_hot_content(platform="x", keyword="OpenClaw")
        self.assertTrue(len(results) > 0)
        self.assertEqual(results[1]['platform'], "x")

if __name__ == "__main__":
    unittest.main()
