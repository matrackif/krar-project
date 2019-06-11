# AS3

This project implements the Agent Language AS3.

## Authors

- Witaut Bajaryn: Design documentation; Examples; Testing the GUI; Bug fixing.
- Filip Matracki: Design documentation; The engine; model consistency validation; query parsing and execution.
- Ivan Matyazh: Design documentation; Testing the engine and preprocessor implementation; bug fixing.
- Weijia Yin: Verifying the documentation; Testing against the examples; Domain description validation.
- Enggar Dwi Prihastomo: Testing; bug fixing.

## Example GUI usage

Run the GUI with:
```
exec/gui.exe
```
or
```
PYTHONPATH="." python3.6 ./ui/gui.py
```

Input Scenario:
```
OBS:
ACS:
A Jim 1
```

Input Domain Description:
```
A causes f by Tom
B causes g by Jim
impossible B by Tom
```

Press `Initialise the Engine` and see the computed models in `Output`.

Input one or more queries:
```
possibly involved Jim
necessary involved Jim
possibly f at 2 when ExampleScenario
necessary f at 2 when ExampleScenario
possibly A at 1
necessary A at 1
```

Press `Test the Query` and see the results of the queries in `Output`.

## Example CLI usage

```
cat > lib.adl3 <<EOF
A causes f by Tom
B causes g by Jim
impossible B by Tom
EOF

cat > scenario.txt <<EOF
OBS:
ACS:
A Jim 1
EOF

cat > queries.txt <<EOF
possibly involved Jim
necessary involved Jim
possibly f at 2 when ExampleScenario
necessary f at 2 when ExampleScenario
possibly A at 1
necessary A at 1
EOF

$ ./main.py -l lib.txt -s scenario.txt -q queries.txt
```

## Running unit tests

```
python3.6 -m unittest
```

## Building a self-contained executable on Windows

Adjust the absolute path in `gui.spec`
to match the repository's location on your machine, then:

```
pip install pyinstaller
pyinstaller -F -y gui.spec
cp dist/gui.exe exec/gui.exe
```
