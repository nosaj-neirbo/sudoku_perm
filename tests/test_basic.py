def test_basic_flat(cli, no_ansi):
    rc, out = cli("6", "-l", "3", "--no-color", "--flat")
    assert rc == 0
    s = no_ansi(out)
    assert "[ 1 2 3 ]" in s
    assert "Total" not in s

def test_basic_grouped(cli, no_ansi):
    rc, out = cli("6", "-l", "3", "--no-color")
    assert rc == 0
    s = no_ansi(out)
    assert "=== Sudoku Combos: Sum 6 | Lengths 3" in s
    assert "[ 1 2 3 ]" in s

def test_version(cli):
    rc, out = cli("--version")
    assert rc == 0
    assert out.strip().count(".") >= 1
