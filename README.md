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
====================     HMean   ====================
FPEMs_4_20ep :  96.42887798394662 [%]
FPEMs_4_400ep :  97.0417941413404 [%]
0.6129161573937836 [%p]
0.6356147351375604 [%]
====================     Precision       ====================
FPEMs_4_20ep :  96.09188643449124 [%]
FPEMs_4_400ep :  97.24255303319164 [%]
1.150666598700397 [%p]
1.197464886366698 [%]
====================     Recall          ====================
FPEMs_4_20ep :  96.76824149160925 [%]
FPEMs_4_400ep :  96.8418624818946 [%]
0.07362099028534885 [%p]
0.07607970254552214 [%]
====================    Time     ====================
FPEMs_4_20ep :  122.26804527076511 [ms]
FPEMs_4_400ep :  122.92722109201787 [ms]
0.6591758212527594 [ms]
0.5391235459706589 [%]
====================    End      ====================
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
test.jpg
```

---

### [Diff Res](https://github.com/Zerohertz/zerohertzPlotLib/blob/main/diffRes.py#L21)

> In

```python
Ver = ['FPEMs_4_200ep', 'FPEMs_4_400ep']

zpl.diffRes('../PANPP/outputs/target', 'test.jpg',
            [0, 0, 2000, 4000], Ver)
```
> Out

![Out](https://user-images.githubusercontent.com/42334717/224615383-d4eb46fd-b14f-4812-ad22-7c2a8bb6e6ba.png)