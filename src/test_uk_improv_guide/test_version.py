def test_version():
    from uk_improv_guide import __version__ as v

    parts = [int(a) for a in v.split(".")]
    for p in parts:
        assert p >= 0
