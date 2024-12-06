package solutions

import (
	"math"
)

// ((x - 9) / (x + 3)) ** 0.5
func SolveTask29(x float64) (float64, error) {
	if x >= -3 && x < 9 {
		return 0, ErrOutOfDomain
	}

	return math.Sqrt((x - 9) / (x + 3)), nil
}
