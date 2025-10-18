def test_explain_has_sections(cli):
    rc, out = cli("23", "-l", "3", "--dupes", "2", "--explain", "--no-color")
    assert rc == 0
    s = out
    assert "allowed=" in s and "caps=" in s
