[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=danitorres13_python-project-140\&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=danitorres13_python-project-140)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=danitorres13_python-project-140\&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=danitorres13_python-project-140)

### Hexlet tests and linter status:

[![Actions Status](https://github.com/danitorres13/python-project-140/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/danitorres13/python-project-140/actions)

---

## Description

Brain Games is a set of command-line interface (CLI) math games designed to train your brain.
The project includes several mini-games where the player must answer correctly to win:

* Even number check
* Calculator (basic arithmetic)
* Greatest Common Divisor (GCD)
* Arithmetic progression
* Prime number detection

The player must answer **three questions in a row correctly** to win. One mistake ends the game.

---

## Requirements

* Python 3.11 or higher
* uv package manager
* Make (for build commands)

---

## Installation

Clone the repository:

```bash
git clone https://github.com/danitorres13/python-project-140.git
cd python-project-140
```

Build the package:

```bash
make build
```

Locate the generated `.whl` file:

```bash
dir dist
```

Install the package (copy the generated file name):

```bash
uv tool install dist/<package-name>.whl
```

---

## Usage

Run any of the games using:

```bash
brain-even
brain-calc
brain-gcd
brain-progression
brain-prime
```

---

## Demo

### brain-even

https://youtu.be/rpdjZxYJS9E

### brain-calc

https://youtu.be/Sc7g7h6ttYg

### brain-gcd

https://youtu.be/PIfPFMuMOfA

### brain-progression

https://youtu.be/PL6qjFAG8gM

### brain-prime

https://youtu.be/HB_FDD7kq1I
