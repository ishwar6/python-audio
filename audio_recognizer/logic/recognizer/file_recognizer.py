from time import time
from typing import Dict

import audio_recognizer.logic.decoder as decoder
from audio_recognizer.base_classes.base_recognizer import BaseRecognizer
from audio_recognizer.config.settings import (ALIGN_TIME, FINGERPRINT_TIME, QUERY_TIME,
                                    RESULTS, TOTAL_TIME)


class FileRecognizer(BaseRecognizer):
    def __init__(self, audio_recognizer):
        super().__init__(audio_recognizer)

    def recognize_file(self, filename: str) -> Dict[str, any]:
        channels, self.Fs, _ = decoder.read(filename, self.audio_recognizer.limit)

        t = time()
        matches, fingerprint_time, query_time, align_time = self._recognize(*channels)
        t = time() - t

        results = {
            TOTAL_TIME: t,
            FINGERPRINT_TIME: fingerprint_time,
            QUERY_TIME: query_time,
            ALIGN_TIME: align_time,
            RESULTS: matches
        }

        return results

    def recognize(self, filename: str) -> Dict[str, any]:
        return self.recognize_file(filename)
