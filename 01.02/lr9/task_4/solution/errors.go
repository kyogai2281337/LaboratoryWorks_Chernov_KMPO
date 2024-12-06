package solution

import "errors"

var (
	ErrIncorrectInput = errors.New("incorrect input")
	ErrWrongLimit     = errors.New("allocation limit exceeded")
	ErrTooSmall       = errors.New("too small number")
)
