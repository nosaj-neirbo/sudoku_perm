## sudoku_perm — Killer Sudoku & Kakuro Permutations (CLI)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![CLI Tool](https://img.shields.io/badge/Type-Command%20Line-orange.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

`sudoku_perm` is a **fast, intuitive command-line tool** for Sudoku, Killer Sudoku, and Kakuro puzzle solvers.

It finds **all unique, order-irrelevant combinations of the digits 1–9** that add up to a given **sum** and **length**, with options for **duplication caps**, 
**must/exclude filters** (with per-length overrides), **multi-sum/multi-length queries**, and **slot-based candidate constraints**. 

Designed for clarity, readability, and solver practicality — perfect for cage analysis, Kakuro clue enumeration,  
or any logic puzzle requiring controlled digit combination searches.

---

### Features

✅ Order-irrelevant generation by sum and length  
✅ Single `--dupes` option for caps (global or per-digit; ranges; `G:N`; `D:0` excludes).  
✅ Per-length dupes via `L<length>:` (tightening only).  
✅ Global & per-length digit filters: `-m`/`--must`, `-x`/`--exclude`, and `--allowed` (via `L<length>:`)  
✅ Per-slot candidate constraints: `--slots`  
✅ Pinned positions: `--pin` (fix position=value and print results with pinned digits placed; others ascend)  
✅ Assignments: `--show-assignment` prints one valid placement (when `--slots`/`--pin` are present)  
✅ Assignments: `--all-fits` prints all valid placements; CSV/JSON include assignments in this mode  
✅ Grouping by length (or flat with `--flat`), counts-only summaries, colorized text  
✅ `--cage` helper: per-slot minima/maxima & digit frequency  
✅ Multi-sum support: `--sums 17 18-20` 

✅ `--explain` prints effective constraints per length before results  
✅ `--examples` provides quick help

---

### Install

#### Option A: Run from source
```bash
chmod +x sudoku_perm
./sudoku_perm --help
```

#### Option B: Application install
```bash
sudo apt-get update && sudo apt-get install -y pipx
pipx ensurepath

# reopen your shell if needed
pipx install .

sudoku-perm --help
```

---

### Quick Start

```bash
chmod +x sudoku_perm

# Basic usage: find all 3-digit combos summing to 15
./sudoku_perm 15 -l 3
```

Output:
```
=== Sudoku Combos: Sum 15 | Lengths 3 | Total 8 ===

[ 1 5 9 ]
[ 1 6 8 ]
[ 2 4 9 ]
[ 2 5 8 ]
[ 2 6 7 ]
[ 3 4 8 ]
[ 3 5 7 ]
[ 4 5 6 ]
```

---

### Duplication Caps — `--dupes` (aliases: `--allow-dupes`, `-d`)

You can specify **how many times each digit may appear**.

| Syntax | Meaning |
|--------|----------|
| `--dupes 2` | Global cap of 2 (each digit ≤ 2 times) |
| `--dupes G:3` | Explicit global cap of 3 |
| `--dupes 1,2:2` | Digits 1 and 2 may appear up to twice |
| `--dupes 2-4:3` | Digits 2, 3, 4 may appear up to 3 times |
| `--dupes 5:0` | Exclude digit 5 entirely |
| Global + per-digit | `--dupes 3 1,2:2` — Global cap 3, but 1 and 2 only twice |

#### Example
```bash
# Allow any digit up to twice, except 1 and 2 (only once)
./sudoku_perm 10 -l 3 --dupes 2 1,2:1
```

---

### Digit Filters

#### Must-have digits (`-m` / `--must`)
Ensure certain digits appear in every result.

```bash
./sudoku_perm 10 -l 3 -m 1 2
```

#### Exclude digits (`-x` / `--exclude`)
Prevent digits from appearing.

```bash
./sudoku_perm 10 -l 3 -x 9
```

#### Allowed digits only (`--allowed`)
Whitelist specific digits (all others disabled).

```bash
./sudoku_perm 10 -l 3 --allowed 1,3,5,7,9
```

---

### Slot Constraints — `--slots`

Control which digits are allowed in each position (1-indexed).

#### Single length
```bash
# Slot 1: 2 or 5
# Slot 2: 3–6
# Slot 3: 5 or 6
./sudoku_perm 12 -l 3 --dupes 2 --slots 1:2,5 2:3-6 3:5,6 --show-assignment
```

Output:
```
=== Sudoku Combos: Sum 12 | Lengths 3 | Total 2 ===

── Sum 12 · Length 3 · 2 combo(s) ──
  [ 2 5 5 ] -> s1=2, s2=5, s3=5
  [ 3 4 5 ] -> s1=3, s2=4, s3=5
```

#### Multiple lengths
```bash
./sudoku_perm 10 -l 2 3 --slots L2:1:1-9 2:1-9   --slots L3:1:1,2 2:3,4 3:5-9   --show-assignment
```

---

### Pinned positions — `--pin`
Fix a digit at a position and show results with pinned digits in place; other positions are filled ascending.

- Single length: `--pin 1=3 3=6`
- Multiple lengths: `--pin L3:1=3 L4:1=4 L5:1=5`

---

### Showing Assignments

- `--show-assignment` shows one valid placement (when `--slots`/`--pin` is used).
- `--all-fits` shows all valid placements (implies `--show-assignment`).
- Grouped by default. `--flat` prints a flat list; ignored when grouping isn’t relevant.

```bash
# Grouped by default
./sudoku_perm 12 -l 3 --dupes 2 --slots 1:2,5 2:3-6 3:5,6 --all-fits

# Flat (one line per fit)
./sudoku_perm 12 -l 3 --dupes 2 --slots 1:2,5 2:3-6 3:5,6 --all-fits -f
```

---

### Cage Stats — `--cage`

Append per-length helper info for puzzle building.

```
=== Sudoku Combos: Sum 15 | Lengths 3 | Total 8 ===
── Sum 15 · Length 3 · 8 combo(s) ──
  [ 1 5 9 ]
  [ 1 6 8 ]
  [ 2 4 9 ]
  [ 2 5 8 ]
  [ 2 6 7 ]
  [ 3 4 8 ]
  [ 3 5 7 ]
  [ 4 5 6 ]

  Cage helper:
   • per-slot min: [1, 4, 6]
   • per-slot max: [4, 6, 9]
   • digit frequency: {1:2, 2:3, 3:2, 4:3, 5:4, 6:3, 7:2, 8:3, 9:2}
```

---

### Output Formats

| Flag | Description |
|------|--------------|
| `--format text` | Default, human-readable (supports color) |
| `--format csv` | Exports to CSV |
| `--format json` | JSON format (can include `--cage`) |

```bash
./sudoku_perm 23 -l 2 3 4 5 --counts-only
./sudoku_perm 10 -l 3 --format csv
./sudoku_perm 15 -l 3 --format json --cage
```

---

### Tips

- All digits default to **1 use** unless modified by `--dupes`.  
- `--flat` is ignored when grouping isn’t relevant (e.g., single length, no fits).  
- Flags are designed to be composable — you can mix `--dupes`, `--slots`, and `--must` safely.

---

### Example Use Cases

- **Killer Sudoku:** Find cages summing to 23 in 4 cells with no repeats.  
- **Kakuro:** Enumerate all valid 3-digit sums for 24 across specific candidates.  
- **Sudoku Constraints:** Determine which digits can fill particular positions in a cage.  

---

### Installation

```bash
git clone https://github.com/yourusername/sudoku_perm.git
cd sudoku_perm
chmod +x sudoku_perm
```

Run:
```bash
./sudoku_perm --help
```

---

### License

**MIT License** — free for personal, educational, and commercial use.  
Please credit **Jason O'Brien** if you adapt or redistribute this project.
