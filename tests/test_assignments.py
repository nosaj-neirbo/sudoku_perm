def test_all_fits_expands(cli):
    rc, out = cli("12", "-l", "3", "--dupes", "2",
                  "--slots", "1:2,5", "2:3-6", "3:5,6",
                  "--all-fits", "--no-color")
    assert rc == 0
    assert "-> s1=" in out

def test_flat_ignored_when_not_relevant(cli):
    rc, out = cli("6", "-l", "3", "--flat", "--no-color")
    assert rc == 0
