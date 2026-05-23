"""Unit tests for emotion detection package."""

import json
import unittest
from unittest.mock import Mock, patch

from EmotionDetection import emotion_detector


class EmotionDetectionTests(unittest.TestCase):
    """Validate dominant emotion output for required statements."""

    def test_dominant_emotions(self):
        cases = {
            "I am glad this happened": "joy",
            "I am really mad about this": "anger",
            "I feel disgusted just hearing about this": "disgust",
            "I am so sad about this": "sadness",
            "I am really afraid that this will happen": "fear",
        }

        def fake_post(url, json=None, headers=None, timeout=20):
            text = json["raw_document"]["text"]
            dominant = cases[text]
            base = {
                "anger": 0.01,
                "disgust": 0.01,
                "fear": 0.01,
                "joy": 0.01,
                "sadness": 0.01,
            }
            base[dominant] = 0.9
            mock_response = Mock()
            mock_response.text = json_module.dumps(
                {"emotionPredictions": [{"emotion": base}]}
            )
            return mock_response

        json_module = json
        with patch("emotion_detection.requests.post", side_effect=fake_post):
            for statement, expected in cases.items():
                with self.subTest(statement=statement):
                    result = emotion_detector(statement)
                    self.assertEqual(result["dominant_emotion"], expected)


if __name__ == "__main__":
    unittest.main()
