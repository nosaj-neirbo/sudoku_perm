def test_global_dupes(cli):
    rc, out = cli("12", "-l", "3", "--dupes", "2", "--no-color", "--flat")
    assert rc == 0
    assert "[ 4 4 4 ]" not in out
    assert "[ 2 5 5 ]" in out or "[ 3 4 5 ]" in out

def test_global_g_colon(cli):
    rc, out = cli("12", "-l", "3", "--dupes", "G:3", "1,2:2", "--no-color", "--flat")
    assert rc == 0
    assert "[ 1 1 1 ]" not in out

def test_range_per_digit_caps(cli):
    rc, out = cli("12", "-l", "3", "--dupes", "2-5:2", "--no-color", "--flat")
    assert rc == 0
    assert "[ 2 2 2 ]" not in out

def test_per_length_dupes_tightening(cli):
    rc, out = cli("12", "-l", "3", "4", "--dupes", "G:3", "L4:1,2:2", "--no-color")
    assert rc == 0

def test_per_length_dupes_error_on_widen(cli):
    rc, out = cli("10", "-l", "3", "--dupes", "2", "L3:1:3", "--no-color")
    assert rc != 0 and "exceeds global cap" in out
