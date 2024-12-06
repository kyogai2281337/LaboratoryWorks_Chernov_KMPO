package solution_test

import (
	"lr9/task_4/solution"
	"testing"
)

func TestSolveModule(t *testing.T) {
	// * Добряки позитивятки
	t.Run("positive module", func(t *testing.T) {
		cs := []struct {
			input uint
			q     uint
			want  uint8
		}{
			{1, 1, 1},
			{123, 4, 0},
			{785444, 4, 3},
		}
		for _, run := range cs {
			actual, err := solution.Solve(run.input, run.q)
			if err != nil {
				t.Errorf("unexpected error: %v", err)
			}
			if actual != run.want {
				t.Errorf("expected: %d, actual: %d", run.want, actual)
			}
		}
	})

	// * Добряки негативятки
	t.Run("negative module", func(t *testing.T) {
		cs := []struct {
			input uint
			q     uint
			want  error
		}{
			{1, 10, solution.ErrIncorrectInput},
			{1, 2, solution.ErrTooSmall},
		}
		for _, run := range cs {
			_, err := solution.Solve(run.input, run.q)
			if err != run.want {
				t.Errorf("expected: %v, actual: %v", run.want, err)
			}
		}
	})
}
