package solution

import (
	"fmt"
)

var (
	conv = func(input uint) string { return fmt.Sprintf("%d", input) }
)

func Solve(input uint, q uint) (uint8, error) {
	// * Объявляем с нулевой счетчик? нет, сперва условие на ликвидность исполнения

	if q >= 10 {
		return 0, ErrIncorrectInput
	}

	if input < q {
		return 0, ErrTooSmall
	}

	stringifiedInput := conv(input)
	stringifiedQ := conv(q)[0]
	ctr := uint8(0)
	for _, l := range stringifiedInput {
		if byte(l) == stringifiedQ {
			ctr++
		}
	}
	return ctr, nil
}

func Solution() (string, error) {
	var input, q uint
	if _, err := fmt.Scanf("%d %d", &input, &q); err != nil {
		return "", fmt.Errorf("parsing error: %v", err)
	}
	resp, err := Solve(input, q)
	if err != nil {
		return "", fmt.Errorf("error finding solution: %v", err)
	}

	return fmt.Sprintf("%d", resp), nil
}
