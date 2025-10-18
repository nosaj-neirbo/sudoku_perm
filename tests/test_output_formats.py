import json
from io import StringIO

def test_csv(cli):
    rc, out = cli("10", "-l", "2", "--format", "csv")
    assert rc == 0
    assert "sum,length,combo" in out

def test_json(cli):
    rc, out = cli("15", "-l", "3", "--format", "json")
    assert rc == 0
    data = json.loads(out)
    assert "sum" in data and "groups" in data

def test_csv_json_with_assignments(cli):
    rc, out = cli("12", "-l", "3", "--dupes", "2",
                  "--slots", "1:2,5", "2:3-6", "3:5,6",
                  "--all-fits", "--format", "csv")
    assert rc == 0 and "assignment" in out
