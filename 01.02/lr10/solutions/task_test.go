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
