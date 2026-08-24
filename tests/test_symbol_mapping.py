from acoustic_token_modem.coding.symbol_mapper import bits_to_bytes, bytes_to_bits


def test_bits_bytes():
    data = b"\x00\xff\x10"
    bits = bytes_to_bits(data)
    assert bits_to_bytes(bits) == data
