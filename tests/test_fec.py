from acoustic_token_modem.coding.fec import decode_identity, encode_identity


def test_identity_fec():
    assert decode_identity(encode_identity(b"abc")) == b"abc"
