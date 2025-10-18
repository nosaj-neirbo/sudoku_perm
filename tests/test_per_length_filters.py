def test_must_exclude_allowed_global(cli):
    rc, out = cli("15", "-l", "3", "-m", "1", "2", "-x", "9", "--allowed", "1,3,5,7,9", "--no-color")
    assert rc != 0
    assert ("required" in out) or ("ERROR" in out)

def test_per_length_must_exclude_allowed(cli):
    rc, out = cli("19", "-l", "3", "4", "5", "--dupes", "1",
                  "-m", "1", "L3:3", "L4:4", "L5:5",
                  "-x", "L3:9",
                  "--allowed", "L3:1-9", "L4:1-9", "L5:1-9",
                  "--pin", "L3:1=3", "L4:1=4", "L5:1=5",
                  "--no-color")
    assert rc == 0
    s = out
    assert ("[ 3 " in s) or ("[ 4 " in s) or ("[ 5 " in s)

def test_must_conflict(cli):
    rc, out = cli("10", "-l", "3", "-m", "9", "-x", "9", "--no-color")
    assert rc != 0 and "required" in out
