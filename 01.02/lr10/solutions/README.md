# Лабораторная работа №10

## Содержание
1. [Краткое описание работы](#1-краткое-описание-работы)
2. [Задачи для выполнения](#2-задачи-для-выполнения)
    - [#14](#задача-14)
    - [#29](#задача-29)
3. [Тесты](#3-тесты)
    - [#14](#тесты-для-задачи-14)
    - [#29](#тесты-для-задачи-29)
4. [Выводы](#4-выводы)

---

## 1. Краткое описание работы
Даны два выражения, которые требуется реализовать и протестировать. Мой номер по списку: **28**, поэтому были выбраны задачи **14** и **29**.

---

## 2. Задачи для выполнения

### Задача 14
Реализовать решение для выражения №14. Конкретное выражение будет дописано позднее.

### Задача 29
Реализовать решение для выражения №29. Конкретное выражение будет дописано позднее.

---

## 3. Тесты

> ⚠️ **Внимание:** в _Go_ EaV-типизированная обработка ошибок. это значит, чтоошибка здесь это тип данных проверяющийся по принципу `err != nil`, а не как в большинстве других ЯП нового поколения, по принципу `try-catch/except`


### Тесты для задачи 14

#### Таблица тестов
| № | Значение | Ожид. результат | Факт. результат | Статус теста |
|---|----------|----------------|-----------------|--------------|
| 1 | 10       | 0.907954       | 0.907954        | ✅           |
| 2 | -8       | -1.140623      | -1.140623       | ✅           |
| 3 | 100      | 0.990087       | 0.990087        | ✅           |
| 4 | 154      | 0.993543       | 0.993543        | ✅           |
| 5 | -1       | Ошибка         | Ошибка          | ✅           |
| 6 | 0        | Ошибка         | Ошибка          | ✅           |


### Тесты для задачи 29

#### Таблица тестов
| № | Значение | Ожид. результат | Факт. результат | Статус теста |
|---|----------|----------------|-----------------|--------------|
| 1 | 10       | 0.277350       | 0.277350        | ✅           |
| 2 | -8       | 1.843909       | 1.843909        | ✅           |
| 3 | 100      | 0.939944       | 0.939944        | ✅           |
| 4 | 154      | 0.961024       | 0.961024        | ✅           |
| 5 | -2       | Ошибка         | Ошибка          | ✅           |
| 6 | 6        | Ошибка         | Ошибка          | ✅           |

---

## 4. Выводы
Протестировано два выражения: задача №14 и задача №29. Все тесты, включая как корректные значения, так и граничные случаи, прошли успешно.

---

## Тестовый код
```go
package solutions_test

import (
	"lr10/solutions"
	"testing"
)

func TestSolveTask29(t *testing.T) {
	// * Positive tests
	t.Run("positive module", func(t *testing.T) {
		cs := []struct {
			input float64
			want  float64
		}{
			{10, 0.277350},
			{-8, 1.843909},
			{100, 0.939944},
			{154, 0.961024},
		}
		for _, run := range cs {
			actual, err := solutions.SolveTask29(run.input)
			if err != nil {
				t.Errorf("unexpected error: %v", err)
			}
			if actual != run.want {
				t.Errorf("expected: %f, actual: %f", run.want, actual)
			}
		}
	})

	t.Run("negative module", func(t *testing.T) {
		cs := []struct {
			input float64
			want  error
		}{
			{-2, solutions.ErrOutOfDomain},
			{6, solutions.ErrOutOfDomain},
		}
		for _, run := range cs {
			_, err := solutions.SolveTask29(run.input)
			if err != run.want {
				t.Errorf("expected: %v, actual: %v", run.want, err)
			}
		}
	})
}

func TestSolveTask14(t *testing.T) {
	// * Positive tests
	t.Run("positive module", func(t *testing.T) {
		cs := []struct {
			input float64
			want  float64
		}{
			{10, 0.907954},
			{-8, -1.140623},
			{100, 0.990087},
			{154, 0.993543},
		}
		for _, run := range cs {
			actual, err := solutions.SolveTask14(run.input)
			if err != nil {
				t.Errorf("unexpected error: %v", err)
			}
			if actual != run.want {
				t.Errorf("expected: %f, actual: %f", run.want, actual)
			}
		}
	})

	t.Run("negative module", func(t *testing.T) {
		cs := []struct {
			input float64
			want  error
		}{
			{-1, solutions.ErrOutOfDomain},
			{0, solutions.ErrOutOfDomain},
		}
		for _, run := range cs {
			_, err := solutions.SolveTask14(run.input)
			if err != run.want {
				t.Errorf("expected: %v, actual: %v", run.want, err)
			}
		}
	})
}
```