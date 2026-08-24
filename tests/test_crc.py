from acoustic_token_modem.protocol.crc import crc32


def test_crc_stable():
    assert crc32(b"ATM0") == crc32(b"ATM0")
    assert crc32(b"a") != crc32(b"b")
