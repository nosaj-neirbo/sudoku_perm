def test_multiple_sums_group_headers(cli):
    rc, out = cli("--sums", "17-18", "-l", "3", "--dupes", "2", "--no-color")
    assert rc == 0
    assert "=== Sudoku Combos: Sum 17" in out
    assert "=== Sudoku Combos: Sum 18" in out
