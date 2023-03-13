<div align=center> <h2> :art: 
Zerohertz's Library for Visualization of Various Results :art: </h2> </div>

### Import

```python
import zerohertzPlotLib as zpl
```

---

### [Mean Processing Time](https://github.com/Zerohertz/zerohertzPlotLib/blob/main/meanProcessingTime.py#L6)

> In

```python
zpl.meanProcessingTime('../PANPP/results/time')
```

---

### [CLEval Plot](https://github.com/Zerohertz/zerohertzPlotLib/blob/main/CLEvalPlot.py#L7)

> In

```python
zpl.CLEvalPlot('../PANPP/results/time', fontsize=15)
```

> Out

```python
====================
0 FPEMs_4_400ep
1 FPEMs_4_180ep
2 FPEMs_4_300ep
3 FPEMs_4_200ep
4 FPEMs_4_20ep
5 TwinReader
====================
 4,1,3,2,0
Plotting...
```

![Out](https://user-images.githubusercontent.com/42334717/224615456-de09a7a8-b5df-47fa-8c50-20f4a0368d7c.png)

---

### [Print Res](https://github.com/Zerohertz/zerohertzPlotLib/blob/main/diffRes.py#L5)

> In

```python
zpl.printRes('../PANPP/outputs/target/FPEMs_4_400ep')
```

> Out

```python
CASE1.jpg
CASE2.jpg
CASE3.jpg
CASE4.jpg
CASE5.jpg
CASE6.jpg
CASE7.jpg
CASE8.jpg
pan_pp_target.py
test.jpg
```

---

### [Diff Res](https://github.com/Zerohertz/zerohertzPlotLib/blob/main/diffRes.py#L18)

> In

```python
Ver = ['FPEMs_4_200ep', 'FPEMs_4_400ep']

zpl.diffRes('../PANPP/outputs/target', 'test.jpg',
            [0, 0, 2000, 4000], Ver)
```
> Out

![Out](https://user-images.githubusercontent.com/42334717/224615383-d4eb46fd-b14f-4812-ad22-7c2a8bb6e6ba.png)