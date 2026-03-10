import pytest
from audioConverter import verifyAudioConverter, audioConverter

def test_valid_format(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "1") # use for testing standard input on function, set attribute
    verifyAudioConverter("song.m4a", "mp3")

def test_invalid_format():
    with pytest.raises(SystemExit): # I use SystemExit instead because it exit after handling error
        verifyAudioConverter("song.pdf", "wav")

