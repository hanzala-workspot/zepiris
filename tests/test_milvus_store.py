"""Unit tests for MilvusFaceStore helpers."""

from zepiris.services.milvus_store import _milvus_str


def test_milvus_str_plain_value() -> None:
    assert _milvus_str("abc123") == "abc123"


def test_milvus_str_escapes_double_quote() -> None:
    assert _milvus_str('te"nant') == 'te\\"nant'


def test_milvus_str_escapes_backslash() -> None:
    assert _milvus_str("back\\slash") == "back\\\\slash"


def test_milvus_str_escapes_backslash_before_quote() -> None:
    # Ensures backslash is escaped first so \" becomes \\\"
    assert _milvus_str('\\"') == '\\\\\\"'


def test_milvus_str_injection_attempt() -> None:
    payload = '" OR "1"=="1'
    escaped = _milvus_str(payload)
    # The closing quote must be escaped so the expression stays valid
    assert '"' not in escaped.replace('\\"', "")
