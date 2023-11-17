import abc
from time import time
from typing import Dict, List, Tuple

import numpy as np

from audio_recognizer.config.settings import DEFAULT_FS


class BaseRecognizer(object, metaclass=abc.ABCMeta):
    def __init__(self, audio_recognizer):
        self.audio_recognizer = audio_recognizer
        self.Fs = DEFAULT_FS

    def _recognize(self, *data) -> Tuple[List[Dict[str, any]], int, int, int]:
        fingerprint_times = []
        hashes = set() 
        """
            to remove possible duplicated fingerprints we built a set.
        """
        for channel in data:
            fingerprints, fingerprint_time = self.audio_recognizer.generate_fingerprints(channel, Fs=self.Fs)
            fingerprint_times.append(fingerprint_time)
            hashes |= set(fingerprints)
        matches, dedup_hashes, query_time = self.audio_recognizer.find_matches(hashes)

        t = time()
        final_results = self.audio_recognizer.align_matches(matches, dedup_hashes, len(hashes))
        align_time = time() - t

        return final_results, np.sum(fingerprint_times), query_time, align_time

    @abc.abstractmethod
    def recognize(self) -> Dict[str, any]:
        """
        base class does nothing
        """
        pass 

