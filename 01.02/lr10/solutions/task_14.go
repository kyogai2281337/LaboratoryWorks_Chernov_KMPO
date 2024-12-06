package solutions

import "math"

// ((x ** 2 - 0.25)** 0.5)/(x+1)
func SolveTask14(x float64) (float64, error) {
	if x == -1 || x > -0.5 && x < 0.5 {
		return 0, ErrOutOfDomain
	}
	return (math.Sqrt(x*x - 0.25)) / (x + 1), nil
}
