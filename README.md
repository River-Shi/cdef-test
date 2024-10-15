## Build
```
python setup.py build_ext --inplace
```

## Run Benchmark
```
python benchmark.py
```

## Result
I am testing on Macos 14.6.1, Chip Apple M3
```
Python BookL1 Benchmark Results:
Creation time: 0.200142 seconds
Access time:   0.105723 seconds

Cython CBookL1 Benchmark Results:
Creation time: 0.064651 seconds
Access time:   0.169590 seconds

```
