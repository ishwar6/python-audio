"""
Audio Recognizer JSON RESPONSE
"""
SONG_ID = "song_id"
SONG_NAME = 'song_name'
RESULTS = 'results'
HASHES_MATCHED = 'hashes_matched_in_input'

"""
Hashes fingerprinted in the db.
"""
FINGERPRINTED_HASHES = 'fingerprinted_hashes_in_db'

"""
Percentage regarding hashes matched vs hashes fingerprinted in the db.
"""
FINGERPRINTED_CONFIDENCE = 'fingerprinted_confidence'

"""
Hashes generated from the input.
"""
INPUT_HASHES = 'input_total_hashes'
"""
Percentage regarding hashes matched vs hashes from the input.
"""
INPUT_CONFIDENCE = 'input_confidence'

TOTAL_TIME = 'total_time'
FINGERPRINT_TIME = 'fingerprint_time'
QUERY_TIME = 'query_time'
ALIGN_TIME = 'align_time'
OFFSET = 'offset'
OFFSET_SECS = 'offset_seconds'

"""
DATABASE CLASS INSTANCES:
"""
DATABASES = {
    'postgres': ("audio_recognizer.database_handler.postgres_database", "PostgreSQLDatabase")
}

"""
TABLE SONGS
"""
SONGS_TABLENAME = "songs"

"""
SONGS FIELDS
"""
FIELD_SONG_ID = 'song_id'
FIELD_SONGNAME = 'song_name'
FIELD_FINGERPRINTED = "fingerprinted"
FIELD_FILE_SHA1 = 'file_sha1'
FIELD_TOTAL_HASHES = 'total_hashes'

"""
TABLE FINGERPRINTS
"""
FINGERPRINTS_TABLENAME = "fingerprints"

"""
FINGERPRINTS FIELDS
"""
FIELD_HASH = 'hash'
FIELD_OFFSET = 'offset'

"""
FINGERPRINTS CONFIG:
"""
CONNECTIVITY_MASK = 2

"""
Sampling rate, related to the Nyquist conditions, which affects
"""
DEFAULT_FS = 44100

"""
Size of the FFT window, affects frequency granularity
"""
DEFAULT_WINDOW_SIZE = 4096
"""
Ratio by which each sequential window overlaps the last and the
"""
DEFAULT_OVERLAP_RATIO = 0.5

"""
Degree to which a fingerprint can be paired with its neighbors. Higher values will
"""
DEFAULT_FAN_VALUE = 5  # 15 was the original value.
"""
Minimum amplitude in spectrogram in order to be considered a peak.
"""
DEFAULT_AMP_MIN = 10
"""
Number of cells around an amplitude peak in the spectrogram in order
"""
PEAK_NEIGHBORHOOD_SIZE = 10  # 20 was the original value.
"""
Thresholds on how close or far fingerprints can be in time in order
"""
MIN_HASH_TIME_DELTA = 0
MAX_HASH_TIME_DELTA = 200
"""
If True, will sort peaks temporally for fingerprinting;
"""
PEAK_SORT = True
"""
Number of bits to grab from the front of the SHA1 hash in the
"""
FINGERPRINT_REDUCTION = 40
"""
Number of results being returned for file recognition
"""
TOPN = 2
