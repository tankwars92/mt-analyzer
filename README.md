# MT Analyze

![Figure_1](https://github.com/user-attachments/assets/1cbcdf79-6245-4f70-a171-53aefd355a94)


Анализ производительности и расчет оптимальных значений для Luanti (Minetest).

1. **Среднее значение (mean)**:
```math
\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i
```

2. **Линейная регрессия (polyfit)**:
```math
y = mx + b
```
где m - наклон (memory_trend), b - точка пересечения с осью y

3. **Нормальное распределение (normal)**:
```math
f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}
```
где μ - среднее значение, σ - стандартное отклонение

4. **Порог FPS для оптимальной дистанции прорисовки**:
```math
\text{fps\_threshold} = 0.9 \times \bar{\text{fps}}
```
