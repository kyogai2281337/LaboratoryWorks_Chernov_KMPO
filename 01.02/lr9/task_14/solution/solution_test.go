package solution_test

import (
	"lr9/task_14/solution"
	"testing"
)

func TestSolveModule(t *testing.T) {
	// * Добряки позитивятки
	t.Run("positive module", func(t *testing.T) {
		cs := []struct {
			input uint8
			want  uint8
		}{
			{1, 1},
			{103, 2},
			{44, 2},
		}
		for _, run := range cs {
			actual, err := solution.Solve(run.input)
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
			input uint8
			want  error
		}{
			{152, solution.ErrWrongLimit},
			{200, solution.ErrWrongLimit},
		}
		for _, run := range cs {
			_, err := solution.Solve(run.input)
			if err != run.want {
				t.Errorf("expected: %v, actual: %v", run.want, err)
			}
		}
	})
}
