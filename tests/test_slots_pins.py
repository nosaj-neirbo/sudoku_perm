def test_slots_single_length_assignment(cli):
    rc, out = cli("12", "-l", "3", "--dupes", "2",
                  "--slots", "1:2,5", "2:3-6", "3:5,6",
                  "--show-assignment", "--no-color")
    assert rc == 0
    assert "-> s1=" in out

def test_pins_multi_length_display(cli):
    rc, out = cli("19", "-l", "3", "4", "5", "--dupes", "1",
                  "--pin", "L3:1=3", "L4:1=4", "L5:1=5",
                  "--no-color")
    assert rc == 0
    assert "[ 3 " in out or "[ 4 " in out or "[ 5 " in out

def test_pin_conflicts_slots(cli):
    rc, out = cli("10", "-l", "3",
                  "--slots", "1:1-2", "2:1-9", "3:1-9",
                  "--pin", "1=3",
                  "--no-color")
    assert rc != 0
    # human-friendly message should indicate a conflict (case-insensitive)
    assert ("conflict" in out.lower()) or ("ERROR" in out)
