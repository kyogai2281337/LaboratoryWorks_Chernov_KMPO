# Лабораторная работа №2. Аппроксимация корней на промежутке

## Структура

Для того, чтобы воссоздать среду выполнения в полном масштабе, мне пришлось сделать своеобразный компилятор математических уравнений. У меня был опыт в похожей сфере, мне довелось разрабатывать компилятор химических уравнений с вычислением графиков по delta(T) и исхода, поэтому с инициализацией рабочего пространства было просто. Затем, стало быть, необходимо ещё и правильно выводить формулы вычисления, его я тоже написал, если что чуть ниже покажу всё то, что упоминаю здесь. Ну и наконец, самое простое - режем интервал напополам, находим присутствие корня и так до того, пока наша целевая задача сокращения не будет больше, чем текущая разница в точках интервала.

---

## Реализация

Вывод программы:

```bash
"f: +2x^3-7x^2+3x-10x
 f': +6x^2-14x+3-10
 f'': +12x-14
 interval: [0.375, 0.4375]
 target: 0.1"

```

Код состоит из трех классов, у каждого из которых нет комментария, но если к сути, структура их порождения выглядит примерно так:

```log
Partition(одночлен)=>Equation(уравнение)=>Solver(класс, предост.решение)
```

Соответственно, минимальный спектр алгоритмов для решения задачи был раскрыт.