def test_missing_sum(cli):
    rc, out = cli("-l", "3")
    assert rc != 0

def test_invalid_sum_range(cli):
    rc, out = cli("--sums", "a-b", "-l", "3")
    assert rc != 0

def test_invalid_slots_position(cli):
    rc, out = cli("10", "-l", "3", "--slots", "0:1-9")
    assert rc != 0

def test_must_not_in_slots(cli):
    rc, out = cli("10", "-l", "3", "-m", "9", "--slots", "1:1-2", "2:1-2", "3:1-2")
    assert rc != 0 and "cannot fit any slot" in out

def test_dupes_conflicting_globals(cli):
    rc, out = cli("10", "-l", "3", "--dupes", "2", "G:3")
    assert rc != 0 and "only one global cap" in out
