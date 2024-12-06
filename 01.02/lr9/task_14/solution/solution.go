package solution

import (
	"fmt"
)

func Solve(input uint8) (uint8, error) {
	q := uint8(input % 2)

	if input >= 110 {
		return 0, ErrWrongLimit
	}

	ctr := uint8(0)
	for input > 0 {
		if input%2 == q {
			ctr++
		}
		input /= 10
	}
	return ctr, nil
}

func Solution() (string, error) {
	var input uint8
	if _, err := fmt.Scanf("%d", &input); err != nil {
		return "", fmt.Errorf("parsing error: %v", err)
	}
	resp, err := Solve(input)
	if err != nil {
		return "", fmt.Errorf("error finding solution: %v", err)
	}

	return fmt.Sprintf("%d", resp), nil
}
