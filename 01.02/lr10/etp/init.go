package etp

import (
	"errors"
	"fmt"
	"lr10/solutions"
)

type tasknum byte

const (
	num14 tasknum = iota
	num29
)

var (
	errUnknownTask = errors.New("unknown task")
)

func (tnum tasknum) String() string {
	switch tnum {
	case num14:
		return "14"
	case num29:
		return "29"
	default:
		return ""
	}
}

func ParseTaskNum(s string) (tasknum, error) {
	switch s {
	case "14":
		return num14, nil
	case "29":
		return num29, nil
	default:
		return 0, errUnknownTask
	}
}

func InitProc() {
	fmt.Println("Enter task number and value, separate them by space.")
	var tnum string
	var value float64
	if _, err := fmt.Scan(&tnum, &value); err != nil {
		fmt.Println(err)
		return
	}
	task, err := ParseTaskNum(tnum)
	if err != nil {
		fmt.Println(err)
		return
	}
	switch task {
	case num14:
		fmt.Println(solutions.SolveTask14(value))
	case num29:
		fmt.Println(solutions.SolveTask29(value))
	}
	fmt.Println("There is 2 values, first is answer, second is error.")
}
